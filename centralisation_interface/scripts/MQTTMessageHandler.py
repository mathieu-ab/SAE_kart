from config import *
from callbacks import *

class MQTTMessageHandler():
    def __init__(self, topics, interface):
        self.topics = topics  # Liste des topics à surveiller
        self.client = mqtt.Client()
        self.interface = interface
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("localhost", keepalive=60)
        self.client.loop_start()

    #callback pour indiquer la connection au broker et à quel topic l'abonnement est fait
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"connecté au broker MQTT avec succès.")
            for topic in self.topics:
                client.subscribe(topic)
                print(f"Handler abonné au topic : {topic}")
        else:
            print(f"échec de la connexion, code de retour : {rc}")

    #callback pour chaque message reçu auquel on est abonné
    def on_message(self, client, userdata, msg):
        msg_received = msg.payload.decode('utf-8')
        print(f"- Message reçu sur le topic {msg.topic}: {msg_received}")
        #redirection des action de chaque topic dans le fichier mqtt_callback dans le dossier callbacks
        if msg.topic == "moteur/vitesse":
            update_vitesse(self.interface, msg_received)
        elif msg.topic == "moteur/temperature":
            update_temperature_moteur(self.interface, msg_received)
        elif msg.topic == "bms/temperature":
            update_temperature_batterie(self.interface, msg_received)
        elif msg.topic == "bms/batterie":
            update_batterie(self.interface, msg_received)
        elif msg.topic == "charge/control":
            update_charge_control(self.interface, msg_received)
        elif msg.topic == "message/prevention":
            update_message_prevention(self.interface, msg_received)
        elif msg.topic == "aide/ligne_blanche/control":
            update_ligne_blanche(self.interface, msg_received)
        elif msg.topic == "aide/endormissement/control":
            update_endormissement(self.interface, msg_received)
        elif msg.topic == "aide/obstacle/control":
            update_obstacle(self.interface, msg_received)
        elif msg.topic == "bouton/page":
            update_bouton_page(self.interface, msg_received)
        elif msg.topic == "bouton/clignotant" : 
            update_button_clignotant(self.interface, msg_received)
        elif msg.topic == "moteur/mode/control" :
            update_mode_conduite(self.interface, msg_received)
        elif msg.topic == "aide/vitesse_consigne/control" :
            update_vitesse_consigne(self.interface, msg_received)

    #méthode pour publier un message avec un topic
    def publish_message(self, topic, message):
        try:
            if topic in topics_non_retain :
                rt = False
            else :
                rt = True
            self.client.publish(topic, message, retain=rt)
            print(f"Message '{message}' envoyé sur le topic '{topic}' avec retain {rt}")
        except Exception as e:
            print(f"Erreur lors de l'envoi : {e}")



