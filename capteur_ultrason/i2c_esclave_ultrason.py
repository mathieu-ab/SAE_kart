import smbus
import time

# Adresse I2C de l'esclave (doit correspondre à celle définie dans le maître)
SLAVE_ADDRESS = 0x08

# Initialisation de la variable pour stocker la distance reçue
distance = 0

# Initialisation de l'I2C sur le bus 1 (le bus I2C standard sur Raspberry Pi 4)
bus = smbus.SMBus(1)

def read_distance():
    """
    Fonction pour lire la distance envoyée par le maître via I2C.
    """
    global distance
    try:
        # Lire deux octets depuis le maître
        high_byte = bus.read_byte(SLAVE_ADDRESS)  # Octet de poids fort
        low_byte = bus.read_byte(SLAVE_ADDRESS)   # Octet de poids faible

        # Reconstituer la distance à partir des deux octets
        distance = (high_byte << 8) | low_byte
        print(f"Distance reçue : {distance} cm")

    except Exception as e:
        print(f"Erreur lors de la lecture I2C : {e}")

if __name__ == "__main__":
    print("Esclave I2C prêt à recevoir des données...")

    try:
        while True:
            read_distance()  # Lire les données depuis le maître
            time.sleep(0.5)  # Pause pour éviter une surcharge

    except KeyboardInterrupt:
        print("\nArrêt du programme.")
    finally:
        bus.close()
