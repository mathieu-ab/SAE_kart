from module_import import *

if sys.platform == "win32":
    CURRENT_PATH = "C:\\Users\\mathi\\Documents\\info\\Python\\projet\\SAE_kart\\centralisation_interface" #chemin d'accés sur mon ordi pour les tests
    tactile = False
else:
    CURRENT_PATH = "/home/kartuser/SAE_kart/centralisation_interface" #chamin d'accés sur le kart
    tactile = True

#pour définir si on utilise le programe en mode tablette (tactile) ou ordinateur (souris)

if tactile :
    MOUSEBUTTONUP = pygame.FINGERUP
    MOUSEBUTTONDOWN = pygame.FINGERDOWN
else :
    MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
    MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN


#loop principale du programme
main_loop = True
#limitation de lavitesse de rafraichissement. Pour fps=30, on a 30 images par secondes
fps = 30
# listes pour avoir les dégradé de couleur
color_green_to_red = list(Color("#61ff01").range_to(Color("#ccff01"),15))
color_green_to_red.extend(list(Color("#ccff01").range_to(Color("#fff001"),15)))
color_green_to_red.extend(list(Color("#fff001").range_to(Color("#ffae01"),15)))
color_green_to_red.extend(list(Color("#ffae01").range_to(Color("#ff6101"),15)))
color_green_to_red.extend(list(Color("#ff6101").range_to(Color("#ff0101"),15)))
#queue des messages de prévention
prevention_queue = [None, None, None]
#vitesse maximal autorisé pour la vitesse de consigne du régulateur/limitateur
VITESSE_MAX = 30
#IP du broker situé sur le hotspot
IP_BROKER_MQTT = "192.168.1.195"
#topic auquel l'abonnement est fait
#les topics commenté sont ceux pour lesquel la pi envoi des message uniquement. Nul besoin d'écouté des réponses pour ceux là
topics = [
    "moteur/vitesse",             #--reçois
    "moteur/temperature",         #--reçois
    # "moteur/mode",              #envoi
    "moteur/mode/control",              #reçois
                                  #
    # "gps/zoom"                  #envoi
                                  #
    "bms/batterie",               #--reçois
    "bms/temperature",            #--reçois

    # "charge/status",            #envoi
    "charge/control",             #--reçois
                                  #
    "message/prevention",         #--reçois
                                  #
    # "aide/clignotant",          #envoi
    # "aide/reg_lim",             #envoi
    # "aide/vitesse_consigne",    #envoi
    "aide/vitesse_consigne/control",    #reçois
    # "aide/ligne_blanche/status",#envoi
    # "aide/endormissement/status",#envoi
    # "aide/obstacle/status"      #envoi
    "aide/ligne_blanche/control", #--reçois
    "aide/endormissement/control",#--reçois
    "aide/obstacle/control",      #--reçois
    "bouton/page",                #--reçois
    "bouton/clignotant",           #--reçois
    "test/topic",
    "eg"
]
#topics pour lesquel l'option retain sera désactivé (retain = dernier message sauvegardé sur le broker et envoyé au chaque nouvel connection)
topics_non_retain = [
    "charge/control",
    "bouton/page",
    "bouton/clignotant",
    "moteur/mode",
    "aide/clignotant",
    "aide/reg_lim",
    "message/prevention",
    "gps/destonation"
]

# Déclaration globale du cache de polices
font_cache: List[Dict[str, Any]] = []
# Déclaration des couleurs des objet pour les 2 mode : dark et light
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
                        "light" : (135, 185, 254),
                        "dark" : (4, 12, 25)
                    }
                }
#Permet de switch de page directement avec des boutons physique
PAGE_HANDLER = {"pages" : ["affichage", "navigation", "systeme"], "indice" : 0}
#temps en secondes entre chaque update de la carte de navigation
TIME_UPDATE_NAV = 3
#touche ignoré pour écrire la destination
IGNORED_KEYS = [
    "shift", "left shift",          # Shift
    "ctrl", "left ctrl", "right ctrl",           # Control
    "alt", "left alt",            # Alt
    "caps lock",       # Caps Lock
    "numlock",        # Num Lock
    "scroll lock",     # Scroll Lock
    "lgui",           # Left Windows (GUI)
    "rgui",           # Right Windows (GUI)
    "esc",            # Escape
    "pause",          # Pause
    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",  # F1 to F12
    "insert",         # Insert
    "home",           # Home
    "page up",         # Page Up
    "page down",       # Page Down
    "end",            # End
    "left",           # Left arrow
    "right",          # Right arrow
    "up",             # Up arrow
    "down",           # Down arrow
    "delete",
    "escape",
    "tab",
    "break",
    "print screen"
]