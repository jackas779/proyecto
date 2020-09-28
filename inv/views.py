#Django
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#Django bootstrap model
from bootstrap_modal_forms.generic import BSModalUpdateView, BSModalCreateView

#forms
from .forms import CategoriaForm, MarcaForm

#Models
from .models import Categorias, Marcas


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