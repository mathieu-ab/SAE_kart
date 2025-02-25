from rplidar import RPLidar

PORT_NAME = "/dev/ttyUSB0"  # Vérifie que c'est bien le bon port !

try:
    lidar = RPLidar(PORT_NAME)
    lidar.start_motor()
    print("LIDAR démarré !")

    print("Lecture d'un seul scan pour tester...")
    for scan in lidar.iter_scans():
        print(f"Nombre de mesures : {len(scan)}")
        for quality, angle, distance in scan:
            print(f"Angle: {angle:.2f}°, Distance: {distance} mm")
        break  # Arrêter après un seul scan pour tester

except Exception as e:
    print(f"Erreur: {e}")

finally:
    print("Arrêt du LIDAR...")
    lidar.stop_motor()
    lidar.disconnect()
    print("LIDAR déconnecté.")
