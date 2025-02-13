from rplidar import RPLidar

# ⚡ Définir le port du LIDAR (À modifier si nécessaire)
PORT_NAME = '/dev/ttyUSB0'  

# Initialiser le LIDAR
lidar = RPLidar(PORT_NAME)

try:
    print("LIDAR en marche... Appuie sur Ctrl+C pour arrêter.")
    
    for scan in lidar.iter_scans(max_buf_meas=300):  # Limite le buffer pour éviter l’erreur
        for (_, angle, distance) in scan:
            print(f"Angle: {angle:.1f}° | Distance: {distance:.1f} mm")
        print("-" * 30)  # Séparation entre chaque tour de scan

except KeyboardInterrupt:
    print("Arrêt du LIDAR...")
    
finally:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    print("LIDAR déconnecté.")
