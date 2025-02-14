import time
import cv2
cap = cv2.VideoCapture(0)
i = 0
ret, frame = cap.read()
while frame == None :
    ret, frame = cap.read()
    print(frame)
    time.sleep(0.5)
    if i == 20 :
        break
    else :
        i+=1
if ret:
    cv2.imshow("Frame", frame)
else:
    print("Erreur : Impossible de récupérer une image.")
cap.release()
cv2.destroyAllWindows()