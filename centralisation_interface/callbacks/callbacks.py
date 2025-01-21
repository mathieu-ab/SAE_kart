from module_import import subprocess
from scripts import MQTTMessageHandler
from config import dark_light_mode

def callback_affichage_button(self_Interface) :
    self_Interface.current_page = "affichage"
    self_Interface.container_storage["affichage"]["Bouton Choix Page"].get_object("Affichage").state = "pressed"
    self_Interface.container_storage["affichage"]["Bouton Choix Page"].get_object("Navigation").state = "normal"
    self_Interface.container_storage["affichage"]["Bouton Choix Page"].get_object("Système").state = "normal"

def callback_navigation_button(self_Interface) :
    self_Interface.current_page = "navigation"
    self_Interface.container_storage["navigation"]["Bouton Choix Page"].get_object("Affichage").state = "normal"
    self_Interface.container_storage["navigation"]["Bouton Choix Page"].get_object("Navigation").state = "pressed"
    self_Interface.container_storage["navigation"]["Bouton Choix Page"].get_object("Système").state = "normal"

def callback_systeme_button(self_Interface) :
    self_Interface.current_page = "systeme"
    self_Interface.container_storage["systeme"]["Bouton Choix Page"].get_object("Affichage").state = "normal"
    self_Interface.container_storage["systeme"]["Bouton Choix Page"].get_object("Navigation").state = "normal"
    self_Interface.container_storage["systeme"]["Bouton Choix Page"].get_object("Système").state = "pressed"

def callback_eco_button(self_Interface) :
    if self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Eco").state != "pressed" :
        self_Interface.mqtt_thread_handler.publish_message("moteur/mode", "eco")
        self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Eco").state = "pressed"
        self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Normal").state = "normal"
        self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Sport").state = "normal"

def callback_normal_button(self_Interface) :
    if self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Normal").state != "pressed" :
        self_Interface.mqtt_thread_handler.publish_message("moteur/mode", "normal")
    self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Eco").state = "normal"
    self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Normal").state = "pressed"
    self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Sport").state = "normal"

def callback_sport_button(self_Interface) :
    if self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Sport").state != "pressed" :
        self_Interface.mqtt_thread_handler.publish_message("moteur/mode", "sport")
    self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Eco").state = "normal"
    self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Normal").state = "normal"
    self_Interface.container_storage["affichage"]["Mode Conduite"].get_object("Sport").state = "pressed"


def callback_charge_button(self_Interface) :
    #popup activation
    #disable le bouton pendant 10s
    self_Interface.mqtt_thread_handler.publish_message("batterie/charge", "activation charge")
    
    script_path = '/home/kartuser/SAE_kart/camera_recule/camera_recule.py'
    try:
        print(f"Exécution du script en arrière-plan : {script_path}")
        # Lancer le script en arrière-plan (ne bloque pas le script principal)
        process = subprocess.Popen(["python", script_path])
        print("Script lancé en arrière-plan.")
        
        # Vous pouvez ajouter ici du code supplémentaire pour continuer à exécuter d'autres tâches dans le script principal
        return process
    except FileNotFoundError:
        print(f"Fichier non trouvé : {script_path}")
        return None
    except Exception as e:
        print(f"Erreur lors de l'exécution du script : {str(e)}")
        return None

def callback_1224h_switch(state_switch, self_Interface) :
    if state_switch :
        self_Interface.format_heure = "24h"
    else :
        self_Interface.format_heure = "12h"

def callback_temperature_unite_switch(state_switch, self_Interface) :
    if state_switch :
        self_Interface.temperature_unite = "°C"
    else :
        self_Interface.temperature_unite = "°F"
    temperature_batterie = self_Interface.temperature_batterie
    temperature_moteur = self_Interface.temperature_moteur
    self_Interface.mqtt_thread_handler.publish_message("moteur/temperature", f"{temperature_moteur}")
    self_Interface.mqtt_thread_handler.publish_message("bms/temperature", f"{temperature_batterie}")

def callback_dark_liht_switch(state_switch, self_Interface) :
    if state_switch :
        dark_light_mode["etat"] = "dark"
        etat = True
    else :
        dark_light_mode["etat"] = "light"
        etat = False
    self_Interface.clickable_object = {
        "affichage" : [],
        "navigation" : [],
        "systeme" : []
    }
    self_Interface.container_storage = {
        "affichage" : {},
        "navigation" : {},
        "systeme" : {}
    }
    self_Interface.setup_draw(self_Interface)
    self_Interface.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object("Switch dark mode").etat = etat
