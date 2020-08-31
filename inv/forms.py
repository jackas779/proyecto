from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Categorias

class CategoriaForm(BSModalModelForm):
    class Meta:
        model = Categorias
        fields = ['descripcion']