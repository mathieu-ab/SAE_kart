import cv2

# Ouvrir la caméra (index 0 pour la première caméra)
cap = cv2.VideoCapture(0)

# Lire une seule image
ret, frame = cap.read()

# Vérifier si l'image a été capturée avec succès
if ret:
    # Afficher l'image
    cv2.imshow("Captured Frame", frame)

    # Attendre que l'utilisateur appuie sur une touche pour fermer la fenêtre
    cv2.waitKey(0)
else:
    print("Erreur : Impossible de récupérer une image.")

# Libérer la caméra et fermer la fenêtre
cap.release()
cv2.destroyAllWindows()
