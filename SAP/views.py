import json
from .logic import logic_SAP
from django.views.decorators.csrf import csrf_exempt
from Orden.views import update_orden_view, get_orden_view
import random
from paho.mqtt import client as mqtt_client
from django.http import HttpResponse
from django.core import serializers
import time
import rsa

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

client.subscribe(topicOrden)
client.on_message = on_message

# Publica las actualizaciones de SAP
def publish(client, msg):
    result = client.publish(topicSAP, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topicSAP}`")
    else:
        print(f"Failed to send message to topic {topicSAP}")

estadosPosibles = ('En HUB de despacho', 'Dron asignado', 'Dron despachado', 'Volando posición X1,Y1', 'Volando posición X2, Y2', 'Aterrizando en HUB de llegada', 'En HUB de llegada')

@csrf_exempt
def SAPApi(request,id=0):
    if request.method == 'GET':
        ordenSAP = logic_SAP.get_orden_SAP(id)
        serializeOrdenSAP = serializers.serialize('json', [ordenSAP])
        return HttpResponse(serializeOrdenSAP, content_type='application/json')

    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            serializeOrden = serializers.serialize('json', [get_orden_view(data['pk']),])
            data1 = json.loads(serializeOrden)[0]
            if data1['fields']['token'] == data['fields']['token']:
                ordenSAP = [get_orden_view(data['pk']), data['fields']['estado']]
                logic_SAP.create_Orden_SAP(ordenSAP)
                return HttpResponse("Orden creada en SAP satisfactoriamente")
            else:
                return HttpResponse("Error token: la orden no ha sido creada en SAP "+"Real: "+data1['fields']['token']+" Falso: "+data['fields']['token'])
        except Exception as e:
            return HttpResponse("Error: la orden no ha sido creada en SAP")

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



