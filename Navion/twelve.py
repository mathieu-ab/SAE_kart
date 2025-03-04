import serial
import time
import csv
from collections import deque

# Configuration du port série
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2)  # Laisser le temps à JeVois de s'initialiser
ser.write(b"setpar serout All\n")  # Activer la sortie série

time.sleep(1)

# Liste des distances prédéfinies (commençant à 3m, puis allant vers les extrêmes)
distances = [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 2.5, 2.0, 1.8, 1.5, 1.2, 1.0, 0.8, 0.6, 0.4, 0.2]

# Fichier CSV pour sauvegarde
csv_filename = "distance_data.csv"

# Fonction pour capturer les 10 dernières valeurs et en faire la moyenne
def capture_last_data(buffer):
    w_values, h_values, x_values, y_values = [], [], [], []
    
    for line in buffer:
        parts = line.split()
        if len(parts) >= 5:
            try:
                _, confidence, x, y, w, h = parts[-6:]
                confidence = int(confidence.split(":")[1])  # Extraction du pourcentage
                x, y, w, h = map(int, [x, y, w, h])
                
                w_values.append(w)
                h_values.append(h)
                x_values.append(x)
                y_values.append(y)
            except ValueError:
                pass  # Ignorer les erreurs de conversion
    
    # Calcul de la moyenne
    if w_values and h_values:
        w_mean = sum(w_values) / len(w_values)
        h_mean = sum(h_values) / len(h_values)
        x_mean = sum(x_values) / len(x_values)
        y_mean = sum(y_values) / len(y_values)
        return w_mean, h_mean, x_mean, y_mean
    return None

# Ouverture du fichier CSV en mode écriture
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Distance (m)", "w", "h", "x", "y"])  # En-tête du fichier

    for distance in distances:
        print(f"Place-toi à {distance}m. Les données s'affichent en continu. Appuie sur 'Entrée' pour capturer...")
        last_lines = deque(maxlen=10)  # Stocke les 10 dernières lignes
        
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                print(line)  # Affichage en continu
                last_lines.append(line)  # Stocke la dernière ligne lue
            
            user_input = input("Appuie sur Entrée pour capturer les données...")
            if user_input == "":  # Capture lorsque Entrée est pressée
                print(f"Capture des dernières données pour {distance}m...")
                data = capture_last_data(last_lines)
                if data:
                    w_mean, h_mean, x_mean, y_mean = data
                    writer.writerow([distance, w_mean, h_mean, x_mean, y_mean])
                    print(f"Données enregistrées pour {distance}m : w={w_mean}, h={h_mean}, x={x_mean}, y={y_mean}")
                else:
                    print(f"Aucune donnée valide capturée pour {distance}m.")
                break  # Passer à la distance suivante

print("Capture terminée. Données enregistrées dans", csv_filename)
ser.close()
