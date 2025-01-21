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
            self.analyse_topic_moteur_vitesse(msg_received)
        elif msg.topic == "moteur/temperature":
            self.analyse_topic_moteur_temperature(msg_received)
        elif msg.topic == "bms/temperature":
            self.analyse_topic_bms_temperature(msg_received)
        elif msg.topic == "bms/batterie":
            self.analyse_topic_bms_batterie(msg_received)
        elif msg.topic == "message/prevention":
            self.analyse_topic_message_prevention(msg_received)



    def publish_message(self, topic, message):
        try:
            self.client.publish(topic, message, retain=True)
            print(f"Message '{message}' envoyé sur le topic '{topic}'")
        except Exception as e:
            print(f"Erreur lors de l'envoi : {e}")

    def analyse_topic_moteur_vitesse(self, message):
        try:
            vitesse = int(message)
            self.interface.update_vitesse(vitesse)
        except Exception as e:
            print(e)

    def analyse_topic_moteur_temperature(self, message):
        try:
            temperature_moteur = int(message)
            self.interface.update_temperature_moteur(temperature_moteur)
        except Exception as e:
            print(e)

    def analyse_topic_bms_temperature(self, message):
        try:
            temperature_batterie = int(message)
            self.interface.update_temperature_batterie(temperature_batterie)
        except Exception as e:
            print(e)

    def analyse_topic_bms_batterie(self, message):
        try:
            batterie = round(int(message) / 100, 2)
            self.interface.update_batterie(batterie)
        except Exception as e:
            print(e)


    def analyse_topic_message_prevention(self, message):
        global prevention_queue, affichage_loop, navigation_loop, systeme_loop
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
        affichage_loop = True
        navigation_loop = False
        systeme_loop = False
