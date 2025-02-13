import numpy as np
from rplidar import RPLidar

# Définir le port du LIDAR
PORT_NAME = '/dev/ttyUSB0'  # Modifier selon le système

# Initialiser le LIDAR
lidar = RPLidar(PORT_NAME)

try:
    for scan in lidar.iter_scans():
        for meas in scan:
            print(f"Angle: {meas[1]:.2f}°, Distance: {meas[2]} mm")
except KeyboardInterrupt:
    print("Arrêt du LIDAR...")
finally:
    lidar.stop()
    lidar.disconnect()
