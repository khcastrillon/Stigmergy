from django.db import models
from Orden.models import comentario

# Create your models here.

class SAP(models.Model):
    comentario = models.CharField(max_length=1000)
   
    def __str__(self):
        return '%s %s' % (self.comentario)
