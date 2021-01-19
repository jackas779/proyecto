from django.urls import path
from .views import *

urlpatterns = [
    #Entradas
    path('ingresos/new', IngresoNew.as_view(), name='ingreso_new'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('ingresos/', IngresoList.as_view(), name='ingreso_list'),
    path('ingresos/read/<int:pk>', IngresoDetailView.as_view(), name='ingreso_detail'),
    path('ingresos/edit/<int:pk>', IngresoEditView.as_view(), name='ingreso_edit'),
    path('ingresos/delete/<int:pk>', IngresoDeleteView.as_view(), name='ingreso_delete'),
    #Salidas
    path('salidas/new/<int:pk>', SalidaNew.as_view(), name='salida_new'),
    path('salidas/', SalidaList.as_view(), name='salida_list'),
    path('salidas/read/<int:pk>', SalidaDetailView.as_view(), name='salida_detail'),
    path('salidas/edit/<int:pk>', SalidaEditView.as_view(), name='salida_edit'),
]

