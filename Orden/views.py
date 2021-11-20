from django.views.decorators.csrf import csrf_exempt
from .logic.logic_orden import get_specific_orden
from .logic.logic_orden import update_estado_orden
from .logic.logic_orden import create_Orden
from django.http import HttpResponse
from django.core import serializers
import rsa
import json
import random
from paho.mqtt import client as mqtt_client


publicKey, privateKey = rsa.newkeys(512)
topicOrden, topicSAP = "Orden", "SAP"

broker = 'broker.emqx.io'
port = 1883
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'SAP'
password = 'public'
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.connect(broker, port)

# Se suscribe a ordenes
def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

client.subscribe(topicSAP)
client.on_message = on_message

# Publica las actualizaciones de SAP
def publish(client, msg):
    result = client.publish(topicOrden, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topicOrden}`")
    else:
        print(f"Failed to send message to topic {topicSAP}")

publicKey, privateKey = rsa.newkeys(512)
topicOrden, topicSAP = "Orden", "SAP"

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
        mqtt.publish()
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
