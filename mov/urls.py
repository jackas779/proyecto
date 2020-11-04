from django.urls import path
from .views import IngresoNew, autocomplete, IngresoList, IngresoDetailView, IngresoEditView, IngresoDeleteView

urlpatterns = [
    #Entradas
    path('ingresos/new', IngresoNew.as_view(), name='ingreso_new'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('ingresos/', IngresoList.as_view(), name='ingreso_list'),
    path('ingresos/read/<int:pk>', IngresoDetailView.as_view(), name='ingreso_detail'),
    path('ingresos/edit/<int:pk>', IngresoEditView.as_view(), name='ingreso_edit'),
    path('ingresos/delete/<int:pk>', IngresoDeleteView.as_view(), name='ingreso_delete'),
]

