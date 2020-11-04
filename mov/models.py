#Django
from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime

#Models
from inv.models import *


class Ingreso(models.Model):
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(default=datetime.now)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {} {}'.format(self.pk, self.fecha_ingreso, self.proveedor.nombres)

    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'


class DetIngreso(models.Model):
    ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modificado_por', verbose_name='modificado por', on_delete=models.CASCADE)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.ingreso, self.producto.descripcion)

    class Meta:
        verbose_name = 'Detalle Ingreso'
        verbose_name_plural = 'Detalles Ingresos'  
