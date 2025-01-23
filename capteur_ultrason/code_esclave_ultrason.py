import spidev
import time

# Initialisation du bus SPI
spi = spidev.SpiDev()  # Création de l'objet SPI
spi.open(0, 0)         # Bus 0, périphérique 0 (CS0)
spi.max_speed_hz = 50000  # Vitesse du SPI
spi.mode = 0b00           # Mode SPI (CPOL=0, CPHA=0)

try:
    print("Lecture SPI en cours...")
    while True:
        # Envoi d'une requête au maître (2 octets vides pour recevoir la réponse)
        response = spi.xfer2([0x00, 0x00])
        
        # Extraction des octets reçus
        high_byte = response[0]
        low_byte = response[1]

        # Reconstitution de la distance
        distance = (high_byte << 8) | low_byte
        print(f"Distance reçue : {distance} cm")

        time.sleep(0.1)  # Pause avant la prochaine lecture

except KeyboardInterrupt:
    print("\nArrêt du programme.")

finally:
    spi.close()
