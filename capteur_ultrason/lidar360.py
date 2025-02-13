from rplidar import RPLidar

# Définir le port du LIDAR
PORT_NAME = '/dev/ttyUSB0'  # Modifier selon le système

# Initialiser le LIDAR
lidar = RPLidar(PORT_NAME)

#Arrêter le moteur après 5 secondes
import time
time.sleep(5)

lidar.stop_motor()
print("Moteur du LIDAR arrêté")

# Déconnexion propre
lidar.stop()
lidar.disconnect()
