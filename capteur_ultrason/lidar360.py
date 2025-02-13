import numpy as np
from rplidar import RPLidar

# Définir le port du LIDAR
PORT_NAME = '/dev/ttyUSB0'  # Modifier selon le système

# Initialiser le LIDAR
lidar = RPLidar(PORT_NAME)

try:
    print("Démarrage de la lecture des données...")
    for scan in lidar.iter_scans():
        for meas in scan:
            if len(meas) < 3:
                continue  # Éviter les erreurs sur les mesures incorrectes
            angle, distance = meas[1], meas[2]
            print(f"Angle: {angle:.2f}°, Distance: {distance} mm")
except RPLidarException as e:
    print(f"Erreur LIDAR: {e}")
except KeyboardInterrupt:
    print("Arrêt du LIDAR...")
finally:
    lidar.stop()
    lidar.disconnect()
    print("LIDAR déconnecté.")
