import numpy as np
import matplotlib.pyplot as plt
from rplidar import RPLidar

PORT_NAME = '/dev/ttyUSB0'  # Remplace par le bon port

# Initialisation du LIDAR avec une réinitialisation
lidar = RPLidar(PORT_NAME, timeout=3)
lidar.stop()
lidar.stop_motor()
lidar.disconnect()

print("Réinitialisation du LIDAR...")
lidar.connect()
lidar.start_motor()
lidar.scan_mode = 'standard'

def plot_lidar():
    plt.ion()
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    try:
        for scan in lidar.iter_scans():
            angles = [np.deg2rad(meas[1]) for meas in scan]
            distances = [meas[2] for meas in scan]

            ax.clear()
            ax.scatter(angles, distances, c='r', s=5)
            ax.set_ylim(0, max(distances) + 100)
            plt.draw()
            plt.pause(0.1)

    except KeyboardInterrupt:
        print("Arrêt du LIDAR...")
        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()

plot_lidar()
