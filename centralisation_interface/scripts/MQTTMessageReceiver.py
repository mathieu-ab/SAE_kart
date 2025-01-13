#####information provisoire
#format des message de prevention pour les afficher sur la pi
#prevention_queue.append({"message" : f"Moteur trop chaud k={k}", "start" : int(time()), "end" : choice([None, 7])})

# #fonction pour arrêter un message de prévention sans ou avec délai. Identification par le message
# def arret_prevention(self, message) :
#     for k in range(len(prevention_queue)) :
#         if message == prevention_queue[k]["message"] :
#             prevention_queue.pop(k)
#             return


from scripts.import_variable import *

class MQTTMessageReceiver(threading.Thread):
    def __init__(self, topics):
        threading.Thread.__init__(self)
        self.topics = topics  # Liste des topics à surveiller
        self.client = mqtt.Client()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"{self.name} connecté au broker MQTT avec succès.")
            # S'abonner à plusieurs topics
            for topic in self.topics:
                client.subscribe(topic)
                print(f"{self.name} abonné au topic : {topic}")
        else:
            print(f"{self.name} échec de la connexion, code de retour : {rc}")

    def on_message(self, client, userdata, msg):
        # Afficher le message reçu avec son topic
        print(f"{self.name} - Message reçu sur le topic {msg.topic}: {msg.payload.decode('utf-8')}")
        self.redirect_message(msg.topic, msg.payload.decode('utf-8'))

    def run(self):
        print(f"{self.name} démarrage...")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("localhost", keepalive=60)
        self.client.loop_forever()
            

    def redirect_message(self, topic, message) :
        print(topic)