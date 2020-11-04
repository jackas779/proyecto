#Django
from django import forms
from datetime import datetime

#Models
from .models import *

#Plugins
from tempus_dominus.widgets import DatePicker


class IngresoForm(forms.ModelForm):
    fecha_ingreso = forms.DateField(
        required=True,
        widget=DatePicker(
            options={
            'minDate': datetime.now().strftime("%Y-%m-%d")
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

    
    def clean(self):
        date = self.fecha_ingreso
        now = datetime.now()
        if date < now:
            raise forms.ValidationError("La fecha debe ser mayor o igual a la actual")
        return super(IngresoForm, self).clean()