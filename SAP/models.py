from django.db import models
from Orden.models import Orden

# Create your models here.

class SAP(models.Model):
    orden = models.OneToOneField(Orden, on_delete=models.CASCADE, primary_key=True)
    estado = models.CharField(max_length=1000)
    #//Usuario por definir
    def __str__(self):
        return '%s %s' % (self.orden.nombre, self.estado)