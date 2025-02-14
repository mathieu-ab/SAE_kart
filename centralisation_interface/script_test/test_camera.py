import time
import cv2
cap = cv2.VideoCapture(0)
time.sleep(1)  # Délai de 1 seconde pour s'assurer que la caméra est prête
ret, frame = cap.read()
print(ret, frame, cap)
if ret:
    cv2.imshow("Frame", frame)
else:
    print("Erreur : Impossible de récupérer une image.")
cap.release()
cv2.destroyAllWindows()