import smbus
import time

# Adresse I2C de l'esclave (doit correspondre à celle définie dans le maître)
SLAVE_ADDRESS = 0x08

# Initialisation de l'I2C sur le bus 1 (le bus I2C standard sur Raspberry Pi 4)
bus = smbus.SMBus(1)

# Nombre de capteurs
NUM_SENSORS = 3

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

    try:
        while True:
            # Lire et afficher les distances pour chaque capteur
            for sensor_id in range(NUM_SENSORS):
                distance = read_sensor_data(sensor_id)
                if distance is not None:
                    print(f"Capteur {sensor_id} : Distance reçue = {distance} cm")

            time.sleep(0.5)  # Pause pour éviter une surcharge

    except KeyboardInterrupt:
        print("\nArrêt du programme.")
    finally:
        bus.close()
