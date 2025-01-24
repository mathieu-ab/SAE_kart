import smbus
import time
import paho.mqtt.client as mqtt

# Adresse I2C de l'esclave (doit correspondre à celle définie dans le maître)
SLAVE_ADDRESS = 0x08

# Initialisation de l'I2C sur le bus 1 (le bus I2C standard sur Raspberry Pi 4)
bus = smbus.SMBus(1)

# Nombre de capteurs
NUM_SENSORS = 3

# Paramètres MQTT
MQTT_BROKER = "localhost"  # Adresse IP du broker MQTT (à remplacer par la tienne)
MQTT_PORT = 1883               # Port par défaut pour MQTT
MQTT_TOPIC = "kart/distance"   # Sujet pour publier les données

# Initialisation du client MQTT
mqtt_client = mqtt.Client()

def connect_mqtt():
    """
    Connecter le client MQTT au broker.
    """
    try:
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
        print("Connecté au broker MQTT")
    except Exception as e:
        print(f"Erreur lors de la connexion au broker MQTT : {e}")
        exit(1)

def publish_distance(sensor_id, distance):
    """
    Publier la distance mesurée pour un capteur spécifique via MQTT.
    Args:
        sensor_id (int): Identifiant du capteur (0, 1, ou 2).
        distance (int): Distance mesurée par le capteur (en cm).
    """
    try:
        # Créer un message au format JSON
        message = {
            "sensor_id": sensor_id,
            "distance_cm": distance
        }
        # Publier le message
        mqtt_client.publish(MQTT_TOPIC, str(message))
        print(f"Publié via MQTT : {message}")
    except Exception as e:
        print(f"Erreur lors de la publication MQTT : {e}")

def read_sensor_data(sensor_id):
    """
    Fonction pour lire la distance d'un capteur spécifique via I2C.
    Args:
        sensor_id (int): Identifiant du capteur (0, 1, ou 2).
    Returns:
        int: Distance mesurée par le capteur (en cm).
    """
    try:
        # Envoyer l'ID du capteur à lire au maître
        bus.write_byte(SLAVE_ADDRESS, sensor_id)
        time.sleep(0.01)  # Pause pour permettre au maître de répondre

        # Lire deux octets depuis le maître
        high_byte = bus.read_byte(SLAVE_ADDRESS)  # Octet de poids fort
        low_byte = bus.read_byte(SLAVE_ADDRESS)   # Octet de poids faible

        # Reconstituer la distance à partir des deux octets
        distance = (high_byte << 8) | low_byte
        return distance

    except Exception as e:
        print(f"Erreur lors de la lecture I2C pour le capteur {sensor_id} : {e}")
        return None

if __name__ == "__main__":
    print("Esclave I2C prêt à recevoir des données...")

    # Connecter le client MQTT au broker
    connect_mqtt()

    try:
        while True:
            # Lire et publier les distances pour chaque capteur
            for sensor_id in range(NUM_SENSORS):
                distance = read_sensor_data(sensor_id)
                if distance is not None:
                    print(f"Capteur {sensor_id} : Distance reçue = {distance} cm")
                    # Publier la distance via MQTT
                    publish_distance(sensor_id, distance)

            time.sleep(0.5)  # Pause pour éviter une surcharge

    except KeyboardInterrupt:
        print("\nArrêt du programme.")
    finally:
        bus.close()
        mqtt_client.disconnect()
