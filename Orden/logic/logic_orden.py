from ..models import Orden

def get_specific_orden(id):
    orden = Orden.objects.get(pk = id)
    return orden.estado


