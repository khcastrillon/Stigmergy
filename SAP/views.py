import json
from .logic import logic_SAP
from django.views.decorators.csrf import csrf_exempt
from Orden.views import update_orden_view, get_orden_view
from django.http import HttpResponse
from django.core import serializers
import time

estadosPosibles = ('En HUB de despacho', 'Dron asignado', 'Dron despachado', 'Volando posición X1,Y1', 'Volando posición X2, Y2', 'Aterrizando en HUB de llegada', 'En HUB de llegada')

@csrf_exempt
def SAPApi(request,id=0):
    if request.method == 'GET':
        ordenSAP = logic_SAP.get_orden_SAP(id)
        serializeOrdenSAP = serializers.serialize('json', [ordenSAP])
        return HttpResponse(serializeOrdenSAP, content_type='application/json')
    elif request.method == 'POST':
        data = json.loads(request.body)
        ordenSAP = [get_orden_view(data['pk']),data['fields']['estado']]
        logic_SAP.create_Orden_SAP(ordenSAP)
        return HttpResponse("Orden creada en SAP satisfactoriamente")
    elif request.method == 'PUT':
        data = json.loads(request.body)
        id = data['pk']
        estado = data['fields']['estado']

        #Simulación  SAP, cuando haya UI se habilita
        # for i in estadosPosibles:
        #     update_orden_SAP_view(id, i)
        #     time.sleep(1)
        # update = logic_SAP.update_estado_orden_SAP(id, 'Lista para recoger')
        # update_orden_view(id, 'Lista para recoger')

        update = logic_SAP.update_estado_orden_SAP(id, estado)
        update_orden_view(id, estado)
        serializeUpdateSAP = serializers.serialize('json', [update])
        return HttpResponse(serializeUpdateSAP, content_type='application/json')

def update_orden_SAP_view(id, pEstado):
    update = logic_SAP.update_estado_orden_SAP(id, pEstado)
    time.sleep(1)
    update_orden_view(id, pEstado)
    serializeUpdateSAP = serializers.serialize('json', [update])
    return HttpResponse(serializeUpdateSAP,content_type='application/json')



