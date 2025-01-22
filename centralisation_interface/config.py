from module_import import *

#--|--# lists/variables
CURRENT_PATH = "/home/kartuser/SAE_kart/centralisation_interface"
# CURRENT_PATH = "C:/Users/mathi/Documents/info/Python/projet/SAE_kart/centralisation_interface"

#pour définir si on utilise le programe en mode tablette (tactile) ou ordinateur (souris)
tactile = True
if tactile :
    MOUSEBUTTONUP = pygame.FINGERUP
    MOUSEBUTTONDOWN = pygame.FINGERDOWN
else :
    MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
    MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN


#loop pour passer d'une page à une autre
main_loop = True

fps = 30
# listes pour avoir les dégradé de couleur
color_green_to_red = list(Color("#61ff01").range_to(Color("#ccff01"),15))
color_green_to_red.extend(list(Color("#ccff01").range_to(Color("#fff001"),15)))
color_green_to_red.extend(list(Color("#fff001").range_to(Color("#ffae01"),15)))
color_green_to_red.extend(list(Color("#ffae01").range_to(Color("#ff6101"),15)))
color_green_to_red.extend(list(Color("#ff6101").range_to(Color("#ff0101"),15)))
#queue des messages de prévention
prevention_queue = []

VITESSE_MAX = 30
IP_BROKER_MQTT = "192.168.1.195"
topics = [
    "moteur/vitesse",       #--reçois
    "moteur/temperature",   #--reçois
    # "moteur/mode",          #envoi
                            #
    "bms/batterie",         #--reçois
    "bms/temperature",      #--reçois

    # "charge/status",        #envoi
    "charge/control",        #--reçois
                            #
    "message/prevention",   #--reçois
                            #
    # "aide/clignotant",      #envoi
    # "aide/reg_lim",         #envoi
    # "aide/vitesse_consigne",#envoi
    # "aide/ligne_blanche/status",#envoi
    # "aide/endormissement/status",#envoi
    # "aide/obstacle/status"  #envoi
    "aide/ligne_blanche/control", #--reçois
    "aide/endormissement/control",#--reçois
    "aide/obstacle/control"       #--reçois
]

# Déclaration globale du cache de polices
font_cache: List[Dict[str, Any]] = []
dark_light_mode = {"etat" : "dark",
                   "text" : {
                        "light" : (0,0,0),
                        "dark" : (255,255,255)
                    },
                    "button" : {"dark" : {
                                    "pressed" : (89, 10, 220),
                                    "normal" : (37, 52, 92),
                                    "disabled" : (37, 52, 92)},
                                "light" : {
                                    "pressed" : (176, 128, 255),
                                    "normal" : (150, 162, 251),
                                    "disabled" : (178, 210, 255)}
                        },
                    "container" : {
                        "light" : (202, 208, 255),
                        "dark" : (17, 26, 50)
                    },
                    "background" : {
                        "light" : (179, 211, 255),
                        "dark" : (4, 12, 25)
                    }
                }