import serial
import time

# Ouverture de la connexion série avec la caméra JeVois
ser = serial.Serial('/dev/ttyUSB2', 115200, timeout=1)
time.sleep(2)  # Délai pour permettre l'initialisation

# Envoi de la commande pour activer la sortie série de JeVois
ser.write(b"setpar serout All\n")
time.sleep(1)  # Petit délai après l'envoi de la commande

# Lecture et affichage en continu des données reçues
while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(f"Données reçues : {line}")
    except KeyboardInterrupt:
        print("\nArrêt du programme.")
        break
    except Exception as e:
        print(f"Erreur : {e}")
        break

# Fermeture de la connexion série avant de quitter
ser.close()
