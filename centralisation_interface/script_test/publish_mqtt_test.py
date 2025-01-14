from random import randint
import paho.mqtt.client as mqtt
import time

class MQTTPublisher:
    def __init__(self, broker_address):
        self.broker_address = broker_address
        self.client = mqtt.Client()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connecté au broker MQTT avec succès.")
        else:
            print(f"Échec de la connexion, code de retour : {rc}")

    def publish_message(self, topic, message):
        self.client.publish(topic, message)
        print(f"Message envoyé sur {topic}: {message}")

    def start(self):
        self.client.on_connect = self.on_connect
        self.client.connect(self.broker_address, 1883, keepalive=60)
        self.client.loop_start()

# Exemple d'utilisation
def main():
    broker_address = "localhost"  # Adresse du broker MQTT
    publisher = MQTTPublisher(broker_address)

    publisher.start()

    # Envoi de messages périodiques sur différents topics
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
    for i in range(5):
        message = f"{randint(10, 100)}"
        publisher.publish_message("moteur/vitesse", message)
        publisher.publish_message("moteur/temperature", message)
        publisher.publish_message("bms/batterie", message)
        time.sleep(1)  # Pause entre les envois

if __name__ == "__main__":
    main()
