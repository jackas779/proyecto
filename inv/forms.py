from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Categorias, Marcas, Proveedores

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