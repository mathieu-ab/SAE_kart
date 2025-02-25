from rplidar import RPLidar

# Définir le port du LIDAR
#PORT_NAME = '/dev/ttyUSB0'  # Modifier selon ton système

# Initialisation du LIDAR
lidar = RPLidar('/dev/ttyUSB0')

try:
    # Démarrer le moteur du LIDAR
    lidar.start_motor()
    print("Moteur du LIDAR démarré")

    # Obtenir un scan et afficher les résultats
    print("Scan en cours...")
    for scan in lidar.iter_scans():
        for meas in scan:
            angle = meas[1]  # Angle en degrés
            distance = meas[2]  # Distance en mm
            print(f"Angle: {angle:.2f}°, Distance: {distance} mm")
        break  # Terminer après un scan pour ne pas boucler indéfiniment

except Exception as e:
    print(f"Erreur: {e}")

finally:
    # Arrêter le moteur et déconnecter le LIDAR proprement
    lidar.stop_motor()
    lidar.disconnect()
    print("Moteur du LIDAR arrêté, LIDAR déconnecté.")
