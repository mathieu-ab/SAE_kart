from module_import import *
from config import *
from callbacks import *
from components import *

#fonction qui va cree chaque objet à dessiner
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
        Shape(
            label="Background Rectangle",
            shape="rectangle",
            size=(820, 500),
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
            dark_light=False,
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
            dark_light=False,
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
            dark_light=False,
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
            text="CHARGE OFF",
            font_name="Roboto-Bold",
            font_size=18,
            icon_path=None,
            state="normal",
            size=(125,47),
            dark_light=False,
            callback_action=callback_charge_button,
            auto_change_state=False,
            self_Interface = self,
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
            font_size=25,
            icon_path=f"affichage/affichage_",
            state="pressed",
            size=(182,68),
            dark_light=True,
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
            label="Aide",
            text="Aide",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"affichage/system_",
            state="normal",
            size=(182,68),
            dark_light=True,
            callback_action=callback_aide_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["affichage"].append(self.container_storage["affichage"]["Bouton Choix Page"].get_object("Aide")) 
    self.container_storage["affichage"]["Bouton Choix Page"].add_object(
        Button(
            label="Navigation",
            text="Navigation",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"affichage/navigation_",
            state="normal",
            size=(182,68),
            dark_light=True,
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
            font_size=25,
            icon_path=f"affichage/system_",
            state="normal",
            size=(182,68),
            dark_light=True,
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
            image_path=f"affichage/wifi_",
            show=True,
            callback_action=None,
            dark_light=True
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Heure Wifi"].add_object(
        Text(
            label="Heure",
            text="9:25",
            font_name="Roboto-Bold",
            font_size=35,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Heure Wifi"].add_object(
        Text(
            label="PMAM",
            text="",
            font_name="Roboto-Bold",
            font_size=20,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=(170, 57)
    )
    self.container_storage["affichage"]["Heure Wifi"].add_object(
        Shape(
            label="Wifi Connected",
            shape="circle",
            color=(26, 237, 21),
            show=True,
            radius=4
        ),
        relative_position=(73, 59)
    )
    self.container_storage["affichage"]["Heure Wifi"].add_object(
        Shape(
            label="Wifi Not Connected 1",
            shape="line",
            color=(255,40,40),
            show=False,
            end_pos=(10, 10),
            width=3
        ),
        relative_position=(68, 54)
    )
    self.container_storage["affichage"]["Heure Wifi"].add_object(
        Shape(
            label="Wifi Not Connected 2",
            shape="line",
            color=(255,40,40),
            show=False,
            end_pos=(10, -10),
            width=3
        ),
        relative_position=(68, 64)
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
        Container(
        label="Batterie Niveau Container",
        show_label=False,
        position=(0, 0),
        size=(73, 50),
        show=False,
        allignement="horizontal"
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Batterie"].get_object("Batterie Niveau Container").add_object(
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
    self.container_storage["affichage"]["Batterie"].get_object("Batterie Niveau Container").add_object(
        Text(
            label="Pourcentage",
            text="%",
            font_name="Roboto-Regular",
            font_size=20,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=None
    )
    self.container_storage["affichage"]["Batterie"].add_object(
        Image(
            label="Batterie Png",
            image_path=f"affichage/batterie_",
            show=True,
            callback_action=None,
            dark_light=True
        ),
        relative_position=(100, 13)
    )
    self.container_storage["affichage"]["Batterie"].add_object(
        Image(
            label="Batterie Png",
            image_path=f"affichage/batterie_",
            show=False,
            callback_action=None,
            dark_light=True
        ),
        relative_position=None
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
        Shape(
            label="Rectangle Batterie",
            shape="rectangle",
            size=(0,0),
            color=(0,255,0),
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
        relative_position=(161, 245)
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
            image_path=f"affichage/temperature_",
            show=True,
            callback_action=None,
            dark_light=True
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
            label="Clignotant Gauche eteint",
            image_path="clignotant/clignotant_gauche_eteint",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(0,0)
    )
    self.container_storage["affichage"]["Clignotant Gauche"].add_object(
        Image(
            label="Clignotant Gauche Allume",
            image_path="clignotant/clignotant_gauche_allume",
            show=False,
            callback_action=None,
            dark_light=False
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
            label="Clignotant Droit eteint",
            image_path="clignotant/clignotant_droit_eteint",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(0,0)
    )
    self.container_storage["affichage"]["Clignotant Droit"].add_object(
        Image(
            label="Clignotant Droit Allume",
            image_path="clignotant/clignotant_droit_allume",
            show=False,
            callback_action=None,
            dark_light=False
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
                label=f"Prevention {i}",
                show_label=False,
                position=(247+i*30, 296),
                size=(363, 30),
                show=False,
                allignement="horizontal"
            ),
            relative_position=None
        )
        self.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").add_object(
            Shape(
                label=f"Prevention {i} Rectangle",
                shape="rectangle",
                size=(363, 30),
                color=(251,44,44),
                border_radius=7,
                show=False
            ),
            relative_position=(0,0)
        )
        self.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").add_object(
            Image(
                label=f"Prevention {i} icon",
                image_path="affichage/danger",
                show=False,
                callback_action=None,
                dark_light=False
            ),
            relative_position=None
        )
        self.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").add_object(
            Text(
                label=f"Prevention {i} text",
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
#------------------------------------Aide--------------------------------------------#
#__________________________________________________________________________________________#

    #--------------Container Background--------------#
    self.container_storage["aide"]["Background"] = Container(
        label="Background",
        show_label=False,
        position=(-10, -10),
        size=(820, 500),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["aide"]["Background"].add_object(
        Shape(
            label="Background Rectangle",
            shape="rectangle",
            size=(820, 500),
            color=dark_light_mode["background"][dark_light_mode["etat"]],
            border_radius=0,
            show=True
        ),
        relative_position=(0, 0)
    )
    #--------------Container Bouton Choix Page--------------#
    self.container_storage["aide"]["Bouton Choix Page"] = Container(
        label="Bouton Choix Page",
        show_label=False,
        position=(0, 396),
        size=(800, 84),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["aide"]["Bouton Choix Page"].add_object(
        Button(
            label="Affichage",
            text="Affichage",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"affichage/affichage_",
            state="normal",
            size=(182,68),
            dark_light=True,
            callback_action=callback_affichage_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["aide"].append(self.container_storage["aide"]["Bouton Choix Page"].get_object("Affichage")) 
    self.container_storage["aide"]["Bouton Choix Page"].add_object(
        Button(
            label="Aide",
            text="Aide",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"affichage/system_",
            state="pressed",
            size=(182,68),
            dark_light=True,
            callback_action=callback_aide_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["aide"].append(self.container_storage["aide"]["Bouton Choix Page"].get_object("Aide")) 
    self.container_storage["aide"]["Bouton Choix Page"].add_object(
        Button(
            label="Navigation",
            text="Navigation",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"affichage/navigation_",
            state="normal",
            size=(182,68),
            dark_light=True,
            callback_action=callback_navigation_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["aide"].append(self.container_storage["aide"]["Bouton Choix Page"].get_object("Navigation")) 
    self.container_storage["aide"]["Bouton Choix Page"].add_object(
        Button(
            label="Système",
            text="Système",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"affichage/system_",
            state="normal",
            size=(182,68),
            dark_light=True,
            callback_action=callback_systeme_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["aide"].append(self.container_storage["aide"]["Bouton Choix Page"].get_object("Système")) 

    self.container_storage["aide"]["Nav Radar"] = Container(
        label="Nav Radar",
        show_label=False,
        position=(20, 20),
        size=(750, 360),
        show=False,
        allignement="horizontal"
    )

    self.container_storage["aide"]["Nav Radar"].add_object(
        Container(
            label="radar",
            show_label=False,
            position=(20, 20),
            size=(300, 350),
            show=True,
            allignement="horizontal"
        ),
        relative_position=None
    )
    self.container_storage["aide"]["Nav Radar"].add_object(
        Image(
            label="Radar Img",
            image_path="navigation/radar2",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(15,10)
    )
    self.container_storage["aide"]["Nav Radar"].get_object("Radar Img").set_size((290, 340))
     
    self.container_storage["aide"]["Nav Radar"].add_object(
        Image(
            label="Obstacle Gauche Arc 1",
            image_path="navigation/obstacle",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(60,53)
    )
    self.container_storage["aide"]["Nav Radar"].get_object("Obstacle Gauche Arc 1").set_size((45, 46)) 
    
    self.container_storage["aide"]["Nav Radar"].add_object(
        Image(
            label="Obstacle Gauche Arc M",
            image_path="navigation/bar",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(135,57)
    )
    self.container_storage["aide"]["Nav Radar"].get_object("Obstacle Gauche Arc M").set_size((45, 7)) 
    
    self.container_storage["aide"]["Nav Radar"].add_object(
        Image(
            label="Obstacle Gauche Arc D",
            image_path="navigation/obstacler",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(215,53)
    )
    self.container_storage["aide"]["Nav Radar"].get_object("Obstacle Gauche Arc D").set_size((45, 46)) 
    
    self.container_storage["aide"]["Nav Radar"].add_object(
        Image(
            label="Obstacle Gauche Arc 2",
            image_path="navigation/obstacle",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(45,35)
    )
    self.container_storage["aide"]["Nav Radar"].get_object("Obstacle Gauche Arc 2").set_size((45, 46))
    
    self.container_storage["aide"]["Nav Radar"].add_object(
        Image(
            label="Obstacle Gauche Arc DD",
            image_path="navigation/obstacler",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(230,35)
    )
    self.container_storage["aide"]["Nav Radar"].get_object("Obstacle Gauche Arc DD").set_size((45, 46))
    
     
    
    self.container_storage["aide"]["Nav Radar"].add_object(
        Image(
            label="Obstacle Gauche Arc 3",
            image_path="navigation/obstacle",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(25,17)
    )
    self.container_storage["aide"]["Nav Radar"].get_object("Obstacle Gauche Arc 3").set_size((45, 46))
    
    self.container_storage["aide"]["Nav Radar"].add_object(
        Image(
            label="Obstacle Gauche Arc DDD",
            image_path="navigation/obstacler",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(247,17)
    )
    self.container_storage["aide"]["Nav Radar"].get_object("Obstacle Gauche Arc DDD").set_size((45, 46))
     
    
    self.container_storage["aide"]["Nav Radar"].add_object(
        Container(
            label="nav autre",
            show_label=False,
            position=(320, 20),
            size=(420, 350),
            show=True,
            allignement="horizontal"
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
        Shape(
            label="Background Rectangle",
            shape="rectangle",
            size=(820, 500),
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
            font_size=25,
            icon_path=f"affichage/affichage_",
            state="normal",
            size=(182,68),
            dark_light=True,
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
            label="Aide",
            text="Aide",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"affichage/system_",
            state="pressed",
            size=(182,68),
            dark_light=True,
            callback_action=callback_aide_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["navigation"].append(self.container_storage["navigation"]["Bouton Choix Page"].get_object("Aide")) 
    self.container_storage["navigation"]["Bouton Choix Page"].add_object(
        Button(
            label="Navigation",
            text="Navigation",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"affichage/navigation_",
            state="normal",
            size=(182,68),
            dark_light=True,
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
            font_size=25,
            icon_path=f"affichage/system_",
            state="normal",
            size=(182,68),
            dark_light=True,
            callback_action=callback_systeme_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["navigation"].append(self.container_storage["navigation"]["Bouton Choix Page"].get_object("Système")) 




    #--------------Container clignotant gauche--------------#
    self.container_storage["navigation"]["Clignotant Gauche"] = Container(
        label="Clignotant Gauche",
        show_label=False,
        position=(40, 331),
        size=(97, 65),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["navigation"]["Clignotant Gauche"].add_object(
        Image(
            label="Clignotant Gauche Allume",
            image_path="clignotant/clignotant_gauche_allume",
            show=False,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(0,0)
    )
    self.container_storage["navigation"]["Clignotant Gauche"].add_object(
        Image(
            label="Clignotant Gauche eteint",
            image_path="clignotant/clignotant_gauche_eteint",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(0,0)
    )
    #--------------Container clignotant droit--------------#
    self.container_storage["navigation"]["Clignotant Droit"] = Container(
        label="Clignotant Droit",
        show_label=False,
        position=(655, 331),
        size=(97, 65),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["navigation"]["Clignotant Droit"].add_object(
        Image(
            label="Clignotant Droit Allume",
            image_path="clignotant/clignotant_droit_allume",
            show=False,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(0,0)
    )
    self.container_storage["navigation"]["Clignotant Droit"].add_object(
        Image(
            label="Clignotant Droit eteint",
            image_path="clignotant/clignotant_droit_eteint",
            show=True,
            callback_action=None,
            dark_light=False
        ),
        relative_position=(0,0)
    )
    #--------------Container gps--------------#
    self.container_storage["navigation"]["Gps"] = Container(
        label="Gps",
        show_label=False,
        position=(20, 20),
        size=(760, 290),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["navigation"]["Gps"].add_object(
        Container(
            label="Option Nav",
            show_label=False,
            position=(20, 20),
            size=(280, 290),
            show=True,
            allignement="vertical"
        ),
        relative_position=None
    )
    self.container_storage["navigation"]["Gps"].get_object("Option Nav").add_object(
        Image(
            label="Bouton Moins Nav",
            image_path="systeme/normal_moins",
            show=True,
            callback_action=callback_nav_moins,
            dark_light=False,
            self_Interface=self
        ),
        relative_position=None
    )
    self.clickable_object["navigation"].append(self.container_storage["navigation"]["Gps"].get_object("Option Nav").get_object("Bouton Moins Nav")) 
    self.container_storage["navigation"]["Gps"].get_object("Option Nav").add_object(
        Image(
            label="Bouton Plus Nav",
            image_path="systeme/normal_plus",
            show=True,
            callback_action=callback_nav_plus,
            dark_light=False,
            self_Interface=self
        ),
        relative_position=None
    )
    self.clickable_object["navigation"].append(self.container_storage["navigation"]["Gps"].get_object("Option Nav").get_object("Bouton Plus Nav")) 
    self.container_storage["navigation"]["Gps"].get_object("Option Nav").add_object(
        Button(
            label="Destination",
            text="Destination",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"navigation/destination_",
            state="normal",
            size=(200,68),
            dark_light=True,
            callback_action=callback_destination,
            auto_change_state=True,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["navigation"].append(self.container_storage["navigation"]["Gps"].get_object("Option Nav").get_object("Destination")) 

    self.container_storage["navigation"]["Gps"].add_object(
        Image(
            label="Image Nav",
            image_path="systeme/normal_moins", #image random pour pouvoir changer l'image plsu tard car celle ci n'est pas dans le répertoire assets/images
            show=True,
            callback_action=None,
            dark_light=False,
            self_Interface=self
        ),
        relative_position=None
    )
    self.container_storage["navigation"]["Gps"].get_object("Image Nav").set_absolute_path(CURRENT_PATH[:-25]+"/GPS/map.png")
    self.container_storage["navigation"]["Gps"].get_object("Image Nav").set_size((435,290))
    self.container_storage["navigation"]["Gps"].reCalcule_position()


    # Définition des rangées de touches du clavier AZERTY
    # keys = [
    #     ["A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P"],
    #     ["Q", "S", "D", "F", "G", "H", "J", "K", "L", "M"],
    #     ["W", "X", "C", "V", "B", "N"]
    # ]

    # # Création des containers pour chaque ligne
    # for row_index, row in enumerate(keys):
    #     row_container = Container(
    #         label=f"Row_{row_index}",
    #         show_label=False,
    #         position=(0, row_index * 60+10),
    #         size=(760, 45),
    #         show=False,
    #         allignement="horizontal"
    #     )
        
    #     for key in row:
    #         button = Button(
    #             label=key,
    #             text=key,
    #             font_name="Roboto-Bold",
    #             font_size=25,
    #             icon_path=None,
    #             state="normal",
    #             size=(63, 63),
    #             dark_light=True,
    #             callback_action=callback_key_press,
    #             auto_change_state=True,
    #             self_Interface=self,
    #             key=key  # Passage de la touche au callback
    #         )
    #         row_container.add_object(button, relative_position=None)
    #         self.clickable_object["navigation"].append(button)
        
    #     self.container_storage["navigation"]["Keyboard"].add_object(row_container, relative_position=None)
    # #ajout espace et back
    # button = Button(
    #     label="Espace",
    #     text="Space",
    #     font_name="Roboto-Bold",
    #     font_size=25,
    #     icon_path=None,
    #     state="normal",
    #     size=(100, 63),
    #     dark_light=True,
    #     callback_action=callback_key_press,
    #     auto_change_state=True,
    #     self_Interface=self,
    #     key=" "  # Passage de la touche au callback
    # )
    # row_container.add_object(button, relative_position=None)
    # self.clickable_object["navigation"].append(button)

    # button = Button(
    #     label="Backspace",
    #     text="Backspace",
    #     font_name="Roboto-Bold",
    #     font_size=25,
    #     icon_path=None,
    #     state="normal",
    #     size=(130, 63),
    #     dark_light=True,
    #     callback_action=callback_key_press,
    #     auto_change_state=True,
    #     self_Interface=self,
    #     key="Backspace"  # Passage de la touche au callback
    # )
    # row_container.add_object(button, relative_position=None)
    # self.clickable_object["navigation"].append(button)
    
    #--------------Container Vitesse--------------#
    self.container_storage["navigation"]["Vitesse"] = Container(
        label="Vitesse",
        show_label=False,
        position=(0, 245),
        size=(800, 149),
        show=False,
        allignement="horizontal"
    )
    self.container_storage["navigation"]["Vitesse"].add_object(
        Text(
            label="Vitesse",
            text="17",
            font_name="7-segment-bold",
            font_size=80,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=None
    )
    self.container_storage["navigation"]["Vitesse"].add_object(
        Text(
            label="Vitesse Unite",
            text="km/h",
            font_name="Roboto-Bold",
            font_size=20,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True
        ),
        relative_position=(470, 128)
    )
    #clavier virtuel
    self.container_storage["navigation"]["Keyboard"] = Container(
        label="Keyboard",
        show_label=False,
        position=(-10, -10), 
        size=(820, 500),
        show=False,
        allignement="vertical"
    )
    #texte écrit par le clavier
    self.container_storage["navigation"]["Keyboard"].add_object(
        Text(
            label="Text keyboard",
            text="Troyes",
            font_name="Roboto-Bold",
            font_size=37,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=False
        ),
        relative_position=None
    )
    self.container_storage["navigation"]["Keyboard"].get_object("Text keyboard").set_position((30, 40))


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
        Shape(
            label="Background Rectangle",
            shape="rectangle",
            size=(820, 500),
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
            font_size=25,
            icon_path=f"affichage/affichage_",
            state="normal",
            size=(182,68),
            dark_light=True,
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
            label="Aide",
            text="Aide",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"affichage/system_",
            state="pressed",
            size=(182,68),
            dark_light=True,
            callback_action=callback_aide_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Bouton Choix Page"].get_object("Aide")) 
    self.container_storage["systeme"]["Bouton Choix Page"].add_object(
        Button(
            label="Navigation",
            text="Navigation",
            font_name="Roboto-Bold",
            font_size=25,
            icon_path=f"affichage/navigation_",
            state="normal",
            size=(182,68),
            dark_light=True,
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
            font_size=25,
            icon_path=f"affichage/system_",
            state="normal",
            size=(182,68),
            dark_light=True,
            callback_action=callback_systeme_button,
            auto_change_state=False,
            self_Interface = self
        ),
        relative_position=None
    )
    #ajout de l'objet bouton au objet clickable
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Bouton Choix Page"].get_object("Système")) 

    
    #--------------Container Aide Conduite--------------#
    self.container_storage["systeme"]["Aide Conduite"] = Container(
        label="Aide Conduite",
        show_label=False,
        position=(20, 10),
        size=(373, 215),
        show=True,
        allignement="horizontal"
    )
    self.container_storage["systeme"]["Aide Conduite"].add_object(
        Container(
            label="Aide Conduite Text",
            show_label=False,
            position=(0, 0),
            size=(246, 215),
            show=False,
            allignement="vertical"
        ), 
        relative_position=None
    )
    self.container_storage["systeme"]["Aide Conduite"].add_object(
        Container(
            label="Aide Conduite Switch",
            show_label=False,
            position=(0, 0),
            size=(126, 215),
            show=False,
            allignement="vertical"
        ), 
        relative_position=None
    )
    
    for sw_text in ["Detection ligne blanche", "Detection obstacle", "Endormissement"] :
        self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Text").add_object(
                    Text(
                label=f"{sw_text} Text",
                text=sw_text,
                font_name="Roboto-Bold",
                font_size=20,
                color=dark_light_mode["text"][dark_light_mode["etat"]],
                justify="left",
                show=True
            ),
            relative_position=None
        )
    self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").add_object(
        Switch(
            label=f"Switch Detection ligne blanche",
            show=True,
            callback_action=callback_detection_ligne_switch,
            self_Interface=self
        ),
        relative_position=None
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").get_object(f"Switch Detection ligne blanche")) 
    self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").add_object(
        Switch(
            label=f"Switch Detection obstacle",
            show=True,
            callback_action=callback_detection_obstacle_switch,
            self_Interface=self
        ),
        relative_position=None
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").get_object(f"Switch Detection obstacle")) 
    self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").add_object(
        Switch(
            label=f"Switch Endormissement",
            show=True,
            callback_action=callback_endormissement_switch,
            self_Interface=self
        ),
        relative_position=None
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Aide Conduite"].get_object("Aide Conduite Switch").get_object(f"Switch Endormissement")) 






    #--------------Container Autre Parametre--------------#
    self.container_storage["systeme"]["Autre Parametre"] = Container(
        label="Autre Parametre",
        show_label=False,
        position=(407, 10),
        size=(373, 215),
        show=True,
        allignement="horizontal"
    )
    self.container_storage["systeme"]["Autre Parametre"].add_object(
        Container(
            label="Autre Parametre Text Left",
            show_label=False,
            position=(0, 0),
            size=(164, 215),
            show=False,
            allignement="vertical"
        ), 
        relative_position=None
    )
    self.container_storage["systeme"]["Autre Parametre"].add_object(
        Container(
            label="Autre Parametre Switch",
            show_label=False,
            position=(0, 0),
            size=(84, 215),
            show=False,
            allignement="vertical"
        ), 
        relative_position=None
    )
    self.container_storage["systeme"]["Autre Parametre"].add_object(
        Container(
            label="Autre Parametre Text Right",
            show_label=False,
            position=(0, 0),
            size=(164, 215),
            show=False,
            allignement="vertical"
        ), 
        relative_position=None
    )

    for sw_text in [["24h", "12h"], ["°C", "°F"], ["dark mode", "light mode"], ["", ""]] :
        self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Text Left").add_object(
                    Text(
                label=f"{sw_text[0]} Text",
                text=sw_text[0],
                font_name="Roboto-Bold",
                font_size=20,
                color=dark_light_mode["text"][dark_light_mode["etat"]],
                justify="left",
                show=True
            ),
            relative_position=None
        )
        self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Text Right").add_object(
                    Text(
                label=f"{sw_text[1]} Text",
                text=sw_text[1],
                font_name="Roboto-Bold",
                font_size=20,
                color=dark_light_mode["text"][dark_light_mode["etat"]],
                justify="left",
                show=True
            ),
            relative_position=None
        )

    self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").add_object(
        Switch(
            label=f"Switch 24h",
            show=True,
            callback_action=callback_1224h_switch,
            self_Interface=self
        ),
        relative_position=None
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object(f"Switch 24h")) 
    self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").add_object(
        Switch(
            label=f"Switch °C",
            show=True,
            callback_action=callback_temperature_unite_switch,
            self_Interface=self
        ),
        relative_position=None
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object(f"Switch °C")) 
    #switch non fonctionnel mais peux important. Mis sur la touche pour l'instant
    self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").add_object(
        Switch(
            label=f"Switch dark mode",
            show=True,
            callback_action=callback_dark_liht_switch,
            self_Interface=self
        ),
        relative_position=None
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object(f"Switch dark mode")) 
    
    #bouton temporaire pour tester la caméras de recule
    self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").add_object(
        Button(
            label="Caméra de Recul",
            text="Caméra de Recul",
            font_name="Roboto-Bold",
            font_size=20,
            icon_path=None,
            state="normal",
            size=(180,50),
            dark_light=False,
            callback_action=callback_cameras_recule,
            auto_change_state=True,
        ),
        relative_position=None
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Autre Parametre"].get_object("Autre Parametre Switch").get_object(f"Caméra de Recul"))



    #--------------Container Regulateur--------------#
    self.container_storage["systeme"]["Regulateur"] = Container(
        label="Regulateur",
        show_label=False,
        position=(20, 236),
        size=(760, 153),
        show=True,
        allignement="horizontal"
    )
    self.container_storage["systeme"]["Regulateur"].add_object(
        Container(
            label="Switch Limitateur Regulateur Container",
            show_label=False,
            position=(0, 0),
            size=(216, 67),
            show=False,
            allignement="horizontal"
        ), 
        relative_position=None
    )
    self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").add_object(
        Image(
            label="Switch Reg",
            image_path="systeme/switch_neutre",
            show=True,
            callback_action=callback_reg_switch,
            dark_light=False,
            self_Interface=self
        ),
        relative_position=(0,0)
    )
    self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").get_object("Switch Reg").size = (72, 68)
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").get_object("Switch Reg")) 
    self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").add_object(
        Image(
            label="Switch Neutre",
            image_path="systeme/vide",
            show=True,
            callback_action=callback_neutre_witch,
            dark_light=False,
            self_Interface=self
        ),
        relative_position=(72,0)
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").get_object("Switch Neutre"))
    self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").add_object(
        Image(
            label="Switch Lim",
            image_path="systeme/vide",
            show=True,
            callback_action=callback_lim_switch,
            dark_light=False,
            self_Interface=self
        ),
        relative_position=(144,0)
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Regulateur"].get_object("Switch Limitateur Regulateur Container").get_object("Switch Lim"))
    self.container_storage["systeme"]["Regulateur"].add_object(
        Image(
            label="Bouton Moins",
            image_path="systeme/normal_moins",
            show=False,
            callback_action=callback_reg_lim_moins,
            dark_light=False,
            self_Interface=self
        ),
        relative_position=None
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Regulateur"].get_object("Bouton Moins")) 
    self.container_storage["systeme"]["Regulateur"].add_object(
        Text(
            label="Vitesse Consigne",
            text=self.vitesse,
            font_name="7-segment-bold",
            font_size=110,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=False,
            vitesse_consigne=self.vitesse
        ),
        relative_position=(430, -85)
    )
    self.container_storage["systeme"]["Regulateur"].add_object(
        Text(
            label="Vitesse Consigne Copie",
            text=self.vitesse,
            font_name="7-segment-bold",
            font_size=110,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=False,
        ),
        relative_position=None
    )
    self.container_storage["systeme"]["Regulateur"].add_object(
        Image(
            label="Bouton Plus",
            image_path="systeme/normal_plus",
            show=False,
            callback_action=callback_reg_lim_plus,
            dark_light=False,
            self_Interface=self
        ),
        relative_position=None
    )
    self.clickable_object["systeme"].append(self.container_storage["systeme"]["Regulateur"].get_object("Bouton Plus")) 
    self.container_storage["systeme"]["Regulateur"].add_object(
        Text(
            label="Neutre Text",
            text="neutre",
            font_name="Roboto-Bold",
            font_size=15,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True,
        ),
        relative_position=(135, 120)
    )
    self.container_storage["systeme"]["Regulateur"].add_object(
        Text(
            label="Limitateur Text",
            text="regulateur",
            font_name="Roboto-Bold",
            font_size=15,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True,
        ),
        relative_position=(25, 15)
    )
    self.container_storage["systeme"]["Regulateur"].add_object(
        Text(
            label="Regulateur Text",
            text="limitateur",
            font_name="Roboto-Bold",
            font_size=15,
            color=dark_light_mode["text"][dark_light_mode["etat"]],
            justify="left",
            show=True,
        ),
        relative_position=(210, 15)
    )









