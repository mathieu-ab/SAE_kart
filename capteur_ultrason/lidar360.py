import numpy as np
from rplidar import RPLidar

# Définir le port du LIDAR
PORT_NAME = '/dev/ttyUSB0'  # Modifier selon le système

# Initialiser le LIDAR
lidar = RPLidar(PORT_NAME, baudrate=115200)

try:
    lidar.stop_motor()  # Arrêter le moteur avant de commencer à lire les scans
    for scan in lidar.iter_scans():
        print(scan)  # Affiche le scan brut pour debug
        for meas in scan:
            try:
                print(f"Angle: {meas[1]:.2f}°, Distance: {meas[2]} mm")
            except IndexError:
                print("Erreur lors du traitement des mesures.")
except KeyboardInterrupt:
    print("Arrêt du LIDAR...")
except Exception as e:
    print(f"Erreur : {e}")
finally:
    lidar.stop()
    lidar.disconnect()
