from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Categorias(models.Model):
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField( auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Categorias'

class Marcas(models.Model):
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField( auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Marcas'

class Proveedores(models.Model):
    nombres = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    contacto = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    telefono = models.CharField(max_length=10, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField( auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name_plural = 'Proveedores'

class Productos(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    codigo_barra = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=200, unique=True)
    existencia = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', editable=False,on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT, related_name='%(class)s_categoria')
    marca = models.ForeignKey(Marcas, on_delete=models.PROTECT)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Productos'
        unique_together = ('codigo', 'codigo_barra')

    