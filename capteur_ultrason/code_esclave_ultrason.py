import RPi.GPIO as GPIO
import time

# Définition des broches SPI
MISO = 19  # Master In Slave Out
MOSI = 21  # Master Out Slave In
SCLK = 23  # Clock
CS = 24    # Chip Select

# Initialisation des broches
GPIO.setmode(GPIO.BCM)
GPIO.setup(MISO, GPIO.OUT)  # MISO est une sortie (vers maître)
GPIO.setup(MOSI, GPIO.IN)   # MOSI est une entrée (depuis maître)
GPIO.setup(SCLK, GPIO.IN)   # Horloge est une entrée
GPIO.setup(CS, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # CS activé en LOW

def lire_octet():
    """
    Fonction pour lire un octet via SPI (bit par bit).
    """
    octet = 0
    for i in range(8):  # Lire 8 bits
        while GPIO.input(SCLK) == 0:  # Attendre le flanc montant de l'horloge
            pass
        bit = GPIO.input(MOSI)  # Lire le bit sur la ligne MOSI
        octet = (octet << 1) | bit  # Décaler à gauche et ajouter le bit lu
        while GPIO.input(SCLK) == 1:  # Attendre le flanc descendant de l'horloge
            pass
    return octet

try:
    print("Esclave SPI prêt à recevoir...")
    while True:
        if GPIO.input(CS) == 0:  # Vérifier si l'esclave est sélectionné
            high_byte = lire_octet()  # Lire l'octet de poids fort
            low_byte = lire_octet()   # Lire l'octet de poids faible
            distance = (high_byte << 8) | low_byte  # Reconstituer la distance
            print(f"Distance reçue : {distance} cm")

except KeyboardInterrupt:
    print("\nArrêt du programme.")
finally:
    GPIO.cleanup()
