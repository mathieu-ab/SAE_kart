import serial
from random import choice, randint
import paho.mqtt.client as mqtt
import time
import threading








class MQTTMessageHandler(threading.Thread):
    def __init__(self, topics):
        threading.Thread.__init__(self)
        self.topics = topics  # Liste des topics à surveiller
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"connecté au broker MQTT avec succès.")
            for topic in self.topics:
                client.subscribe(topic)
                print(f"Handler abonné au topic : {topic}")
        else:
            print(f"échec de la connexion, code de retour : {rc}")

    def on_message(self, client, userdata, msg):
        msg_received = msg.payload.decode('utf-8')
        print(f"- Message reçu sur le topic {msg.topic}: {msg_received}")
        if msg.topic == "moteur/vitesse":
            self.interface.update_vitesse(msg_received)



    def publish_message(self, topic, message):
        try:
            self.client.publish(topic, message)
            print(f"Message '{message}' envoyé sur le topic '{topic}'")
        except Exception as e:
            print(f"Erreur lors de l'envoi : {e}")
    def run(self) :
        self.client.connect("localhost", keepalive=60)
        self.client.loop_start()







# Exemple d'utilisation
def main():
    topics = [
        "moteur/vitesse",
        "moteur/temperature",
        "moteur/mode",
        "aide/vitesse_consigne",
        "aide/reg_lim",
    ]
    broker_address = "localhost"  # Adresse du broker MQTT
    publisher = MQTTMessageHandler(broker_address)

    publisher.start()

    # Envoi de messages périodiques sur différents topics

    # Paramètres de la connexion série (utilise /dev/serial0 pour la connexion série sur GPIO)
    ser = serial.Serial('/dev/serial0', 9600, timeout=1)  # Baudrate 9600 et timeout de 1 seconde
    time.sleep(2)  # Attendre 2 secondes pour établir la connexion

    def envoyer_commande(vitesse, mode):
        """
        Envoie la vitesse de consigne et le mode de conduite à l'ATmega328P.
        :param vitesse: La vitesse de consigne à envoyer (en km/h).
        :param mode: Le mode de conduite (char: 'N' pour normal, 'E' pour éco, 'T' pour turbo).
        """
        message = f"{vitesse},{mode}\n"
        ser.write(message.encode())  # Envoie de la commande série
        print(f"Commandé: {vitesse} km/h, Mode: {mode}")

    def lire_donnees():
        """Lire les données reçues (vitesse et température) de l'ATmega328P."""
        try:
            while True:
                if ser.in_waiting > 0:  # Si des données sont disponibles
                    data = ser.readline().decode('utf-8').strip()  # Lire une ligne et la décoder
                    print(f"Données reçues: {data}")
                    traiter_donnees(data)
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("Programme interrompu.")
        finally:
            ser.close()  # Fermer la connexion série

    def traiter_donnees(data):
        """Traiter les données reçues (vitesse et température) sous forme 'vitesse: xx.xx, temp: yy.yy'."""
        try:
            if "vitesse" in data and "temp" in data:
                parts = data.split(',')
                vitesse = float(parts[0].split(':')[1].strip())
                temperature = float(parts[1].split(':')[1].strip())
                publisher.publish_message("moteur/vitesse", vitesse)
                publisher.publish_message("moteur/temperature", temperature)
                print(f"Vitesse actuelle: {vitesse} km/h, Température moteur: {temperature} °C")
        except Exception as e:
            print(f"Erreur dans le traitement des données : {e}")

    # Exemple de commande
    vitesse_consigne = 30  # Vitesse de consigne (par exemple, 30 km/h)
    mode_conduite = 'N'  # Mode 'N' pour normal

    # Envoie de la commande à l'ATmega328P
    envoyer_commande(vitesse_consigne, mode_conduite)

    # Lire les données envoyées par l'ATmega328P
    lire_donnees()

if __name__ == "__main__":
    main()