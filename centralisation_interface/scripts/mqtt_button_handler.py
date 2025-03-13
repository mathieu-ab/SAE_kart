import paho.mqtt.client as mqtt

BROKER = "192.168.1.205"
TOPIC_SUB = "charge/button/set"
TOPIC_PUB = "charge/button/state"

def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC_SUB)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    client.publish(TOPIC_PUB, message, retain=True)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_forever()
