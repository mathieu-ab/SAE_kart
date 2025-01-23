import smbus
import time

# Adresse I2C de l'esclave (doit correspondre à celle définie dans le code Arduino)
SLAVE_ADDRESS = 0x08

# Initialisation du bus I2C
bus = smbus.SMBus(1)  # Le bus I2C 1 est généralement utilisé sur la Raspberry Pi

def read_distance():
    try:
        # Lire les données envoyées par le maître (Arduino)
        data = bus.read_i2c_block_data(SLAVE_ADDRESS, 0, 3)  # Lire 3 octets

        # Extraction des données
        capteur_id = data[0]               # ID du capteur (0, 1 ou 2)
        distance = (data[1] << 8) | data[2]  # Combiner les octets pour obtenir la distance

        return capteur_id, distance

    except Exception as e:
        print(f"Erreur de communication I2C : {e}")
        return None, None

if __name__ == "__main__":
    print("Esclave I2C prêt à recevoir des données...")
    try:
        while True:
            # Lire la distance et l'ID du capteur
            capteur_id, distance = read_distance()

            if capteur_id is not None and distance is not None:
                print(f"Capteur {capteur_id + 1} - Distance : {distance} cm")
            
            # Attente avant la prochaine lecture
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Arrêt du programme.")
