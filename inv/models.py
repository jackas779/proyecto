from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.forms.models import model_to_dict

class Categorias(models.Model):
    descripcion = models.CharField(max_length=100, null=False, blank=False, unique=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField( auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion

    def toJson(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'

class Marcas(models.Model):
    descripcion = models.CharField(max_length=100, null=False, blank=False, unique=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField( auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion

    def toJson(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class Proveedores(models.Model):
    nombres = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    contacto = models.PositiveIntegerField(validators=[MinValueValidator(1)], null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    telefono = models.PositiveIntegerField(validators=[MinValueValidator(1)], null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField( auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

class Productos(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    codigo_barra = models.PositiveIntegerField(validators=[MinValueValidator(1)], null=False, blank=False)
    descripcion = models.CharField(max_length=200, unique=True)
    existencia = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', editable=False,on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT, related_name='%(class)s_categoria')
    marca = models.ForeignKey(Marcas, on_delete=models.PROTECT)

    def __str__(self):
        return self.descripcion

    
    def toJson(self):
        item = model_to_dict(self)
        item['categoria'] = self.categoria.toJson()
        item['marca'] = self.marca.toJson()
        return item

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        unique_together = ('codigo', 'codigo_barra')

