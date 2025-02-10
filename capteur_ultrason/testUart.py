import serial

# Ouvrir le port série
ser = serial.Serial('/dev/serial0', 9600, timeout=1)
ser.flush()

while True:
    if ser.in_waiting > 0:
        message = ser.readline().decode('utf-8').strip()
        print("Reçu de l'Arduino :", message)
