import serial
import time

# Coefficients de régression linéaire
a = -0.0058559  # Coefficient directeur
b = 9.0531      # Ordonnée à l'origine

# Fonction pour estimer la distance à partir de la hauteur détectée
def estimer_distance(h):
    return a * h + b  # Application de l'équation de régression linéaire

# Ouverture de la connexion série avec JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
time.sleep(2)  # Délai pour permettre l'initialisation de la caméra

# Activation de la sortie série de JeVois
ser.write(b"setpar serout All\n")
time.sleep(1)  # Petit délai après l'envoi de la commande

print("Lecture des données en cours... Appuyez sur Ctrl+C pour arrêter.")

# Boucle principale pour la lecture des données et l'estimation de la distance
while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            parts = line.split()
            if len(parts) >= 5:  # Vérification du nombre de données reçues
                try:
                    h = int(parts[4])  # Extraction de la hauteur détectée
                    distance = estimer_distance(h)  # Calcul de la distance estimée
                    print(f"Hauteur détectée: {h} pixels → Distance estimée: {distance:.2f} m")
                except ValueError:
                    print("Erreur de conversion des données reçues.")
    except KeyboardInterrupt:
        print("\nArrêt du programme.")
        break

# Fermeture de la connexion série avant de quitter le programme
ser.close()
