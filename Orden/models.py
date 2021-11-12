# Create your models here.
from django.db import models
from django.utils.crypto import get_random_string
class Orden(models.Model):
    nombre = models.CharField(max_length=60)
    articulos = models.CharField(max_length=1000)
    estado = models.CharField(max_length=1000)
    valor = models.IntegerField()
    dateTime = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=60,default="")
    #//Usuario por definir
    def __str__(self):
        return '{}'.format(self.nombre, self.articulos, self.estado, self.valor, self.dateTime, self.token)