import serial
import time

# Coefficients from MATLAB regression equation
a = -0.0058559  # Slope (coefficient directeur)
b = 9.5212     # Intercept (ordonnée à l'origine)

# Function to estimate distance using the corrected equation
def estimer_distance(h):
    return a * h + b  # Applying the regression equation

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
time.sleep(2)  # Allow JeVois to initialize

# Enable serial output from JeVois
ser.write(b"setpar serout All\n")
time.sleep(1)

print("Lecture des données en cours... Appuyez sur Ctrl+C pour arrêter.")

# Read data and estimate corrected distance
while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            parts = line.split()
            if len(parts) >= 5:  # Ensure the line contains enough data
                try:
                    h = int(parts[4])  # Extract height
                    distance_estimee = estimer_distance(h)
                    print(f"Hauteur détectée: {h} pixels → Distance corrigée: {distance_estimee:.2f} m")
                except ValueError:
                    print("Erreur de conversion des données reçues.")
    except KeyboardInterrupt:
        print("\nArrêt du programme.")
        break

ser.close()
