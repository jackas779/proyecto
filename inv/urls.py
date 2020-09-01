from django.urls import path 
from .views import CategoriaList, CategoriaEdit, categoria_inactivar

urlpatterns = [
    path('categorias/', CategoriaList.as_view(), name="categoria_list"),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/inactivar/<int:id>', categoria_inactivar, name='categoria_inactivar'),
]