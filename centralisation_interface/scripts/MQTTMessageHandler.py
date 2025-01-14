from scripts.import_variable import *


class MQTTMessageHandler(threading.Thread):
    def __init__(self, topics, interface):
        threading.Thread.__init__(self)
        self.topics = topics  # Liste des topics à surveiller
        self.client = mqtt.Client()
        self.interface = interface
        self.lock = threading.Lock()  # Verrou pour synchroniser l'accès à la liste des messages à envoyer
        self.condition = threading.Condition()  # Condition pour gérer la mise en stase

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
        elif msg.topic == "bms/batterie":
            self.analyse_topic_bms_batterie(msg_received)
        elif msg.topic == "message/prevention":
            self.analyse_topic_message_prevention(msg_received)

    def run(self):
        print(f"démarrage...")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("localhost", keepalive=60)

        self.client.loop_start()

        while True:
            with self.condition:
                while not self.envoi_mqtt_msg:
                    self.condition.wait()

                with self.lock:
                    message_to_send = self.envoi_mqtt_msg.pop(0)

            if message_to_send:
                topic, message = message_to_send

                print(f"Envoi : {message} au topic {topic}")
                try:
                    self.client.publish(topic, message)
                except Exception as e:
                    print(f"Erreur lors de l'envoi : {e}")

    def add_message(self, topic, message):
        with self.lock:
            self.envoi_mqtt_msg.append((topic, message))
        with self.condition:
            self.condition.notify()

    def analyse_topic_moteur_vitesse(self, message):
        try:
            vitesse = int(message)
            self.interface.vitesse = vitesse
        except Exception as e:
            print(e)

    def analyse_topic_moteur_temperature(self, message):
        try:
            temperature = int(message)
            self.interface.temperature = temperature
        except Exception as e:
            print(e)

    def analyse_topic_bms_batterie(self, message):
        try:
            batterie = int(message)
            batterie = batterie
            self.interface.batterie = batterie
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
