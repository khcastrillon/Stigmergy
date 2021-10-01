from django.db import models

# Create your models here.
from django.db import models



class Orden(models.Model):
    nombre = models.CharField(max_length=60)
    articulos = models.CharField(max_length=1000)
    estado = models.CharField(max_length=1000)
    fecha = models.DateField
    #//Usuario por definir
    valor = models.IntegerField
    def __str__(self):
        return '{}'.format(self.nombre, self.fecha, self.estado)