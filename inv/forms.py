from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Categorias, Marcas, Proveedores, Productos
from django import forms

class CategoriaForm(BSModalModelForm):
    class Meta:
        model = Categorias
        fields = ['descripcion']
        labels = {
            'descripcion': 'Nombre'
        }


class MarcaForm(BSModalModelForm):
    class Meta:
        model = Marcas
        fields = ['descripcion']
        labels = {
            'descripcion': 'Nombre'
        }


class ProveedorForm(BSModalModelForm):
    class Meta:
        model = Proveedores
        fields = ['nombres', 'direccion', 'contacto', 'email', 'telefono']


class ProductoForm(BSModalModelForm):
    class Meta:
        model = Productos
        fields = ['codigo', 'codigo_barra', 'descripcion', 'categoria', 'marca', 'image']
        labels = {
            'image': 'Imagen'
        }

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = 'Seleccione una categoría'
        self.fields['marca'].empty_label = 'Seleccione una marca'