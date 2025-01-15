#import des modules
from colour import Color
from random import choice, randint
from time import sleep, time, localtime
import pygame
import threading
import socket
import os
from pathlib import Path
import paho.mqtt.client as mqtt





#--|--# lists/variables
CURRENT_PATH = Path("").resolve()

#pour définir si on utilise le programe en mode tablette (tactile) ou ordinateur (souris)
tactile = False
if tactile :
    MOUSEBUTTONUP = pygame.FINGERUP
    MOUSEBUTTONDOWN = pygame.FINGERDOWN
else :
    MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
    MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN


#loop pour passer d'une page à une autre
main_loop = True
affichage_loop = True
navigation_loop = False
systeme_loop = False

fps = 30
#coordonées des boutons des différent mode en x
info_mode_conduite = {"eco" : 25, "normal" : 203, "sport" : 384}
# listes pour avoir les dégradé de couleur
color_green_to_red = list(Color("#61ff01").range_to(Color("#ccff01"),15))
color_green_to_red.extend(list(Color("#ccff01").range_to(Color("#fff001"),15)))
color_green_to_red.extend(list(Color("#fff001").range_to(Color("#ffae01"),15)))
color_green_to_red.extend(list(Color("#ffae01").range_to(Color("#ff6101"),15)))
color_green_to_red.extend(list(Color("#ff6101").range_to(Color("#ff0101"),15)))
#queue des messages de prévention
prevention_queue = []
#dictionnaire des switchs
switch_dict = {"detection_ligne_blanche" : {"etat" : True,
                            "position" : [292, 27],
                            "position_x_rond" : [297]},
                "detection_obstacle" : {"etat" : True,
                            "position" : [292, 92],
                            "position_x_rond" : [297]},
                "endormissement" : {"etat" : True,
                            "position" : [292, 157],
                            "position_x_rond" : [297]},
                "syst_heure" : {"etat" : True,
                            "position" : [568, 27],
                            "position_x_rond" : [575]},
                "syst_unite" : {"etat" : True,
                            "position" : [568, 92],
                            "position_x_rond" : [575]},
                "syst_dark_mode" : {"etat" : True,
                            "position" : [568, 157],
                            "position_x_rond" : [575]},

                }

VITESSE_MAX = 30
COLOR_MODE_CONDUITE = {"dark" : {
                            "selected" : (89, 10, 220),
                            "not selected" : (12, 20, 31)},
                        "light" : {
                            "selected" : (176, 128, 255),
                            "not selected" : (178, 210, 255)}
                        }
IP_BROKER_MQTT = "192.168.1.88"
topics = [
    "moteur/vitesse",       #--reçois
    "moteur/temperature",   #--reçois
    "moteur/mode",          #envoi
                            #
    "bms/batterie",         #--reçois
    "bms/temperature",      #--reçois
                            #
    "message/prevention",   #--reçois
                            #
    "aide/clignotant",      #envoi
    "aide/reg_lim",         #envoi
    "aide/vitesse_consigne",#envoi
    "aide/ligne_blanche",   #envoi
    "aide/endormissement",  #envoi
    "aide/obstacle"         #envoi
]