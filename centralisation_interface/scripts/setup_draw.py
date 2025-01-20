from module_import import *
from config import *
from callbacks import *
from components import Container
from components import Button
from components import Text
from components import Image
from components import Rectangle



def setup_draw(self) :
    #--------------Container Background--------------#
    self.container_storage["affichage"]["Background"] = Container(
        label="Background",
        show_label=False,
        position=(-10, -10),
        size=(820, 500),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["affichage"]["Background"].add_object(
        Rectangle(
            label="Background Rectangle",
            size=(820, 480),
            color=dark_light_mode["background"][dark_light_mode["etat"]],
            border_radius=0,
            show=True
        ),
        relative_position=(0, 0)
    )
    #--------------Container Mode Conduite--------------#
    self.container_storage["affichage"]["Mode Conduite"] = Container(
        label="Mode Conduite",
        show_label=True,
        position=(20, 11),
        size=(367, 88),
        show=True,
        allignement="horizontal"
    )
    #bouton Eco
    self.container_storage["affichage"]["Mode Conduite"].add_object(
        Button(
            label="Eco",
            text="ECO",
            font_name="Roboto-Bold",
            font_size=18,
            icon_path=None,
            state="normal",
            size=(100,47),
            callback_action=callback_eco_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["affichage"].append(self.container_storage["affichage"]["Mode Conduite"].get_object("Eco")) 
    #bouton Normal
    self.container_storage["affichage"]["Mode Conduite"].add_object(
        Button(
            label="Normal",
            text="NORMAL",
            font_name="Roboto-Bold",
            font_size=18,
            icon_path=None,
            state="pressed",
            size=(100,47),
            callback_action=callback_normal_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["affichage"].append(self.container_storage["affichage"]["Mode Conduite"].get_object("Normal")) 
    #bouton Sport
    self.container_storage["affichage"]["Mode Conduite"].add_object(
        Button(
            label="Sport",
            text="SPORT",
            font_name="Roboto-Bold",
            font_size=18,
            icon_path=None,
            state="normal",
            size=(100,47),
            callback_action=callback_sport_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["affichage"].append(self.container_storage["affichage"]["Mode Conduite"].get_object("Sport")) 



    #--------------Container Activation Charge--------------#
    self.container_storage["affichage"]["Activation Charge"] = Container(
        label="Activation Charge",
        show_label=True,
        position=(401, 11),
        size=(147, 88),
        show=True,
        allignement="horizontal"
    )
    self.container_storage["affichage"]["Activation Charge"].add_object(
        Button(
            label="Charge",
            text="CHARGE",
            font_name="Roboto-Bold",
            font_size=18,
            icon_path=None,
            state="normal",
            size=(100,47),
            callback_action=callback_charge_button,
            auto_change_state=True,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["affichage"].append(self.container_storage["affichage"]["Activation Charge"].get_object("Charge")) 


    
    #--------------Container Bouton Choix Page--------------#
    self.container_storage["affichage"]["Bouton Choix Page"] = Container(
        label="Bouton Choix Page",
        show_label=False,
        position=(0, 396),
        size=(800, 84),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["affichage"]["Bouton Choix Page"].add_object(
        Button(
            label="Affichage",
            text="Affichage",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/affichage_{dark_light_mode["etat"]}.png",
            state="pressed",
            size=(247,68),
            callback_action=callback_affichage_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["affichage"].append(self.container_storage["affichage"]["Bouton Choix Page"].get_object("Affichage")) 
    self.container_storage["affichage"]["Bouton Choix Page"].add_object(
        Button(
            label="Navigation",
            text="Navigation",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/navigation_{dark_light_mode["etat"]}.png",
            state="normal",
            size=(247,68),
            callback_action=callback_navigation_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["affichage"].append(self.container_storage["affichage"]["Bouton Choix Page"].get_object("Navigation")) 
    self.container_storage["affichage"]["Bouton Choix Page"].add_object(
        Button(
            label="Système",
            text="Système",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/system_{dark_light_mode["etat"]}.png",
            state="normal",
            size=(247,68),
            callback_action=callback_systeme_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["affichage"].append(self.container_storage["affichage"]["Bouton Choix Page"].get_object("Système")) 


    
    #--------------Container Heure Wifi--------------#
    self.container_storage["affichage"]["Heure Wifi"] = Container(
        label="Heure Wifi",
        show_label=False,
        position=(562, 11),
        size=(216, 88),
        show=True,
        allignement="horizontal"
    )
    self.container_storage["affichage"]["Heure Wifi"].add_object(
        Image(
            label="Wifi",
            image_path="affichage/wifi.png",
            show=True,
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Heure Wifi"].add_object(
        Text(
            label="Heure",
            text="20:25",
            font_name="Roboto-Bold",
            font_size=35,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=None
    )


    
    #--------------Container Batterie--------------#
    self.container_storage["affichage"]["Batterie"] = Container(
        label="Batterie",
        show_label=True,
        position=(20, 115),
        size=(220, 205),
        show=True,
        allignement="horizontal"
    )
    self.container_storage["affichage"]["Batterie"].add_object(
        Text(
            label="Niveau",
            text="50",
            font_name="Roboto-Regular",
            font_size=30,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Batterie"].add_object(
        Image(
            label="Batterie Png",
            image_path="affichage/batterie.png",
            show=True,
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Batterie"].add_object(
        Text(
            label="Pourcentage",
            text="%",
            font_name="Roboto-Regular",
            font_size=20,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=(65, 95)
    )
    self.container_storage["affichage"]["Batterie"].add_object(
        Text(
            label="Niveau Text",
            text="Niveau",
            font_name="Roboto-Bold",
            font_size=17,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="center",
            show=True
        ),
        relative_position=(50, 120)
    )
    self.container_storage["affichage"]["Batterie"].add_object(
        Rectangle(
            label="Rectangle Batterie",
            size=(1,1),
            color=(0,0,0),
            border_radius=5,
            show=True
        ),
        relative_position=(0, 0)
    )


    
    #--------------Container Vitesse--------------#
    self.container_storage["affichage"]["Vitesse"] = Container(
        label="Vitesse",
        show_label=False,
        position=(240, 20),
        size=(322, 186),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["affichage"]["Vitesse"].add_object(
        Text(
            label="Vitesse",
            text="17",
            font_name="7-segment-bold",
            font_size=160,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Vitesse"].add_object(
        Text(
            label="Vitesse Unite",
            text="km/h",
            font_name="Roboto-Bold",
            font_size=25,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=(161, 240)
    )


    
    #--------------Container Temperature--------------#
    self.container_storage["affichage"]["Temperature"] = Container(
        label="Température",
        show_label=True,
        position=(562, 116),
        size=(216, 172),
        show=True,
        allignement="horizontal"
    )
    self.container_storage["affichage"]["Temperature"].add_object(
        Image(
            label="Temperature Png",
            image_path="affichage/temperature.png",
            show=True,
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Temperature"].add_object(
        Container(
            label="Temperature Container",
            show_label=False,
            position=(91, 15),
            size=(81, 135),
            show=False,
            allignement="vertical"
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Temperature"].get_object("Temperature Container").add_object(
        Text(
            label="Temperature Batterie",
            text="200",
            font_name="Roboto-Bold",
            font_size=35,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Temperature"].get_object("Temperature Container").add_object(
        Text(
            label="Temperature Batterie Text",
            text="Batterie",
            font_name="Roboto-Bold",
            font_size=17,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Temperature"].get_object("Temperature Container").add_object(
        Text(
            label="Temperature Moteur",
            text="20",
            font_name="Roboto-Bold",
            font_size=35,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Temperature"].get_object("Temperature Container").add_object(
        Text(
            label="Temperature Moteur Text",
            text="Moteur",
            font_name="Roboto-Bold",
            font_size=17,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Temperature"].add_object(
        Text(
            label="Temperature Batterie Unite",
            text="°C",
            font_name="Roboto-Bold",
            font_size=25,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=(182, 35)
    )
    self.container_storage["affichage"]["Temperature"].add_object(
        Text(
            label="Temperature Moteur Unite",
            text="°C",
            font_name="Roboto-Bold",
            font_size=25,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=(182, 100)
    )


    
    #--------------Container clignotant gauche--------------#
    self.container_storage["affichage"]["Clignotant Gauche"] = Container(
        label="Clignotant Gauche",
        show_label=False,
        position=(40, 331),
        size=(97, 65),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["affichage"]["Clignotant Gauche"].add_object(
        Image(
            label="Clignotant Gauche Allume",
            image_path="clignotant/clignotant_gauche_allume.png",
            show=False,
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=(0,0)
    )
    self.container_storage["affichage"]["Clignotant Gauche"].add_object(
        Image(
            label="Clignotant Gauche eteint",
            image_path="clignotant/clignotant_gauche_eteint.png",
            show=True,
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=(0,0)
    )


    
    #--------------Container clignotant droit--------------#
    self.container_storage["affichage"]["Clignotant Droit"] = Container(
        label="Clignotant Droit",
        show_label=False,
        position=(655, 331),
        size=(97, 65),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["affichage"]["Clignotant Droit"].add_object(
        Image(
            label="Clignotant Droit Allume",
            image_path="clignotant/clignotant_droit_allume.png",
            show=False,
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=(0,0)
    )
    self.container_storage["affichage"]["Clignotant Droit"].add_object(
        Image(
            label="Clignotant Droit eteint",
            image_path="clignotant/clignotant_droit_eteint.png",
            show=True,
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=(0,0)
    )


    
    #--------------Container Prevention--------------#
    self.container_storage["affichage"]["Prevention"] = Container(
        label="Prevention",
        show_label=False,
        position=(247, 290),
        size=(363, 110),
        show=False,
        allignement="vertical"
    )
    for i in range(3) :
        self.container_storage["affichage"]["Prevention"].add_object(
            Container(
                label=f"Prevention {(i+1)}",
                show_label=False,
                position=(247+i*30, 296),
                size=(363, 30),
                show=False,
                allignement="horizontal"
            ),
            relative_position=None
        )
        self.container_storage["affichage"]["Prevention"].get_object(f"Prevention {(i+1)}").add_object(
            Rectangle(
                label=f"Prevention {(i+1)} Rectangle",
                size=(363, 30),
                color=(251,44,44),
                border_radius=7,
                show=False
            ),
            relative_position=(0,0)
        )
        self.container_storage["affichage"]["Prevention"].get_object(f"Prevention {(i+1)}").add_object(
            Image(
                label=f"Prevention {(i+1)} icon",
                image_path="affichage/danger.png",
                show=False,
                callback_action=None,
                callback_mqtt_response=None
            ),
            relative_position=None
        )
        self.container_storage["affichage"]["Prevention"].get_object(f"Prevention {(i+1)}").add_object(
            Text(
                label=f"Prevention {(i+1)} icon",
                text="Attention moteur trop chaud !",
                font_name="Roboto-Bold",
                font_size=20,
                color=dark_light_mode["text"][dark_light_mode["etat"]],
                justify="left",
                show=False
            ),
            relative_position=None
        )








#__________________________________________________________________________________________#
#------------------------------------Navigation--------------------------------------------#
#__________________________________________________________________________________________#

    #--------------Container Background--------------#
    self.container_storage["navigation"]["Background"] = Container(
        label="Background",
        show_label=False,
        position=(-10, -10),
        size=(820, 500),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["navigation"]["Background"].add_object(
        Rectangle(
            label="Background Rectangle",
            size=(820, 480),
            color=dark_light_mode["background"][dark_light_mode["etat"]],
            border_radius=0,
            show=True
        ),
        relative_position=(0, 0)
    )
    #--------------Container Bouton Choix Page--------------#
    self.container_storage["navigation"]["Bouton Choix Page"] = Container(
        label="Bouton Choix Page",
        show_label=False,
        position=(0, 396),
        size=(800, 84),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["navigation"]["Bouton Choix Page"].add_object(
        Button(
            label="Affichage",
            text="Affichage",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/affichage_{dark_light_mode["etat"]}.png",
            state="pressed",
            size=(247,68),
            callback_action=callback_affichage_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["navigation"].append(self.container_storage["navigation"]["Bouton Choix Page"].get_object("Affichage")) 
    self.container_storage["navigation"]["Bouton Choix Page"].add_object(
        Button(
            label="Navigation",
            text="Navigation",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/navigation_{dark_light_mode["etat"]}.png",
            state="normal",
            size=(247,68),
            callback_action=callback_navigation_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["navigation"].append(self.container_storage["navigation"]["Bouton Choix Page"].get_object("Navigation")) 
    self.container_storage["navigation"]["Bouton Choix Page"].add_object(
        Button(
            label="Système",
            text="Système",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/system_{dark_light_mode["etat"]}.png",
            state="normal",
            size=(247,68),
            callback_action=callback_systeme_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["navigation"].append(self.container_storage["navigation"]["Bouton Choix Page"].get_object("Système")) 








#__________________________________________________________________________________________#
#------------------------------------Système--------------------------------------------#
#__________________________________________________________________________________________#

    #--------------Container Background--------------#
    self.container_storage["systeme"]["Background"] = Container(
        label="Background",
        show_label=False,
        position=(-10, -10),
        size=(820, 500),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["systeme"]["Background"].add_object(
        Rectangle(
            label="Background Rectangle",
            size=(820, 480),
            color=dark_light_mode["background"][dark_light_mode["etat"]],
            border_radius=0,
            show=True
        ),
        relative_position=(0, 0)
    )
    #--------------Container Bouton Choix Page--------------#
    self.container_storage["systeme"]["Bouton Choix Page"] = Container(
        label="Bouton Choix Page",
        show_label=False,
        position=(0, 396),
        size=(800, 84),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["systeme"]["Bouton Choix Page"].add_object(
        Button(
            label="Affichage",
            text="Affichage",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/affichage_{dark_light_mode["etat"]}.png",
            state="pressed",
            size=(247,68),
            callback_action=callback_affichage_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Bouton Choix Page"].get_object("Affichage")) 
    self.container_storage["systeme"]["Bouton Choix Page"].add_object(
        Button(
            label="Navigation",
            text="Navigation",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/navigation_{dark_light_mode["etat"]}.png",
            state="normal",
            size=(247,68),
            callback_action=callback_navigation_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Bouton Choix Page"].get_object("Navigation")) 
    self.container_storage["systeme"]["Bouton Choix Page"].add_object(
        Button(
            label="Système",
            text="Système",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/system_{dark_light_mode["etat"]}.png",
            state="normal",
            size=(247,68),
            callback_action=callback_systeme_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Bouton Choix Page"].get_object("Système")) 













