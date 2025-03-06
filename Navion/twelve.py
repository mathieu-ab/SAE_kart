import serial
import time
import csv

# Configuration du port série
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2)  # Laisser le temps à JeVois de s'initialiser
ser.write(b"setpar serout All\n")  # Activer la sortie série

time.sleep(1)

# Liste des distances prédéfinies (commençant à 3m, puis allant vers les extrêmes)
distances = [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 2.5, 2.0, 1.8, 1.5, 1.2, 1.0, 0.8, 0.6, 0.4, 0.2]

# Fichier CSV pour sauvegarde
csv_filename = "distance_data.csv"

# Fonction pour capturer une seule valeur
def capture_data():
    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(line)  # Affichage de la ligne reçue
            parts = line.split()
            if len(parts) >= 5:
                try:
                    _, confidence, x, y, w, h = parts[-6:]
                    confidence = int(confidence.split(":")[1])  # Extraction du pourcentage
                    x, y, w, h = map(int, [x, y, w, h])
                    return w, h, x, y
                except ValueError:
                    pass  # Ignorer les erreurs de conversion

# Ouverture du fichier CSV en mode écriture
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Distance (m)", "w", "h", "x", "y"])  # En-tête du fichier

    for distance in distances:
        print(f"Place-toi à {distance}m. Les données s'affichent en continu. Appuie sur 'Entrée' pour capturer...")
        input()  # Attente d'une pression sur Entrée
        print(f"Capture des données pour {distance}m...")
        data = capture_data()
        if data:
            w, h, x, y = data
            writer.writerow([distance, w, h, x, y])
            print(f"Données enregistrées pour {distance}m : w={w}, h={h}, x={x}, y={y}")
        else:
            print(f"Aucune donnée valide capturée pour {distance}m.")

print("Capture terminée. Données enregistrées dans", csv_filename)
ser.close()
