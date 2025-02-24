import serial
import paho.mqtt.client as mqtt

# Configuration du port série
UART_PORT = "/dev/serial0"  # Assurez-vous que c'est le bon port UART
BAUD_RATE = 9600
MQTT_BROKER = "192.168.1.205"
MQTT_TOPIC = "kart/distance"

# Initialisation de la communication série
ser = serial.Serial(UART_PORT, BAUD_RATE, timeout=1)
ser.flush()
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, 1883, 60)


print("Esclave UART prêt à recevoir des données...\n")

while True:
    if ser.in_waiting > 0:  # Vérifie si des données sont disponibles
        try:
            # Lecture des données
            data = ser.readline().decode("utf-8").strip()
            print(f"Distance reçue : {data} cm")
            mqtt_client.publish(MQTT_TOPIC, data)
            print(f"MQTT → {data}")
        except Exception as e:
            print(f"Erreur de lecture UART : {e}")
# Fermeture propre
ser.close()
mqtt_client.disconnect()
print("Arrêt du programme.")
