import serial

# Configuration du port série (remplace "/dev/serial0" par "/dev/ttyS0" si nécessaire)
ser = serial.Serial('/dev/serial0', 9600, timeout=1)
ser.flush()

while True:
    if ser.in_waiting > 0:
        try:
            distance = ser.readline().decode('utf-8' ,errors='ignore').strip()
            print(f"Distance reçue : {distance} cm")
        except UnicodeDecodeError:
            print("Erreur de décodage, données corrompues")
