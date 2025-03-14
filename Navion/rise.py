import serial
import time

# Ouverture de la connexion série avec la caméra JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
time.sleep(2)  # Délai pour permettre l'initialisation

# Envoi de la commande pour activer la sortie série de JeVois
ser.write(b"setpar serout All\n")
time.sleep(1)  # Petit délai après l'envoi de la commande

# Lecture et affichage en continu des données reçues
while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(line)
    except KeyboardInterrupt:
        print("\nArrêt...")
        break
    except Exception as e:
        print(e)
        break

ser.close()
