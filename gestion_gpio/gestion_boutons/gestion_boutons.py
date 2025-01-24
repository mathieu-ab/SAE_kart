from gpiozero import Button
from signal import pause
import paho.mqtt.client as mqtt


test = False

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au broker MQTT avec succès.")
    else:
        print(f"Échec de la connexion, code de retour : {rc}")

# Fonction pour publier un message via MQTT
def publish_message(topic, message):
    try:
        client.publish(topic, message, retain=False)
        print(f"Message '{message}' envoyé sur le topic '{topic}'")
    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")

# Callbacks pour les différents boutons
def callback_right_page(pin):
    if test :
        print(f"Appui sur le bouton connecté à GPIO {pin}")
    publish_message("bouton/page", "right")

def callback_left_page(pin):
    if test :
        print(f"Appui sur le bouton connecté à GPIO {pin}")
    publish_message("bouton/page", "left")

def callback_clignotant_droit(pin):
    if test :
        print(f"Appui sur le bouton connecté à GPIO {pin}")
    publish_message("bouton/clignotant", "right")

def callback_clignotant_left(pin):
    if test :
        print(f"Appui sur le bouton connecté à GPIO {pin}")
    publish_message("bouton/clignotant", "left")

# Configurer plusieurs boutons
buttons = [
    {"button": Button(5, bounce_time=0.1), "callback": callback_right_page},
    {"button": Button(6, bounce_time=0.1), "callback": callback_left_page},
    {"button": Button(16, bounce_time=0.1), "callback": callback_clignotant_droit},
    {"button": Button(17, bounce_time=0.1), "callback": callback_clignotant_left},
]

# Associer les callbacks avec une fermeture pour capturer la variable correcte
for button in buttons:
    button_instance = button["button"]
    callback_function = button["callback"]
    button_instance.when_pressed = lambda b=button_instance, cb=callback_function: cb(b.pin.number)

print("Appuyez sur un bouton (Ctrl+C pour quitter)")
client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", keepalive=60)
client.loop_start()
pause()

