from django.urls import path 
from . import views

urlpatterns = [
    #Categorías
    path('categorias/', views.CategoriaList.as_view(), name="categoria_list"),
    path('categorias/new', views.CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', views.CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/inactivar/<int:id>', views.categoria_inactivar, name='categoria_inactivar'),
    #Marcas
    path('marcas/', views.MarcaList.as_view(), name="marca_list"),
    path('marcas/new', views.MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>', views.MarcaEdit.as_view(), name='marca_edit'),
    path('marcas/inactivar/<int:id>', views.marca_inactivar, name='marca_inactivar'),
    #Proveedores
    path('proveedores/', views.ProveedorList.as_view(), name="proveedor_list"),
    path('proveedores/new', views.ProveedorNew.as_view(), name="proveedor_new"),
    path('proveedores/edit/<int:pk>', views.ProveedorEdit.as_view(), name="proveedor_edit"),
    path('proveedores/inactivar/<int:id>', views.proveedor_inactivar, name="proveedor_inactivar"),
]