from ..models import Orden
from django.utils.crypto import get_random_string

def get_specific_orden(id):
    orden = Orden.objects.get(pk = id)
    return orden

def create_Orden(orden):
    p = Orden.objects.create(nombre=orden[0], articulos=orden[1], estado=orden[2], valor=orden[3], token = get_random_string(length=50))
    return p

def update_estado_orden(id, pEstado):
    Orden.objects.filter(pk=id).update(estado=pEstado)
    updateEstadoOrden = get_specific_orden(id)
    return updateEstadoOrden