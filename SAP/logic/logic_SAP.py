from ..models import SAP

def get_orden_SAP(id):
    ordenSAP = SAP.objects.get(pk=id)
    return ordenSAP

def update_estado_orden_SAP(id, pEstado):
    SAP.objects.filter(pk=id).update(estado=pEstado)
    updateEstadoOrdenSAP = get_orden_SAP(id)
    return updateEstadoOrdenSAP

def create_Orden_SAP(ordenSAP):
    p = SAP.objects.create(orden=ordenSAP[0], estado=ordenSAP[1])
    return p
