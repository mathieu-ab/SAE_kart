from rplidar import RPLidar

# Définir le port du LIDAR
PORT_NAME = '/dev/ttyUSB0'  # Modifier selon le système

# Initialiser le LIDAR
lidar = RPLidar(PORT_NAME)

# Fonction pour afficher l'angle et la distance en continu
def show_lidar_data():
    try:
        # Démarrer le moteur du LIDAR
        lidar.start_motor()
        print("Moteur du LIDAR démarré")

        # Récupérer et afficher les scans en continu
        for scan in lidar.iter_scans():
            for meas in scan:
                angle = meas[1]  # Angle en degrés
                distance = meas[2]  # Distance en mm
                print(f"Angle: {angle:}°, Distance: {distance} mm")

    except KeyboardInterrupt:
        print("Arrêt du LIDAR...")

    finally:
        # Déconnexion propre (arrêter le moteur et se déconnecter)
        lidar.stop()
        lidar.disconnect()
        print("LIDAR déconnecté.")

# Exécuter la fonction
show_lidar_data()
