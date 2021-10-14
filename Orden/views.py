from django.views.decorators.csrf import csrf_exempt
from .logic.logic_orden import get_specific_orden
from .logic.logic_orden import update_estado_orden
from .logic.logic_orden import create_Orden
from django.http import HttpResponse
from django.core import serializers
import json

@csrf_exempt
def ordenAPI(request,id=0):
    if request.method == 'GET':
        orden = get_specific_orden(id)
        serializeOrden = serializers.serialize('json', [orden])
        return HttpResponse(serializeOrden, content_type='application/json')
    elif request.method == 'POST':
        data = json.loads(request.body)
        orden = [data['fields']['nombre'], data['fields']['articulos'], data['fields']['estado'], data['fields']['valor']]
        create_Orden(orden)
        return HttpResponse("Orden creada en SAP satisfactoriamente")
    elif request.method == 'PUT':
        data = json.loads(request.body)
        id = data['pk']
        estado = data['fields']['estado']
        update = update_estado_orden(id, estado)
        serializeUpdate = serializers.serialize('json', [update])
        return HttpResponse(serializeUpdate, content_type='application/json')

def get_orden_view(id):
    order = get_specific_orden(id)
    return order

def update_orden_view(id, pEstado):
    update = update_estado_orden(id, pEstado)
    serializeUpdateOrden = serializers.serialize('json', [update])
    return HttpResponse(serializeUpdateOrden,content_type='application/json')
