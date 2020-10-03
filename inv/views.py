#Django
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#Django bootstrap model
from bootstrap_modal_forms.generic import BSModalUpdateView, BSModalCreateView

#forms
from .forms import CategoriaForm, MarcaForm, ProveedorForm, ProductoForm

#Models
from .models import Categorias, Marcas, Proveedores, Productos


class CategoriaList(LoginRequiredMixin, ListView):
    """Vista para mostrar todas las categorías"""
    model = Categorias
    template_name = 'inv/categorias.html'
    context_object_name = 'categorias'


class CategoriaNew(LoginRequiredMixin, BSModalCreateView):
    """Vista para crear nuevas categorías"""
    model = Categorias
    template_name = 'inv/categoriaForm.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria_list')

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, BSModalUpdateView):
    """Vista para editar categorías"""
    model = Categorias
    template_name = 'inv/categoriaForm.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user
        return super().form_valid(form)

@login_required
def categoria_inactivar(request, id):
    model = Categorias.objects.get(pk=id)
    
    if request.method == "GET":
        if model.estado is True:
            model.estado = False
        else:
            model.estado = True
        model.usuario_modificacion = request.user
        model.save()
    return redirect("categoria_list")


class MarcaList(LoginRequiredMixin, ListView):
    """Vista para mostrar todas las marcas"""
    model = Marcas
    template_name = 'inv/marcas.html'
    context_object_name = 'marcas'


class MarcaNew(LoginRequiredMixin, BSModalCreateView):
    """Vista para crear nuevas marcas"""
    model = Marcas
    template_name = 'inv/marcaForm.html'
    form_class = MarcaForm
    success_url = reverse_lazy('marca_list')

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, BSModalUpdateView):
    """Vista para editar marcas"""
    model = Marcas
    template_name = 'inv/marcaForm.html'
    form_class = MarcaForm
    success_url = reverse_lazy('marca_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user
        return super().form_valid(form)

@login_required
def marca_inactivar(request, id):
    model = Marcas.objects.get(pk=id)
    
    if request.method == "GET":
        if model.estado is True:
            model.estado = False
        else:
            model.estado = True
        model.usuario_modificacion = request.user
        model.save()
    return redirect("marca_list")


class ProveedorList(LoginRequiredMixin, ListView):
    """Vista para mostrar todas los proveedores"""
    model = Proveedores
    template_name = 'inv/proveedorList.html'
    context_object_name = 'proveedores'


class ProveedorNew(LoginRequiredMixin, BSModalCreateView):
    """Vista para crear nuevos proveedores"""
    model = Proveedores
    template_name = 'inv/proveedorForm.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_list')

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class ProveedorEdit(LoginRequiredMixin, BSModalUpdateView):
    """Vista para editar proveedor"""
    model = Proveedores
    template_name = 'inv/proveedorForm.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user
        return super().form_valid(form)

@login_required
def proveedor_inactivar(request, id):
    model = Proveedores.objects.get(pk=id)
    
    if request.method == "GET":
        if model.estado is True:
            model.estado = False
        else:
            model.estado = True
        model.usuario_modificacion = request.user
        model.save()
    return redirect("proveedor_list")


class ProductoList(LoginRequiredMixin, ListView):
    """Vista para mostrar todos los productos"""
    model = Productos
    template_name = 'inv/productos.html'
    context_object_name = 'productos'


class ProductoNew(LoginRequiredMixin, BSModalCreateView):
    """Vista para crear nuevos productos"""
    model = Productos
    template_name = 'inv/productoForm.html'
    form_class = ProductoForm
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class ProductoEdit(LoginRequiredMixin, BSModalUpdateView):
    """Vista para editar proveedor"""
    model = Productos
    template_name = 'inv/productoForm.html'
    form_class = ProductoForm
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user
        return super().form_valid(form)

@login_required
def producto_inactivar(request, id):
    model = Productos.objects.get(pk=id)
    
    if request.method == "GET":
        if model.estado is True:
            model.estado = False
        else:
            model.estado = True
        model.usuario_modificacion = request.user
        model.save()
    return redirect("producto_list")