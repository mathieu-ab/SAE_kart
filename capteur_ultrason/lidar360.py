from rplidar import RPLidar

PORT_NAME = '/dev/ttyUSB0'

try:
    lidar = RPLidar(PORT_NAME)
    print("Connexion au LIDAR réussie.")
    lidar.stop()
    lidar.disconnect()
except Exception as e:
    print(f"Erreur de connexion au LIDAR: {e}")
