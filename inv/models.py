from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField( auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion


class Marcas(models.Model):
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField( auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion


class Proveedor(models.Model):
    Nombres = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    contacto = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=250, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField( auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombress