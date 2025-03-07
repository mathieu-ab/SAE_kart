import serial
import time

# Coefficients from MATLAB regression equation
a = -0.0054741  # Slope (coefficient directeur)
b = 9.0531      # Intercept (ordonnée à l'origine)

# Coefficients from the correction factor equation
a_corr = -0.00233  # Slope for correction factor
b_corr = 2.63156   # Intercept for correction factor

# Function to estimate raw distance using regression equation
def estimer_distance(h):
    return a * h + b  # Applying the regression equation

# Function to compute dynamic correction factor
def correction_factor(h):
    return a_corr * h + b_corr  # Computes correction factor based on height

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
                    h = int(parts[4])  # Extract detected height
                    raw_distance = estimer_distance(h)  # Compute initial distance
                    factor = correction_factor(h)  # Compute dynamic correction factor
                    corrected_distance = raw_distance / factor  # Apply correction

                    print(f"Hauteur détectée: {h} pixels → Distance corrigée: {corrected_distance:.2f} m")
                except ValueError:
                    print("Erreur de conversion des données reçues.")
    except KeyboardInterrupt:
        print("\nArrêt du programme.")
        break

ser.close()
