#Django
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#Django bootstrap model
from bootstrap_modal_forms.generic import BSModalUpdateView

#forms
from .forms import CategoriaForm

#Models
from .models import Categorias


class CategoriaList(LoginRequiredMixin, ListView):
    """Vista para mostrar todas las categorías"""
    model = Categorias
    template_name = 'inv/categorias.html'
    context_object_name = 'categorias'


class CategoriaEdit(LoginRequiredMixin, BSModalUpdateView):
    """Vista para editar categorías"""
    model = Categorias
    template_name = 'inv/categoriaForm.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)


def categoria_inactivar(request, id):
    model = Categorias.objects.get(pk=id)
    
    if request.method == "GET":
        if model.estado is True:
            model.estado = False
        else:
            model.estado = True
        model.save()
    
    return redirect("categoria_list")