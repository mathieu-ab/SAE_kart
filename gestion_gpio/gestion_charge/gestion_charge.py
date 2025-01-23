import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

# Configuration des GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_INPUT_PIN = 19  # GPIO pour recevoir l'activation MLI (remplacez par votre GPIO)
GPIO_OUTPUT_PIN = 18  # GPIO pour activer la charge (remplacez par votre GPIO)
GPIO.setup(GPIO_INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GPIO_OUTPUT_PIN, GPIO.OUT)

# Configuration MQTT
BROKER = "localhost"  # Remplacez par l'adresse de votre broker MQTT
PORT = 1883  # Port par défaut pour MQTT
TOPIC_MLI = "charge/mli"
TOPIC_CONTROL = "charge/control"

# Fonction appelée lorsque le client reçoit un message MQTT
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
        topic = msg.topic

        if topic == TOPIC_CONTROL:
            if payload == "ON":
                print("Reçu ON, GPIO_OUTPUT_PIN mis à 1")
                GPIO.output(GPIO_OUTPUT_PIN, GPIO.HIGH)
            elif payload == "OFF":
                print("Reçu OFF, GPIO_OUTPUT_PIN mis à 0")
                GPIO.output(GPIO_OUTPUT_PIN, GPIO.LOW)

    except Exception as e:
        print(f"Erreur lors du traitement du message: {e}")

# Initialisation du client MQTT
client = mqtt.Client()
client.on_message = on_message

try:
    client.connect(BROKER, PORT, 60)
    client.subscribe([(TOPIC_MLI, 0), (TOPIC_CONTROL, 0)])
    print("Connecté au broker MQTT et abonné aux topics")

    client.loop_start()

    while True:
        # Vérifie l'état du GPIO_INPUT_PIN
        if GPIO.input(GPIO_INPUT_PIN) == GPIO.HIGH:
            print("GPIO_INPUT_PIN activé, envoi MQTT: charge/mli ON")
            client.publish(TOPIC_MLI, "ON")
        else:
            print("GPIO_INPUT_PIN désactivé, envoi MQTT: charge/mli OFF")
            client.publish(TOPIC_MLI, "OFF")

        time.sleep(1)  # Pause pour éviter une surcharge

except KeyboardInterrupt:
    print("Interruption par l'utilisateur")

finally:
    print("Nettoyage GPIO et déconnexion MQTT")
    GPIO.cleanup()
    client.loop_stop()
    client.disconnect()
