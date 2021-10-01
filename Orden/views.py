from .logic.logic_orden import get_specific_orden
from django.http import HttpResponse
from django.core import serializers
from .models import Orden
import json
from django.shortcuts import get_object_or_404

def get_orden(request, id):
    order = get_specific_orden(id=id)
    return HttpResponse(order, content_type='application/json')

def prueba(request,id):
    if request.method == 'PUT':
        order = get_object_or_404(Orden,pk=id)
        print(order.estado)
        estado_body = json.loads(request.body)
        order.estado = estado_body['estado']
        order.save()

        return HttpResponse(order.estado, content_type='application/json')