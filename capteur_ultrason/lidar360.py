import numpy as np
import matplotlib.pyplot as plt
from rplidar import RPLidar

# Définir le port du LIDAR (UART sur la Raspberry Pi)
PORT_NAME = '/dev/serial0'  # Sur Windows : 'COM3' ou 'COM4'

# Initialiser le LIDAR
lidar = RPLidar(PORT_NAME)

def plot_lidar():
    plt.ion()  # Activer le mode interactif
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})  # Graphique polaire

    try:
        for scan in lidar.iter_scans():
            angles = [np.deg2rad(meas[1]) for meas in scan]  # Conversion angle en radians
            distances = [meas[2] for meas in scan]  # Distances en mm

            ax.clear()
            ax.scatter(angles, distances, c='r', s=5)  # Affichage des points
            ax.set_ylim(0, max(distances) + 100)  # Ajustement de l'échelle
            plt.draw()
            plt.pause(0.1)  # Pause pour rafraîchir l'affichage

    except KeyboardInterrupt:
        print("Arrêt du LIDAR...")
        lidar.stop()
        lidar.disconnect()

plot_lidar()
