#Django
from django import forms
from datetime import datetime

#Models
from .models import *
from inv.models import Productos

#Plugins
from tempus_dominus.widgets import DatePicker
from bootstrap_modal_forms.forms import BSModalModelForm


class IngresoForm(forms.ModelForm):
    fecha_ingreso = forms.DateField(
        required=True,
        widget=DatePicker(
             attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            },
        ),
        initial = datetime.now().strftime("%Y-%m-%d")
    )
    class Meta:
        model = Ingreso
        fields = ['proveedor', 'fecha_ingreso']

    def __init__(self, *args, **kwargs):
        super(IngresoForm, self).__init__(*args, **kwargs)
        self.fields['proveedor'].empty_label = 'Seleccione un proveedor'
        self.fields['fecha_ingreso'].widget.attrs['autocomplete'] = 'off'


class SalidaForm(BSModalModelForm):
    class Meta:
        model = Salida
        fields = ['cantidad', 'observacion']

    def clean(self, *args, **kwargs):
        cleaned_data = super(SalidaForm, self).clean(*args, **kwargs)
        existencia = int(Productos.objects.get(pk=self.initial['pk']).existencia)
        cantidad = int(cleaned_data.get('cantidad'))
        if not Salida.objects.filter(producto=self.initial['pk']):
            if cantidad > existencia:
                self.add_error('cantidad', 'La cantidad ingresada supera la existencia del producto')
        else:
            cant = 0
            for i in Salida.objects.filter(producto=self.initial['pk']):
                cant += i.cantidad
            if cantidad > int(existencia+cant):
                self.add_error('cantidad', 'La cantidad ingresada supera la existencia del producto')

    def __init__(self, *args, **kwargs):
        super(SalidaForm, self).__init__(*args, **kwargs)
        self.fields['cantidad'].widget.attrs['min'] = '1'