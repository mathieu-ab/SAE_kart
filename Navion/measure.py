import serial
import time
import numpy as np

# Données de référence (Hauteur en fonction de la Distance)
hauteur_reference = np.array([1668, 1546, 1507, 1474, 1391, 1329, 1180, 1127, 952, 951, 950, 897, 777, 740, 511, 496, 447, 421, 418, 417])
distance_reference = np.array([0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])

# Ajustement d'une régression linéaire
coeffs = np.polyfit(hauteur_reference, distance_reference, 1)  # Ajustement linéaire
def estimer_distance(h):
    return np.polyval(coeffs, h)  # Calcul de la distance estimée

# Connexion au port série de JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
time.sleep(2)  # Attente de l'initialisation

# Activation de la sortie série complète
ser.write(b"setpar serout All\n")
time.sleep(1)

print("Lecture des données en cours... Appuyez sur Ctrl+C pour arrêter.")

# Lecture et estimation de la distance
while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            parts = line.split()
            if len(parts) >= 5:  # Vérification que la ligne contient les valeurs attendues
                try:
                    h = int(parts[4])  # Extraction de la hauteur
                    distance_estimee = estimer_distance(h)
                    print(f"Hauteur détectée: {h} pixels → Distance estimée: {distance_estimee:.2f} m")
                except ValueError:
                    print("Erreur de conversion des données reçues.")
    except KeyboardInterrupt:
        print("\nArrêt du programme.")
        break

ser.close()
