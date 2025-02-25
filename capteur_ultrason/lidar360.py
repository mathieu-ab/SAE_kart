import time
from rplidar import RPLidar

# LIDAR setup
lidar = RPLidar('/dev/ttyUSB0')  # Assurez-vous que le port est correct

try:
    print("Starting LIDAR scanning...")

    # Démarrer le moteur du LIDAR
    lidar.start_motor()

    # Collecter les scans
    for scan in lidar.iter_scans():
        if len(scan) > 0:
            print(f"Scan en cours avec {len(scan)} mesures:")
            for measurement in scan:
                try:
                    if len(measurement) != 3:
                        raise ValueError(f"Longueur de mesure inattendue: {len(measurement)}")
                    
                    quality, angle, distance = measurement
                    # Afficher les résultats de l'angle et de la distance
                    print(f"Qualité: {quality}, Angle: {angle:.2f}°, Distance: {distance:.2f} mm")
                except Exception as e:
                    print(f"Erreur lors du traitement de la mesure: {e}")
    
except Exception as e:
    print(f"Erreur avec le LIDAR: {e}")

finally:
    print("Arrêt du LIDAR...")
    lidar.stop_motor()  # Arrêter le moteur du LIDAR
    lidar.disconnect()  # Déconnecter proprement
    print("LIDAR arrêté et déconnecté.")
