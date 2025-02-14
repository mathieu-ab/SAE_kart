from imutils.video import VideoStream
import paho.mqtt.client as mqtt
from imutils import face_utils
from threading import Thread
import numpy as np
import argparse
import imutils
import math
import time
import dlib
import cv2
import os
import sys

class MQTTPublisher:
    def __init__(self, broker_address):
        self.broker_address = broker_address
        self.client = mqtt.Client()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connecté au broker MQTT avec succès.")
        else:
            print(f"Échec de la connexion, code de retour : {rc}")

    def publish_message(self, topic, message):
        self.client.publish(topic, message, retain=False)
        print(f"Message envoyé sur {topic}: {message}")

    def start(self):
        self.client.on_connect = self.on_connect
        self.client.connect(self.broker_address, 1883, keepalive=60)
        self.client.loop_start()

publisher = MQTTPublisher("localhost")
publisher.start()


CURRENT_PATH = "/home/kartuser/SAE_kart/endormissement"
target_fps = 30
frame_interval = 1 / target_fps  # Intervalle entre chaque frame (en secondes)



def alarm():
    global c, alarm_status, alarm_status2
    if alarm_status:
        c += 1
        alarm_status_help = True
        publisher.publish_message("message/prevention", "Ne vous endormez pas au volant et faite une pause !|None")
    elif alarm_status_help and alarm_status == False:
        alarm_status_help = False
        publisher.publish_message("message/prevention", "Ne vous endormez pas au volant et faite une pause !|Stop")
        publisher.publish_message("message/prevention", "Ne vous endormez pas au volant et faite une pause ! |10")
    if alarm_status2:
        publisher.publish_message("message/prevention", "Vous drevez faire une pause !|10")

def eye_aspect_ratio(eye):
    A = math.dist(eye[1], eye[5])
    B = math.dist(eye[2], eye[4])
    C = math.dist(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def final_ear(shape):
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    leftEye, rightEye = shape[lStart:lEnd], shape[rStart:rEnd]
    return (eye_aspect_ratio(leftEye) + eye_aspect_ratio(rightEye)) / 2.0, leftEye, rightEye

def lip_distance(shape):
    top_lip = np.concatenate((shape[50:53], shape[61:64]))
    low_lip = np.concatenate((shape[56:59], shape[65:68]))
    return abs(np.mean(top_lip, axis=0)[1] - np.mean(low_lip, axis=0)[1])

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--webcam", type=int, default=0, help="index of webcam on system")
args = vars(ap.parse_args())

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 30
YAWN_THRESH = 20
alarm_status = alarm_status2 = alarm_status_help = False
COUNTER = c = 0
START_TIME_PROG = time.time() // 60

print("-> Chargement du détecteur et prédicteur...")
detector = cv2.CascadeClassifier(CURRENT_PATH+"/haarcascade_frontalface_default.xml")
predictor = dlib.shape_predictor(CURRENT_PATH+"/shape_predictor_68_face_landmarks.dat")

print("-> Démarrage du flux vidéo")
vs = VideoStream(src=args["webcam"]).start()
time.sleep(1.0)

while True:
    start_time = time.time()
    frame = vs.read()
    
    if frame is None:
        print("Erreur : Impossible de récupérer une image de la caméra.")
        break  # Ou tu peux ajouter une logique pour réessayer après un délai.

    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    for (x, y, w, h) in rects:
        rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
        shape = face_utils.shape_to_np(predictor(gray, rect))
        ear, leftEye, rightEye = final_ear(shape)
        distance = lip_distance(shape)
        
        if ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES and not alarm_status:
                alarm_status = True
                Thread(target=alarm).start()
        else:
            COUNTER, alarm_status = 0, False
        
        if distance > YAWN_THRESH and not alarm_status2:
            alarm_status2 = True
            Thread(target=alarm).start()
        else:
            alarm_status2 = False

    time.sleep(max(0, frame_interval - (time.time() - start_time)))
    
    elapsed_minutes = (time.time() // 60) - START_TIME_PROG
    if elapsed_minutes >= 120:  # 2 heures
        if (elapsed_minutes - 120) % 30 == 0:  # Toutes les 30 minutes après 2h
            print("Attention, ça fait plus de 2h que vous conduisez. une pause s'impose")
        else:
            print("Attention, ça fait 2h que vous conduisez. une pause s'impose")

cv2.destroyAllWindows()
vs.stop()
