import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

# Configuration des GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_INPUT_PIN = 12  # GPIO pour recevoir l'activation MLI 
GPIO_OUTPUT_PIN = 13  # GPIO pour activer la charge 
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
                GPIO.output(GPIO_OUTPUT_PIN, GPIO.HIGH)
                client.publish("charge/status", "ON")
            elif payload == "OFF":
                GPIO.output(GPIO_OUTPUT_PIN, GPIO.LOW)
                client.publish("charge/status", "OFF")

    except Exception as e:
        print(f"Erreur lors du traitement du message: {e}")

# Fonction appelée lors d'un changement d'état du GPIO_INPUT_PIN
def gpio_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        client.publish(TOPIC_MLI, "ON")
    else:
        client.publish(TOPIC_MLI, "OFF")

# Initialisation du client MQTT
client = mqtt.Client()
client.on_message = on_message

try:
    # Connexion au broker MQTT
    client.connect(BROKER, PORT, 60)
    client.subscribe([(TOPIC_MLI, 0), (TOPIC_CONTROL, 0)])

    # Ajout d'une interruption sur le GPIO_INPUT_PIN
    GPIO.add_event_detect(GPIO_INPUT_PIN, GPIO.BOTH, callback=gpio_callback, bouncetime=200)

    # Lancer la boucle MQTT
    client.loop_forever()

except KeyboardInterrupt:
    print("Interruption par l'utilisateur")

finally:
    print("Nettoyage GPIO et déconnexion MQTT")
    GPIO.cleanup()
    client.disconnect()
