#Django
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Count
import json

#Models
from .models import *
from user.models import Profile
from inv.models import *

#Forms
from .forms import *

#Plugins
from bootstrap_modal_forms.generic import BSModalReadView, BSModalDeleteView, BSModalCreateView, BSModalUpdateView

class IngresoNew(LoginRequiredMixin, CreateView):
    """Vista para crear nuevos ingresos"""
    model = Ingreso
    template_name = 'mov/ingresoForm.html'
    form_class = IngresoForm
    success_url = 'ingreso_list'
    success_message = "Ingreso creado exitosamente"

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            data = {}
            ings = json.loads(request.POST['ing'])
            ing = Ingreso()
            pro = Proveedores.objects.get(pk=int(ings['proveedor']))
            ing.proveedor = pro
            ing.usuario_creacion = self.request.user
            ing.fecha_ingreso = ings['fecha_ingreso']
            ing.save()
            for i in ings['productos']:
                producto = Productos.objects.get(pk=int(i['id']))
                det = DetIngreso()
                det.ingreso = ing
                det.producto = producto
                det.cantidad = int(i['cant'])
                producto.existencia += det.cantidad
                det.usuario_creacion = self.request.user
                det.save()
                producto.save()
        return JsonResponse(data, safe=False)

@login_required
def autocomplete(request):
    """Función para el mostrar todos los productos"""
    if 'term' in request.GET:
        data = []
        prods = Productos.objects.filter(estado=True, descripcion__icontains=request.GET.get('term'))[0:10]
        for i in prods:
            item = i.toJson()
            item['value'] = i.descripcion
            item['img'] = str(i.image.url)
            data.append(item)
        return JsonResponse(data, safe=False)


class IngresoList(LoginRequiredMixin, ListView):
    """Vista para mostrar todos los ingresos"""
    model = Ingreso
    template_name = 'mov/ingresos.html'
    context_object_name = 'ingresos'


class IngresoDetailView(LoginRequiredMixin, BSModalReadView):
    """Vista para mostrar el detalle de un ingreso"""
    model = Ingreso
    template_name = 'mov/ingresoDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalles'] = DetIngreso.objects.filter(ingreso=self.kwargs['pk'])
        return context


class IngresoEditView(LoginRequiredMixin, UpdateView):
    """Vista para editar un ingreso"""
    model = Ingreso
    template_name = 'mov/ingresoForm.html'
    form_class = IngresoForm
    success_url = 'ingreso_list'
    success_message = "Ingreso editado exitosamente"

    def form_valid(self, form):
        form.instance.usuario_modificion = self.request.user
        return super().form_valid(form)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            data = {}
            ings = json.loads(request.POST['ing'])
            ing = Ingreso.objects.get(pk=self.kwargs['pk'])
            pro = Proveedores.objects.get(pk=int(ings['proveedor']))
            ing.proveedor = pro
            ing.usuario_modificacion = self.request.user
            ing.fecha_ingreso = ings['fecha_ingreso']
            ing.save()

            for i in ing.detingreso_set.all():
                producto = Productos.objects.get(pk=i.producto.pk)
                producto.existencia -= i.cantidad
                producto.save()

            ing.detingreso_set.all().delete()

            for i in ings['productos']:
                producto = Productos.objects.get(pk=int(i['id']))
                det = DetIngreso()
                det.ingreso = ing
                det.producto = producto
                det.cantidad = int(i['cant'])
                producto.existencia += det.cantidad
                det.usuario_creacion = self.request.user
                det.save()
                producto.save()
        return JsonResponse(data, safe=False)


    def get_product_details(self):
        data = []
        try:
            for i in DetIngreso.objects.filter(ingreso=self.kwargs['pk']):
                item = i.producto.toJson()
                item['cant'] = i.cantidad
                data.append(item)
        except expression as identifier:
            pass
        return data

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['det'] = json.dumps(self.get_product_details())
        return context


class IngresoDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para eliminar un ingreso"""
    model = Ingreso
    template_name = 'mov/ingreso_confirm_delete.html'
    success_url = reverse_lazy('ingreso_list')
    success_message = "Ingreso eliminado exitosamente"

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            ing = Ingreso.objects.get(pk=self.kwargs['pk'])
            for i in ing.detingreso_set.all():
                producto = Productos.objects.get(pk=i.producto.pk)
                producto.existencia -= i.cantidad
                producto.save()

            ing.detingreso_set.all().delete()
            ing.delete()
        return redirect('ingreso_list')


class SalidaNew(LoginRequiredMixin, CreateView):
    """Vista para crear nuevas salidas"""
    model = Salida
    form_class = SalidaForm
    template_name = 'mov/salidaForm.html'
    success_url = reverse_lazy('salida_list')
    success_message = "Salida creada exitosamente"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'product': Productos.objects.filter(pk=self.kwargs['pk']).first()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, initial={'pk': self.kwargs['pk']})
        if form.is_valid():
            producto = Productos.objects.get(pk=self.kwargs['pk'])
            cantidad = int(request.POST.get('cantidad'))
            observacion = request.POST.get('observacion')
            usuario_creacion = self.request.user
            Salida.objects.create(producto=producto, cantidad=cantidad, observacion=observacion, usuario_creacion=usuario_creacion)
            producto.existencia -= cantidad
            producto.save()
            messages.success(request, 'Salida creada exitosamente')
            return redirect('salida_list')
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.instance.producto = Productos.objects.get(pk=self.kwargs['pk'])
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

    
class SalidaList(LoginRequiredMixin, ListView):
    """Vista para mostrar todos las salidas"""
    model = Salida
    template_name = 'mov/salidas.html'
    context_object_name = 'salidas'

    def get_queryset(self):
        productos = []
        salidas = []
        for i in Salida.objects.all().order_by('-pk'):
            if i.producto not in productos:
                productos.append(i.producto)
                salidas.append(i)
        return salidas
    

class SalidaDetailView(LoginRequiredMixin, BSModalReadView, BSModalDeleteView):
    """Vista para mostrar el detalle de una salida"""
    model = Productos
    template_name = 'mov/salidaDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalles'] = Salida.objects.filter(producto=self.kwargs['pk']).order_by('-fecha_creacion')
        return context

    def post(self, request, *args, **kwargs):
        lista = list(map(int, request.POST.getlist('item')))
        producto = Productos.objects.get(pk=self.kwargs['pk'])
        with transaction.atomic():
            for i in Salida.objects.filter(pk__in=lista):
                producto.existencia += i.cantidad
            producto.save()
            Salida.objects.filter(pk__in=lista).delete()
        if len(lista) > 1:
            messages.success(request, 'Registros eliminados exitosamente')
        else:
            messages.success(request, 'Registro eliminado exitosamente')
        return redirect('salida_list')


class SalidaEditView(LoginRequiredMixin, BSModalUpdateView):
    model = Salida
    template_name = 'mov/salidaFormEdit.html'
    form_class = SalidaForm
    success_url = 'salida_list'
    success_message = 'Salida actualizada exitosamente'

    def post(self, request, *args, **kwargs):
        salida = Salida.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(request.POST, initial={'pk': salida.producto.id})
        if form.is_valid():
            producto = Productos.objects.get(pk=salida.producto.pk)
            cantidad = int(request.POST.get('cantidad'))
            observacion = request.POST.get('observacion')

            producto.existencia += salida.cantidad
            producto.existencia -= cantidad
            producto.save()

            salida.cantidad = cantidad
            salida.observacion = observacion
            salida.usuario_modificacion = self.request.user
            salida.save()
            messages.success(request, 'Salida actualizada exitosamente')
            return redirect('salida_list')
        return render(request, self.template_name, {'form': form})