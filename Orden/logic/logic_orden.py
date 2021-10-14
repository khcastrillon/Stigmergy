from ..models import Orden

def get_specific_orden(id):
    orden = Orden.objects.get(pk = id)
    return orden

def update_estado_orden(id, pEstado):
    Orden.objects.filter(pk=id).update(estado=pEstado)
    updateEstadoOrden = get_specific_orden(id)
    return updateEstadoOrden