from django.urls import path 
from .views import CategoriaList, CategoriaEdit

urlpatterns = [
    path('categoria/', CategoriaList.as_view(), name="categoria_list"),
    path('categoria/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
]