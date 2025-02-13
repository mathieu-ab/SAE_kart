import numpy as np
from rplidar import RPLidar

# Définir le port du LIDAR
PORT_NAME = '/dev/ttyUSB0'  # Modifier selon le système

# Initialiser le LIDAR avec la vitesse de communication explicite
lidar = RPLidar(PORT_NAME, baudrate=256000)  # Tente un baudrate plus élevé

try:
    lidar.start_motor()  # Démarrer le moteur avant de commencer à lire les scans

    # Récupérer un seul scan
    scan = next(lidar.iter_scans())  
    for meas in scan:
        print(f"Angle: {meas[1]:.2f}°, Distance: {meas[2]} mm")
except KeyboardInterrupt:
    print("Arrêt du LIDAR...")
except Exception as e:
    print(f"Erreur : {e}")
finally:
    lidar.stop_motor()  # Arrêter le moteur après l'utilisation
    lidar.stop()
    lidar.disconnect()
