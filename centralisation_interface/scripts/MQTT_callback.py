



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
        vitesse = int(message)
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