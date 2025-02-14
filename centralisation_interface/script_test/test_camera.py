from picamera2 import Picamera2
import cv2
import numpy as np

# Initialisation de la caméra
picam2 = Picamera2()
picam2.start()

# Capture une image
frame = picam2.capture_array()

# Affiche l'image avec OpenCV
cv2.imshow("Image Capturée", frame)

# Attends que l'utilisateur appuie sur une touche pour fermer la fenêtre
cv2.waitKey(0)

# Libère les ressources et ferme les fenêtres
cv2.destroyAllWindows()
picam2.stop()