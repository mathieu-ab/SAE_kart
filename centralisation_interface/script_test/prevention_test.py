from random import choice, randint
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
        self.client.publish(topic, message, retain=False)
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
    time.sleep(1)
    
    publisher.publish_message("message/prevention", f"{randint(0, 100)} Vous drevez faire une|11")
    time.sleep(1)
    publisher.publish_message("message/prevention", f"{randint(0, 100)} Vous drevez faire une|11")
    time.sleep(1)
    publisher.publish_message("message/prevention", f"{randint(0, 100)} Somnolence détectée, prenez |None|True")
        

        # time.sleep(0.5)  # Pause entre les envois
    publisher.client.loop_stop()
    publisher.client.disconnect()
if __name__ == "__main__":
    main()
