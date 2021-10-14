from ..models import Orden

def get_specific_orden(id):
    orden = Orden.objects.get(pk = id)
    return orden

def create_Orden(orden):
    p = Orden.objects.create(nombre=orden[0], articulos=orden[1], estado=orden[2], valor=orden[4])
    return p

def update_estado_orden(id, pEstado):
    Orden.objects.filter(pk=id).update(estado=pEstado)
    updateEstadoOrden = get_specific_orden(id)
    return updateEstadoOrden