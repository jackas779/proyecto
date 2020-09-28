from django.urls import path 
from . import views

urlpatterns = [
    #Categorías
    path('categoria/', views.CategoriaList.as_view(), name="categoria_list"),
    path('categoria/new', views.CategoriaNew.as_view(), name='categoria_new'),
    path('categoria/edit/<int:pk>', views.CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria/inactivar/<int:id>', views.categoria_inactivar, name='categoria_inactivar'),
    #Marcas
    path('marca/', views.MarcaList.as_view(), name="marca_list"),
    path('marca/new', views.MarcaNew.as_view(), name='marca_new'),
]