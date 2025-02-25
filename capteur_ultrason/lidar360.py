from rplidar import RPLidar

PORT_NAME = '/dev/ttyUSB0'  # Modifier selon le système

def show_lidar_data():
    try:
        print("Initialisation du LIDAR...")
        lidar = RPLidar(PORT_NAME)
        print("LIDAR connecté.")

        # Démarrer le moteur du LIDAR
        lidar.start_motor()
        print("Moteur du LIDAR démarré")

        # Récupérer et afficher les scans en continu
        for scan in lidar.iter_scans():
            print(f"Scan reçu, nombre de mesures: {len(scan)}")
            for meas in scan:
                angle = meas[1]  # Angle en degrés
                distance = meas[2]  # Distance en mm
                print(f"Angle: {angle:.2f}°, Distance: {distance} mm")

    except Exception as e:
        print(f"Erreur pendant l'exécution: {e}")

    finally:
        print("Arrêt du LIDAR...")
        try:
            lidar.stop()
            lidar.disconnect()
            print("LIDAR déconnecté.")
        except Exception as e:
            print(f"Erreur lors de la déconnexion du LIDAR: {e}")

# Exécuter la fonction
show_lidar_data()
