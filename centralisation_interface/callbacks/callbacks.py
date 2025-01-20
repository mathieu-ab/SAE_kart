from scripts import MQTTMessageHandler

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