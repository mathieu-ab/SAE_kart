import serial

# Configuration de l'UART sur la Raspberry Pi
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

try:
    while True:
        if uart.in_waiting > 0:  # Vérifier si des données sont disponibles
            data = uart.readline().decode('utf-8').strip()  # Lire et décoder les données
            print("Donnée reçue :", data)  # Afficher la distance reçue
except KeyboardInterrupt:
    print("Arrêt du programme.")
    uart.close()
