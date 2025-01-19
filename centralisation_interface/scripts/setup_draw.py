from module_import import *
from config import *
from components import Container
from components import Button
from components import Text
from components import Image



def setup_draw(self) :
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
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=None
    )
    #bouton Normal
    self.container_storage["affichage"]["Mode Conduite"].add_object(
        Button(
            label="Normal",
            text="NORMAL",
            font_name="Roboto-Bold",
            font_size=18,
            icon_path=None,
            state="normal",
            size=(100,47),
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=None
    )
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
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=None
    )



    #--------------Container Mode Conduite--------------#
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
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=None
    )


    
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
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Bouton Choix Page"].add_object(
        Button(
            label="Navigation",
            text="Navigation",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/navigation_{dark_light_mode["etat"]}.png",
            state="normal",
            size=(247,68),
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Bouton Choix Page"].add_object(
        Button(
            label="System",
            text="System",
            font_name="Roboto-Bold",
            font_size=35,
            icon_path=f"affichage/system_{dark_light_mode["etat"]}.png",
            state="normal",
            size=(247,68),
            callback_action=None,
            callback_mqtt_response=None
        ),
        relative_position=None
    )


    
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
            image_path="/affichage/wifi.png",
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
            justify="left"
        ),
        relative_position=None
    )