from config import *
from utils.utils import *
from callbacks.callbacks import (
    callback_affichage_button,
    callback_navigation_button,
    callback_systeme_button,
    callback_aide_button)

def update_clignotant(self) :
    if self.clignotant["allume"] != None  :
        self.clignotant["etat"] = not self.clignotant["etat"] 
        self.clignotant["cligno"]+=1
        if self.clignotant["allume"] == "gauche" :
            if self.clignotant["etat"] == True :    
                self.container_storage["affichage"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = True
                self.container_storage["affichage"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = False
                self.container_storage["navigation"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = True
                self.container_storage["navigation"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = False
            else :
                self.container_storage["affichage"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = False
                self.container_storage["affichage"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = False
                self.container_storage["navigation"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = False
                self.container_storage["navigation"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = False
        if self.clignotant["allume"] == "droite" :
            if self.clignotant["etat"] == True :    
                self.container_storage["affichage"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = True
                self.container_storage["affichage"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = False
                self.container_storage["navigation"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = True
                self.container_storage["navigation"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = False
            else :
                self.container_storage["affichage"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = False
                self.container_storage["affichage"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = False
                self.container_storage["navigation"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = False
                self.container_storage["navigation"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = False
        if self.clignotant["cligno"] == 7 :
            self.clignotant["allume"] = None
            self.mqtt_thread_handler.publish_message("bouton/clignotant", "eteint")

def update_batterie(self, message) : 
    try :
        batterie = round(int(message) / 100, 2)
        self.container_storage["affichage"]["Batterie"].get_object("Batterie Niveau Container").get_object("Niveau").text = f"{int(batterie*100)}"
        self.container_storage["affichage"]["Batterie"].get_object("Rectangle Batterie").color = hex_to_rgb(color_green_to_red[int((1-batterie)*len(color_green_to_red))])
        self.container_storage["affichage"]["Batterie"].get_object("Rectangle Batterie").position = (131, 150+int((1-batterie)*150))
        self.container_storage["affichage"]["Batterie"].get_object("Rectangle Batterie").kwargs["size"] = (73, int(batterie*150))
        self.container_storage["affichage"]["Batterie"].get_object("Batterie Niveau Container").reCalcule_position()
        self.container_storage["affichage"]["Batterie"].get_object("Batterie Niveau Container").reCalcule_position()
    except Exception as e:
        print(e)    

def update_vitesse(self, message) :
    try :
        vitesse = int(float(message))
        self.container_storage["affichage"]["Vitesse"].get_object("Vitesse").text = str(vitesse)
        self.container_storage["navigation"]["Vitesse"].get_object("Vitesse").text = str(vitesse)
        self.vitesse = vitesse
    except Exception as e:
        print(e)

def update_temperature_moteur(self, message) :
    try :
        temperature_moteur = int(message)
        self.temperature_moteur = temperature_moteur
        self.container_storage["affichage"]["Temperature"].get_object("Temperature Container").get_object("Temperature Moteur").text = str(test_convertion_Celsius_to_Fahrenheit(temperature_moteur, self.temperature_unite))
        self.container_storage["affichage"]["Temperature"].get_object("Temperature Moteur Unite").text = self.temperature_unite
        self.container_storage["affichage"]["Temperature"].reCalcule_position()
        self.container_storage["affichage"]["Temperature"].reCalcule_position()
    except Exception as e:
        print(e)

def update_temperature_batterie(self, message) :
    try :
        temperature_batterie = int(message)
        self.temperature_batterie = temperature_batterie
        self.container_storage["affichage"]["Temperature"].get_object("Temperature Container").get_object("Temperature Batterie").text = str(test_convertion_Celsius_to_Fahrenheit(temperature_batterie, self.temperature_unite))
        self.container_storage["affichage"]["Temperature"].get_object("Temperature Batterie Unite").text = self.temperature_unite
        self.container_storage["affichage"]["Temperature"].reCalcule_position()
        self.container_storage["affichage"]["Temperature"].reCalcule_position()
    except Exception as e:
        print(e)

def update_charge_status(self, message) :
    try :
        if message == "PLUGGED" :
            self.container_storage["affichage"]["Activation Charge"].show = True
            self.container_storage["affichage"]["Activation Charge"].get_object("Charge").state = "normal"
            self.container_storage["affichage"]["Activation Charge"].get_object("Charge").text.text = "CHARGE OFF"
            self.container_storage["affichage"]["Activation Charge"].show = True
            self.container_storage["affichage"]["Activation Charge"].get_object("Title_container_Activation Charge").show = True
            self.container_storage["affichage"]["Activation Charge"].get_object("Charge").show = True
        else :
            self.container_storage["affichage"]["Activation Charge"].get_object("Charge").state = "disabled"
            self.container_storage["affichage"]["Activation Charge"].get_object("Charge").text.text = "CHARGE OFF"
            self.container_storage["affichage"]["Activation Charge"].show = False
            self.container_storage["affichage"]["Activation Charge"].get_object("Title_container_Activation Charge").show = False
            self.container_storage["affichage"]["Activation Charge"].get_object("Charge").show = False
    except Exception as e:
        print(e)

def update_ligne_blanche(self, message) :
    try :
        new_state = message
        if new_state == "ON" :
            script_path = "/home/kartuser/SAE_kart/endormissement/endormissement.py"

            # Vérifie si le script est déjà en cours d'exécution
            check_process = f"pgrep -f '{script_path}'"
            process = subprocess.run(check_process, shell=True, executable="/bin/bash", capture_output=True, text=True)

            if process.stdout.strip():  
                print(f"{script_path} est déjà en cours d'exécution.")
            else:
                print(f"Lancement de {script_path}...")
                subprocess.Popen(["python3", script_path], cwd=os.path.dirname(script_path))

            self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").get_object("Switch Detection ligne blanche").etat = True
            self.mqtt_thread_handler.publish_message("aide/ligne_blanche/status", "ON")
        else :
            self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").get_object("Switch Detection ligne blanche").etat = False
            self.mqtt_thread_handler.publish_message("aide/ligne_blanche/status", "OFF")
    except Exception as e:
        print(e)

def update_obstacle(self, message) :
    try :
        new_state = message
        if new_state == "ON" :
            self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").get_object("Switch Detection obstacle").etat = True
            self.mqtt_thread_handler.publish_message("aide/obstacle/status", "ON")
        else :
            self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").get_object("Switch Detection obstacle").etat = False
            self.mqtt_thread_handler.publish_message("aide/obstacle/status", "OFF")
    except Exception as e:
        print(e)

def update_endormissement(self, message) :
    try :
        new_state = message
        if new_state == "ON" :
            self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").get_object("Switch Endormissement").etat = True
            self.mqtt_thread_handler.publish_message("aide/endormissement/status", "ON")
        else :
            self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").get_object("Switch Endormissement").etat = False
            self.mqtt_thread_handler.publish_message("aide/endormissement/status", "OFF")
    except Exception as e:
        print(e)

def update_bouton_page(self, message) :
    if message == "right" and PAGE_HANDLER["indice"] < 4 :
        PAGE_HANDLER["indice"] = (PAGE_HANDLER["indice"]+1)
    elif message == "left" and PAGE_HANDLER["indice"] > 0:
        PAGE_HANDLER["indice"] = (PAGE_HANDLER["indice"]-1)
    
    self.current_page = PAGE_HANDLER["pages"][PAGE_HANDLER["indice"]]
    if self.current_page == "affichage" :
        callback_affichage_button(self)
    elif self.current_page == "navigation" :
        callback_navigation_button(self)
    elif self.current_page == "aide" :
        callback_aide_button(self)
    elif self.current_page == "systeme" :
        callback_systeme_button(self)

def update_button_clignotant(self, message) : 
    self.clignotant["index_clignotant"] = fps//2
    if message == "left" :
        self.clignotant = {"index_clignotant" : 1, "cligno" : 1, "etat" : False, "allume" : "gauche", "start" : int(time())}
    if message == "right" :
        self.clignotant = {"index_clignotant" : 1, "cligno" : 1, "etat" : False, "allume" : "droite", "start" : int(time())} 

def update_message_prevention(self, message):
    print(f"Message reçu dans update_message_prevention: {message}")
    
    message_parts = message.split("|")
    print(f"Parts après split: {message_parts}")  # Debugging
    
    if len(message_parts) not in [2, 3]:
        print(f"Longueur du message de prévention incorrecte ! Message : {message}")
        return

    message_text = message_parts[0]

    # Vérification du clignotement
    clignotement = False
    if len(message_parts) == 3:
        if message_parts[2] in ["True", "False"]:
            clignotement = message_parts[2] == "True"
        else:
            print(f"Erreur: Valeur inattendue pour clignotement: {message_parts[2]}")

    # Vérification du temps
    try:
        if message_parts[1] not in ["None", "Stop"]:
            message_parts[1] = int(message_parts[1])
    except ValueError:
        print(f"Problème avec la fin du message : {message_parts[1]}")
        return

    print(f"Message traité: texte={message_text}, temps={message_parts[1]}, clignotement={clignotement}")

    if message_parts[1] == "Stop":
        remove_prevention_message(self, message_text)
    else:
        prevention_queue.append([message_text, clignotement])
        draw_prevention_message(self)
        
        if message_parts[1] != "None":
            timer = threading.Timer(message_parts[1], remove_prevention_message, args=(self, message_text))
            timer.start()



def remove_prevention_message(self, msg) : 
    global prevention_queue
    try :
        index = [prevention_queue[i][0] for i in range(len(prevention_queue))].index(msg)
    except :
        print(f"Le message {msg} n'est pas présent dans les message affiché ou a déjà été supprimé")
        return
    prevention_queue.pop(index)
    draw_prevention_message(self)


def update_mode_conduite(self, msg_received) :
    if msg_received == "Mode_eco" : 
        if self.container_storage["affichage"]["Mode Conduite"].get_object("Eco").state != "pressed" :
            self.container_storage["affichage"]["Mode Conduite"].get_object("Eco").state = "pressed"
            self.container_storage["affichage"]["Mode Conduite"].get_object("Normal").state = "normal"
            self.container_storage["affichage"]["Mode Conduite"].get_object("Sport").state = "normal"
    elif msg_received == "Mode_normal" :
        if self.container_storage["affichage"]["Mode Conduite"].get_object("Normal").state != "pressed" :
            self.container_storage["affichage"]["Mode Conduite"].get_object("Eco").state = "normal"
            self.container_storage["affichage"]["Mode Conduite"].get_object("Normal").state = "pressed"
            self.container_storage["affichage"]["Mode Conduite"].get_object("Sport").state = "normal"
        image_object = self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").get_object("Switch Reg")
        if image_object.image_path == "systeme/switch_neutre" :
            return
        image_object.change_image("systeme/switch_neutre")
        self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").get_object("Switch Reg").size = (72, 68)
        #activation des options de vitesse de consigne
        self.container_storage["systeme"]["Regulateur"].get_object("Bouton Moins").show = False
        self.container_storage["systeme"]["Regulateur"].get_object("Vitesse Consigne").show = False
        self.container_storage["systeme"]["Regulateur"].get_object("Bouton Plus").show = False
    elif msg_received == "Mode_sport" :
        if self.container_storage["affichage"]["Mode Conduite"].get_object("Sport").state != "pressed" :
            self.container_storage["affichage"]["Mode Conduite"].get_object("Eco").state = "normal"
            self.container_storage["affichage"]["Mode Conduite"].get_object("Normal").state = "normal"
            self.container_storage["affichage"]["Mode Conduite"].get_object("Sport").state = "pressed"
    elif msg_received == "Mode_regulateur" :
        image_object = self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").get_object("Switch Reg")
        if image_object.image_path == "systeme/switch_regulateur" :
            return
        image_object.change_image("systeme/switch_regulateur")
        self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").get_object("Switch Reg").size = (72, 68)
        #activation des options de vitesse de consigne
        self.container_storage["systeme"]["Regulateur"].get_object("Bouton Moins").show = True
        self.container_storage["systeme"]["Regulateur"].get_object("Vitesse Consigne").show = True
        self.container_storage["systeme"]["Regulateur"].get_object("Bouton Plus").show = True
    elif msg_received == "Mode_limitateur" :
        image_object = self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").get_object("Switch Reg")
        if image_object.image_path == "systeme/switch_limitateur" :
            return
        image_object.change_image("systeme/switch_limitateur")
        self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").get_object("Switch Reg").size = (72, 68)
        #activation des options de vitesse de consigne
        self.container_storage["systeme"]["Regulateur"].get_object("Bouton Moins").show = True
        self.container_storage["systeme"]["Regulateur"].get_object("Vitesse Consigne").show = True
        self.container_storage["systeme"]["Regulateur"].get_object("Bouton Plus").show = True

def update_eg(self, msg_recieved) :
    if msg_recieved == "allume" :
        self.eg_choice = choice([['1120-', 84], ['1119-', 81], ['1119_21-', 78], ['1119_1-', 89]])
        self.current_page = "eg"
    else :
        self.current_page = "affichage"


# def update_vitesse_consigne(self, msg_received) :
#     try :
#         self.vitesse_consigne = int(msg_received)
#         self.container_storage["systeme"]["Regulateur"].get_object("Vitesse Consigne").text = self.vitesse_consigne
#     except :
#         print("Problème de conversion en int pour la vitesse de consigne control.")



def update_1224h(self, message) :
    try :
        new_state = message
        if new_state == "ON" :
            self.format_heure = "24h"
            self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object("Switch 24h").etat = True
            self.mqtt_thread_handler.publish_message("aide/1224h/status", "ON")
        else :
            self.format_heure = "12h"
            self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object("Switch 24h").etat = False
            self.mqtt_thread_handler.publish_message("aide/1224h/status", "OFF")
    except Exception as e:
        print(e)

def update_temperature_unite(self, message) :
    try :
        new_state = message
        if new_state == "ON" :
            self.temperature_unite = "°C"
            self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object("Switch °C").etat = True
            self.mqtt_thread_handler.publish_message("aide/temperature_unite/status", "ON")
        else :
            self.temperature_unite = "°F"
            self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object("Switch °C").etat = False
            self.mqtt_thread_handler.publish_message("aide/temperature_unite/status", "OFF")
        temperature_batterie = self.temperature_batterie
        temperature_moteur = self.temperature_moteur
        self.mqtt_thread_handler.publish_message("moteur/temperature", f"{temperature_moteur}")
        self.mqtt_thread_handler.publish_message("bms/temperature", f"{temperature_batterie}")
    except Exception as e:
        print(e)
    
def update_dark_liht(self, message) :
    try :
        new_state = message
        if new_state == "ON" :
            dark_light_mode["etat"] = "dark"
            self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object("Switch dark mode").etat = True
            self.mqtt_thread_handler.publish_message("aide/dark_light/status", "ON")
        else :
            dark_light_mode["etat"] = "light"
            self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object("Switch dark mode").etat = False
            self.mqtt_thread_handler.publish_message("aide/dark_light/status", "OFF")
        self.container_storage["affichage"]["Background"].get_object("Background Rectangle").change_color(dark_light_mode["background"][dark_light_mode["etat"]])
        self.container_storage["navigation"]["Background"].get_object("Background Rectangle").change_color(dark_light_mode["background"][dark_light_mode["etat"]])
        self.container_storage["aide"]["Background"].get_object("Background Rectangle").change_color(dark_light_mode["background"][dark_light_mode["etat"]])
        self.container_storage["systeme"]["Background"].get_object("Background Rectangle").change_color(dark_light_mode["background"][dark_light_mode["etat"]])
        for page in self.container_storage :
            for container in self.container_storage[page].values() :
                container.update_color()
    except Exception as e:
        print(e)
        
def update_navigation(self, message):
    try:
        radar = self.container_storage["aide"]["Nav Radar"]

        # Hide all indicators initially
        indicators = [
            "Near Left", "Near Center", "Near Right",
            "Medium Left", "Medium Center", "Medium Right",
            "Far Left", "Far Center", "Far Right"
        ]
        for indicator in indicators:
            radar.get_object(indicator).show = False

        # Handle "Clear" message (no objects detected)
        if message == "Clear":
            return  # All indicators remain hidden

        # Process multiple detections if message contains "|"
        detected_positions = message.split(" | ")

        # Show only the relevant indicators
        for pos in detected_positions:
            if pos in indicators:
                radar.get_object(pos).show = True

    except Exception as e:
        print(e)

        
def update_vitesseauto(self, message) :
    try :
            vitesse = int(float(message))
            self.container_storage["aide"]["Nav Radar"].get_object("Vitesse").get_object("vitesse").text = str(vitesse)
            self.vitesse = vitesse
    except Exception as e:
        print(e)


def update_charge_button_state(self, message) :
    st = "pressed" if message == "ON" else "normal"
    self.container_storage["affichage"]["Activation Charge"].get_object("Charge").state = st
    self.container_storage["affichage"]["Activation Charge"].get_object("Charge").text.text = f"CHARGE {message}"
