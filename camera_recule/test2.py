import cv2
import subprocess

# Fonction pour dessiner les lignes de guidage
def draw_guide_lines(frame):
    height, width, _ = frame.shape

    # Définir les zones
    safe_zone_y = int(height * 0.7)
    caution_zone_y = int(height * 0.85)
    danger_zone_y = int(height * 0.95)

    # Ligne verte pour la zone sûre
    cv2.line(frame, (int(width * 0.2), safe_zone_y), (int(width * 0.8), safe_zone_y), (0, 255, 0), 3)
    # Ligne jaune pour la zone de précaution
    cv2.line(frame, (int(width * 0.1), caution_zone_y), (int(width * 0.9), caution_zone_y), (0, 255, 255), 3)
    # Ligne rouge pour la zone de danger
    cv2.line(frame, (0, danger_zone_y), (width, danger_zone_y), (0, 0, 255), 3)
    # Lignes diagonales blanches pour le guidage
    cv2.line(frame, (int(width * 0.4), safe_zone_y), (int(width * 0.3), height), (255, 255, 255), 2)
    cv2.line(frame, (int(width * 0.6), safe_zone_y), (int(width * 0.7), height), (255, 255, 255), 2)

    return frame

# Paramètres pour le flux RTSP
rtsp_url = "rtsp://192.168.1.195:8554/stream"  # Remplacez <IP_DU_SERVEUR> par l'adresse de votre serveur RTSP
width, height = 640, 480
fps = 30

# Commande FFmpeg pour envoyer le flux vidéo
ffmpeg_command = [
    "C:\\PATH_programe\\ffmpeg.exe",
    "-re",  # Lecture en temps réel
    "-f", "rawvideo",  # Format brut
    "-pixel_format", "bgr24",  # Format des pixels (OpenCV utilise BGR)
    "-video_size", f"{width}x{height}",  # Taille de la vidéo
    "-framerate", str(fps),  # FPS
    "-i", "-",  # Entrée via stdin
    "-c:v", "libx264",  # Codec vidéo
    "-preset", "ultrafast",  # Réduction de la latence
    "-f", "rtsp",  # Format de sortie RTSP
    rtsp_url  # URL cible
]

# Lancer FFmpeg en tant que processus
ffmpeg_process = subprocess.Popen(ffmpeg_command, stdin=subprocess.PIPE)

# Ouvrir la webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, fps)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la webcam.")
    exit()

try:
    print("Streaming rear-view camera via RTSP... Press Ctrl+C to stop.")
    while True:
        # Lire une frame depuis la webcam
        ret, frame = cap.read()

        if not ret:
            print("Erreur : Impossible de lire la frame.")
            break

        # Ajouter les lignes de guidage
        frame_with_lines = draw_guide_lines(frame)

        # Envoyer la frame à FFmpeg
        ffmpeg_process.stdin.write(frame_with_lines.tobytes())

except KeyboardInterrupt:
    print("\nArrêt du flux RTSP...")

finally:
    # Libérer les ressources
    cap.release()
    ffmpeg_process.stdin.close()
    ffmpeg_process.wait()
    print("Flux RTSP arrêté.")
