from django.urls import path 
from .views import CategoriaList, CategoriaEdit

urlpatterns = [
    path('categorias/', CategoriaList.as_view(), name="categoria_list"),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
]