import spi
import time

# Initialisation du bus SPI
spi = spi.Spi()  # Création de l'objet SPI
spi.open(0, 0)         # Bus 0, périphérique 0 (CS0)
spi.max_speed_hz = 50000  # Vitesse maximale du bus SPI
spi.mode = 0b00           # Mode SPI (CPOL=0, CPHA=0)

def receive_distance():
    """
    Fonction pour recevoir la distance en deux octets via SPI.
    Retourne la distance en centimètres.
    """
    # Lire deux octets depuis le bus SPI
    response = spi.xfer2([0x00, 0x00])  # Envoyer deux octets vides pour recevoir les données
    high_byte = response[0]            # Premier octet reçu
    low_byte = response[1]             # Deuxième octet reçu

    # Reconstituer la valeur de distance
    distance = (high_byte << 8) | low_byte
    return distance

try:
    print("Esclave SPI prêt à recevoir les données...")
    while True:
        distance = receive_distance()
        print(f"Distance reçue : {distance} cm")

        # Ajouter une logique si nécessaire, par exemple :
        if distance > 0 and distance <= 100:
            print("Obstacle détecté à proximité !")
        else:
            print("Pas d'obstacle détecté.")

        time.sleep(0.1)  # Pause avant la prochaine lecture

except KeyboardInterrupt:
    print("\nArrêt du programme.")

finally:
    spi.close()
