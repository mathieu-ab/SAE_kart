import paho.mqtt.client as mqtt

class MQTTSubscriber:
    def __init__(self, broker_address, topics):
        self.broker_address = broker_address
        self.topics = topics
        self.client = mqtt.Client()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connecté au broker MQTT avec succès.")
            for topic in self.topics:
                client.subscribe(topic)
                print(f"Abonné au topic : {topic}")
        else:
            print(f"Échec de la connexion, code de retour : {rc}")

    def on_message(self, client, userdata, msg):
        print(f"Reçu sur {msg.topic}: {msg.payload.decode('utf-8')}")

    def start(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker_address, 1883, keepalive=60)
        self.client.loop_forever()

# Exemple d'utilisation
def main():
    broker_address = "localhost"  # Adresse du broker MQTT
    topics = [
        "moteur/vitesse",
        "moteur/temperature",
        "moteur/mode",

        "bms/batterie",

        "message/prevention",

        "aide/clignotant",
        "aide/reg_lim",
        "aide/vitesse_consigne",
        "aide/ligne_blanche",
        "aide/endormissement",
        "aide/obstacle"
    ]

    subscriber = MQTTSubscriber(broker_address, topics)
    subscriber.start()

if __name__ == "__main__":
    main()
