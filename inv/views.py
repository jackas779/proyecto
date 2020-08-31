#Django
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

#Django bootstrap model
from bootstrap_modal_forms.generic import BSModalUpdateView

#forms
from .forms import CategoriaForm

#Models
from .models import Categorias


class CategoriaList(ListView):
    """Vista para mostrar todas las categorías"""
    model = Categorias
    template_name = 'inv/categorias.html'
    context_object_name = 'categorias'


class CategoriaEdit(BSModalUpdateView):
    """Vista para editar categorías"""
    model = Categorias
    template_name = 'inv/categoriaForm.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria_list')