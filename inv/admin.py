from django.contrib import admin
from .models import Categorias, Marcas, Proveedores, Productos

admin.site.register(Categorias)
admin.site.register(Marcas)
admin.site.register(Proveedores)
admin.site.register(Productos)