from .logic.logic_orden import get_specific_orden
from .logic.logic_orden import update_estado_orden
from django.http import HttpResponse
from django.core import serializers
from .models import Orden
import json
from django.shortcuts import get_object_or_404

def get_orden(request, id):
    order = get_specific_orden(id=id)
    serializeOrden = serializers.serialize('json', [order])
    return HttpResponse(serializeOrden, content_type='application/json')

def update_orden_view(id, pEstado):
    update = update_estado_orden(id, pEstado)
    serializeUpdateOrden = serializers.serialize('json', [update])
    return HttpResponse(serializeUpdateOrden,content_type='application/json')

def prueba(request,id):
    if request.method == 'PUT':
        order = get_object_or_404(Orden,pk=id)
        print(order.estado)
        estado_body = json.loads(request.body)
        order.estado = estado_body['estado']
        order.save()
        return HttpResponse(order.estado, content_type='application/json')