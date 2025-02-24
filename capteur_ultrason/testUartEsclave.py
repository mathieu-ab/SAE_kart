import serial

# Configuration du port série
UART_PORT = "/dev/serial0"  # Assurez-vous que c'est le bon port UART
BAUD_RATE = 9600

# Initialisation de la communication série
ser = serial.Serial(UART_PORT, BAUD_RATE, timeout=1)
ser.flush()

print("Esclave UART prêt à recevoir des données...\n")

while True:
    if ser.in_waiting > 0:  # Vérifie si des données sont disponibles
        try:
            # Lecture des données
            data = ser.readline().decode("utf-8").strip()
            print(f"Distance reçue : {data} cm")

        except Exception as e:
            print(f"Erreur de lecture UART : {e}")
