from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Categorias, Marcas

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