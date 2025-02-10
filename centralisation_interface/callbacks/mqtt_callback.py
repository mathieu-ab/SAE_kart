from config import *
from utils.utils import *
from callbacks.callbacks import (
    callback_affichage_button,
    callback_navigation_button,
    callback_systeme_button)

def update_clignotant(self) :
    if self.clignotant["allume"] != None  :
        self.clignotant["etat"] = not self.clignotant["etat"] 
        self.clignotant["cligno"]+=1
        if self.clignotant["allume"] == "gauche" :
            print(self.clignotant)
            if self.clignotant["etat"] == True :    
                self.container_storage["affichage"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = True
                self.container_storage["affichage"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = False
            else :
                self.container_storage["affichage"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = False
                self.container_storage["affichage"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = False
        if self.clignotant["allume"] == "droite" :
            if self.clignotant["etat"] == True :    
                self.container_storage["affichage"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = True
                self.container_storage["affichage"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = False
            else :
                self.container_storage["affichage"]["Clignotant Droit"].get_object("Clignotant Droit Allume").show = False
                self.container_storage["affichage"]["Clignotant Gauche"].get_object("Clignotant Gauche Allume").show = False
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

def update_charge_control(self, message) :
    try :
        new_state = message
        if new_state == "ON" :
            self.container_storage["affichage"]["Activation Charge"].get_object("Charge").state = "pressed"
            self.container_storage["affichage"]["Activation Charge"].get_object("Charge").text.text = "CHARGE ON"
            self.mqtt_thread_handler.publish_message("charge/status", "ON")
        else :
            self.container_storage["affichage"]["Activation Charge"].get_object("Charge").state = "normal"
            self.container_storage["affichage"]["Activation Charge"].get_object("Charge").text.text = "CHARGE OFF"
            self.mqtt_thread_handler.publish_message("charge/status", "OFF")
    except Exception as e:
        print(e)

def update_ligne_blanche(self, message) :
    try :
        new_state = message
        if new_state == "ON" :
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
    if message == "right" and PAGE_HANDLER["indice"] < 2 :
        PAGE_HANDLER["indice"] = (PAGE_HANDLER["indice"]+1)
    elif message == "left" and PAGE_HANDLER["indice"] > 0:
        PAGE_HANDLER["indice"] = (PAGE_HANDLER["indice"]-1)
    
    self.current_page = PAGE_HANDLER["pages"][PAGE_HANDLER["indice"]]
    if self.current_page == "affichage" :
        callback_affichage_button(self)
    elif self.current_page == "navigation" :
        callback_navigation_button(self)
    elif self.current_page == "systeme" :
        callback_systeme_button(self)

def update_button_clignotant(self, message) : 
    self.clignotant["index_clignotant"] = fps//2
    if message == "left" :
        self.clignotant = {"index_clignotant" : 1, "cligno" : 1, "etat" : False, "allume" : "gauche", "start" : int(time())}
    if message == "right" :
        self.clignotant = {"index_clignotant" : 1, "cligno" : 1, "etat" : False, "allume" : "droite", "start" : int(time())} 

def update_message_prevention(self, message) :
    message_parts = message.split("|")
    if len(message_parts) != 2:
        print(f"Longueur du message de prévention incorrecte ! Message : {message}")
        return

    message_text = message_parts[0]
    try:
        if message_parts[1] in ["None", "Stop"] :
            pass
        else :
            message_parts[1] = int(message_parts[1])
    except ValueError:
        print(f"Problème avec la fin du message : {message_parts[1]}")
        return

    if message_parts[1] == "Stop" :
            remove_prevention_message(self, message_text)
    else :
        try :
            index = prevention_queue.index(None)
        except :
            index = 0
        prevention_queue[index] = message_text
        draw_prevention_message(self)
        if message_parts[1] != "None" :
            timer = threading.Timer(message_parts[1], remove_prevention_message, args=(self, message_text))
            timer.start()


def draw_prevention_message(self_Interface) :
    for i in range(len(prevention_queue)) :
        if prevention_queue[i] == None :
            self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} text").text = ""
            self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} text").show = False
            self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} icon").show = False
            self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} Rectangle").show = False
        else :
            self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} text").text = prevention_queue[i]
            self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} text").show = True
            self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} icon").show = True
            self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} Rectangle").show = True

def remove_prevention_message(self, msg) : 
    global prevention_queue
    try :
        index = prevention_queue.index(msg)
    except :
        print(f"Le message {msg} n'est pas présent dans les message affiché ou a déjà été supprimé")
        return
    prevention_queue[index] = None
    non_none = [x for x in prevention_queue if x is not None]
    none = [x for x in prevention_queue if x is None]
    prevention_queue = non_none + none
    draw_prevention_message(self)