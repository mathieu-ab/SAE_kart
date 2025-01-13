from scripts.import_variable import *

class MQTTMessagePublisher(threading.Thread):
    def __init__(self, thread_name, topic, broker, port=1883):
        super().__init__(name=thread_name)
        self.topic = topic
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"{self.name} connecté au broker MQTT avec succès.")
        else:
            print(f"{self.name} échec de la connexion, code de retour : {rc}")

    def run(self):
        # Connexion au broker
        self.client.on_connect = self.on_connect
        self.client.connect(self.broker, self.port, 60)
        
        # Lancer la boucle pour se maintenir connecté et envoyer des messages
        self.client.loop_start()

        # Envoyer des messages périodiquement
        for i in range(5):  # Envoie 5 messages pour l'exemple
            message = f"Message {i+1} du topic {self.topic}"
            print(f"{self.name} envoie : {message}")
            self.client.publish(self.topic, message)
            time.sleep(2)  # Attente de 2 secondes entre chaque message
        
        # Après envoi des messages, arrêter la boucle
        self.client.loop_stop()

# # Paramètres de configuration
# topic = "mon/topic"
# broker = "localhost"  # Adresse du broker, ici c'est localhost
# port = 1883  # Port par défaut pour MQTT

# # Création d'un thread pour envoyer des messages MQTT
# mqtt_publisher_thread = MQTTMessagePublisher(thread_name="MQTTPublisherThread", topic=topic, broker=broker, port=port)

# # Démarrer le thread
# mqtt_publisher_thread.start()

# # Attendre que le thread termine son travail
# mqtt_publisher_thread.join()

# print("Tous les messages ont été envoyés.")
