import serial
import paho.mqtt.client as mqtt

# Configuration du port UART sur la Raspberry Pi
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

# Configuration du client MQTT
MQTT_BROKER = "192.168.1.205"  # Remplace par l'IP de ton broker MQTT
MQTT_PORT = 1883
MQTT_TOPIC = "kart/capteurs/distance"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

try:
    while True:
        if uart.in_waiting > 0:  # Vérifie si des données sont disponibles
            data = uart.readline().decode('utf-8').strip()  # Lire et décoder les données
            print("Donnée reçue :", data)  # Afficher les distances
            
            # Envoi des données au broker MQTT
            client.publish(MQTT_TOPIC, data)
            print(f"Donnée envoyée sur MQTT : {data}")

except KeyboardInterrupt:
    print("Arrêt du programme.")
    uart.close()
    client.disconnect()
