from .logic.logic_orden import get_specific_orden
from django.http import HttpResponse
from django.core import serializers

def get_orden(request, id):
    order = get_specific_orden(id=id)
    return HttpResponse(order, content_type='application/json')
