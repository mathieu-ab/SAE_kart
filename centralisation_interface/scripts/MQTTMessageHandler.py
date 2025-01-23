from config import *

class MQTTMessageHandler():
    def __init__(self, topics, interface):
        self.topics = topics  # Liste des topics à surveiller
        self.client = mqtt.Client()
        self.interface = interface
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("localhost", keepalive=60)
        self.client.loop_start()

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
        elif msg.topic == "moteur/temperature":
            self.interface.update_temperature_moteur(msg_received)
        elif msg.topic == "bms/temperature":
            self.interface.update_temperature_batterie(msg_received)
        elif msg.topic == "bms/batterie":
            self.interface.update_batterie(msg_received)
        elif msg.topic == "charge/status":
            self.interface.update_charge_control(msg_received)
        elif msg.topic == "message/prevention":
            self.interface.update_message_prevention(msg_received)
        elif msg.topic == "aide/ligne_blanche/control":
            self.interface.update_ligne_blanche(msg_received)
        elif msg.topic == "aide/endormissement/control":
            self.interface.update_endormissement(msg_received)
        elif msg.topic == "aide/obstacle/control":
            self.interface.update_obstacle(msg_received)
        elif msg.topic == "bouton/page":
            self.interface.update_bouton_page(msg_received)
        elif msg.topic == "bouton/clignotant" : 
            self.interface.update_button_clignotant(msg_received)

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


    def analyse_topic_message_prevention(self, message):
        global prevention_queue
        message_parts = message.split("|")
        if len(message_parts) != 2:
            print(f"Longueur du message de prévention incorrecte ! Message : {message}")
            return

        message_text = message_parts[0]
        try:
            choix = None if message_parts[1] == "None" else int(message_parts[1])
        except ValueError:
            print(f"Problème avec la fin du message : {message_parts[1]}")
            return

        prevention_queue.append({"message": message_text, "start": int(time()), "end": choix})
