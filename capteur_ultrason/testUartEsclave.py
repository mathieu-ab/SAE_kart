import serial
import paho.mqtt.client as mqtt

# Configuration
UART_PORT = "/dev/serial0"
BAUD_RATE = 9600
MQTT_BROKER = "localhost"
MQTT_TOPIC = "kart/distance"

# Initialisation
ser = serial.Serial(UART_PORT, BAUD_RATE, timeout=1)
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, 1883, 60)

print("Lecture UART et publication MQTT...")

while True:
    try:
        if ser.in_waiting > 0:
            data = ser.readline().decode("utf-8", errors="ignore").strip()
            if data.isdigit():
                mqtt_client.publish(MQTT_TOPIC, data)
                print(f"MQTT → {data}")
    except KeyboardInterrupt:
        break

# Fermeture propre
ser.close()
mqtt_client.disconnect()
print("Arrêt du programme.")
