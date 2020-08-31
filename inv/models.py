from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField( auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.descripcion