
from scripts.setup_draw import *
from module_import import *
from components import *
from config import *
from utils.utils import *

class Interface :
    def __init__(self):
        self.mqtt_thread_handler = None
        #initialisation pygame (interface graphique) 
        pygame.init()
        pygame.display.set_caption("Tableau de bord Kart") #changement du titre de la fenêtre
        if tactile : #si on est en mode ecran tactile
            pygame.mouse.set_visible(False) # à enlever pour voir la souris

        #Ouverture de la fenêtre Pygame
        self.largeur_ecran, self.hauteur_ecran = 800, 480
        self.window = pygame.display.set_mode((800,480)) #création d'une fenêtre en plein écran
        self.clock = pygame.time.Clock() #clock utile pour bloquer la boucle du jeu et limiter la vitesse de la boucle (même principe que sleep du module time)

        self.index = 0
        self.clickable_object = {
            "affichage" : [],
            "navigation" : [],
            "systeme" : []
        }
        self.container_storage = {
            "affichage" : {},
            "navigation" : {},
            "systeme" : {}
        }
        self.current_page = "affichage"

        #paramètrage
        self.format_heure = "24h"
        self.temperature_unite = "°C"

        #variable importé des autre partie du projet SAE
        self.vitesse = 17
        self.temperature_batterie = 170
        self.temperature_moteur = 175
        setup_draw(self)

    


    def draw(self) :
        for container in self.container_storage[self.current_page].values() :
            container.draw(self.window)


    def start(self) :
        while main_loop :
            self.index+=1
            self.event_window()
            #Limitation de vitesse de la boucle
            self.clock.tick(fps) 

            self.draw()

            self.periodic_test()


            #Rafraîchissement de l'écran
            pygame.display.flip()


    def periodic_test(self) :
        #test toute les secondes
        if self.index % fps == 0:
            update_heure(self)
        if self.index % (fps*10) == 0 :
            test_connection(self)
            self.index = 0


    def update_batterie(self, new_batterie) : 
        self.container_storage["affichage"]["Batterie"].get_object("Batterie Niveau Container").get_object("Niveau").text = f"{int(new_batterie*100)}"
        self.container_storage["affichage"]["Batterie"].get_object("Rectangle Batterie").color = hex_to_rgb(color_green_to_red[int((1-new_batterie)*len(color_green_to_red))])
        self.container_storage["affichage"]["Batterie"].get_object("Rectangle Batterie").position = (131, 150+int((1-new_batterie)*150))
        self.container_storage["affichage"]["Batterie"].get_object("Rectangle Batterie").kwargs["size"] = (73, int(new_batterie*150))
        self.container_storage["affichage"]["Batterie"].get_object("Batterie Niveau Container").reCalcule_position()
        self.container_storage["affichage"]["Batterie"].get_object("Batterie Niveau Container").reCalcule_position()
    
    def update_vitesse(self, new_vitesse) :
        self.container_storage["affichage"]["Vitesse"].get_object("Vitesse").text = str(new_vitesse)
        self.container_storage["navigation"]["Vitesse"].get_object("Vitesse").text = str(new_vitesse)

    def update_temperature_moteur(self, new_temperature_moteur) :
        self.container_storage["affichage"]["Temperature"].get_object("Temperature Container").get_object("Temperature Moteur").text = str(new_temperature_moteur)
        self.container_storage["affichage"]["Temperature"].reCalcule_position()
        self.container_storage["affichage"]["Temperature"].reCalcule_position()

    def update_temperature_batterie(self, new_temperature_batterie) :
        print(len(str(new_temperature_batterie)))
        self.container_storage["affichage"]["Temperature"].get_object("Temperature Container").get_object("Temperature Batterie").text = str(new_temperature_batterie)
        self.container_storage["affichage"]["Temperature"].reCalcule_position()
        self.container_storage["affichage"]["Temperature"].reCalcule_position()
                # #permet de tester toute les 10 secondes
                # if self.index >= fps*10 :
                #     if is_connected() :
                #         self.wifi_etat = True
                #     else :
                #         self.wifi_etat = False
                #     self.index = 0
                # if self.index%(fps//2) == 0 :
                #     changement_etat_clignotant(self)
                



            # #boucle d'affichage de l'onglet navigation
            # while navigation_loop :
            #     self.index+=1
            #     self.event_window()
            #     #Limitation de vitesse de la boucle
            #     self.clock.tick(fps) 

            #     #affichage des images
            #     self.window.blit(self.images["background_navigation_"+self.dark_mode["etat"]], (0,0)) #image du background
            #     affichage_clignotant(self)
            #     #affichage vitesse
            #     affichage_texte(self.window, f"{self.vitesse}", self.fonts["font_vitesse_navigation"], (388, 330), self.dark_mode["anti_color"])

            #     if self.index%(fps//2) == 0 :
            #         changement_etat_clignotant(self)
            #         self.index = 0
            #     #Rafraîchissement de l'écran
            #     pygame.display.flip()




            # #boucle d'affichage de l'onglet parametre
            # while systeme_loop :
            #     self.event_window()
            #     #Limitation de vitesse de la boucle
            #     self.clock.tick(fps) 
            #     #affichage des images
            #     self.window.blit(self.images["background_systeme_"+self.dark_mode["etat"]], (0,0)) #image du background
                
            #     #afichage des switchs
            #     for sw in switch_dict.values() :
            #         affichage_switch(self, sw["position"], sw["etat"], sw["position_x_rond"])
            #     if self.info_regulateur_limitateur["affichage"] :
            #         #affichage des boutçons plus et moins du limitateur et régulateur
            #         affichage_bouton_regulateur_limitateur(self)
            #         affichage_texte(self.window, f"{self.vitesse_consigne}", self.fonts["font_vitesse_consigne"], (570, 270), self.dark_mode["anti_color"])
            #     affichage_switch_3_etat(self, self.info_switch_3_etat_regulateur["position"], self.info_switch_3_etat_regulateur["etat"], self.info_switch_3_etat_regulateur["position_x_rond"])
            #     #Rafraîchissement de l'écran
            #     pygame.display.flip()






    def event_window(self) :
        global main_loop, affichage_loop, navigation_loop, systeme_loop
        #position de la sourie pour le clic
        X, Y = pygame.mouse.get_pos()

        #event du clavier/de la fenêtre
        keys = pygame.key.get_pressed() #on récupère tout les touches du clavier (keys[] = True si la touche est préssé)
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE] :     #Si on ferme le jeu, on sort des 2 boucles (principal et menu) ce qui ferme le jeu
                main_loop = False
                affichage_loop = False
                navigation_loop = False
                systeme_loop = False

            if event.type == MOUSEBUTTONDOWN : # fonctionnement avec souris
                for objt in self.clickable_object[self.current_page] :
                    objt.on_click((X, Y))
            elif event.type == MOUSEBUTTONUP : # fonctionnement avec souris
                for objt in self.clickable_object[self.current_page] :
                    objt.on_release((X, Y))
                


    def test_clic(self, x, y) :
        global main_loop, affichage_loop, navigation_loop, systeme_loop
        #test sur l'onglet affichage
        if affichage_loop :
            #test clic mode conduite
            for info_mode_item in info_mode_conduite.items() : #boucle pour les 3 boutons. La dernière condition est pour éviter d'envoyer un rechanger au même mode de conduite
                if info_mode_item[1] < x < info_mode_item[1] + 134 and 36 < y < 93 and self.mode_conduite != info_mode_item[0]:
                    self.mode_conduite = info_mode_item[0]
                    #permet d'envoyer l'information via mqtt
                    self.mqtt_thread_handler.add_message("moteur/mode", self.mode_conduite)
            #test clic clognotant gauche
            if 56 < x < 148 and 329 < y < 391 :
                self.clignotant_info = {"cligno" : 1, "etat" : True, "allume" : "gauche", "start" : int(time())}
                #permet d'envoyer l'information via mqtt
                self.mqtt_thread_handler.add_message("aide/clignotant", "ga")
            #test clic clognotant droit
            elif 655 < x < 752 and 329 < y < 391 :
                self.clignotant_info = {"cligno" : 1, "etat" : True, "allume" : "droite", "start" : int(time())} 
                #permet d'envoyer l'information via mqtt
                self.mqtt_thread_handler.add_message("aide/clignotant", "da")

        #si on est sur l'onglet navigation
        if navigation_loop :
            #test clic clognotant gauche
            if 56 < x < 148 and 329 < y < 391 :
                self.clignotant_info = {"cligno" : 1, "etat" : True, "allume" : "gauche", "start" : int(time())}
                #permet d'envoyer l'information via mqtt
                self.mqtt_thread_handler.add_message("aide/clignotant", "ga")
            #test clic clognotant droit
            elif 655 < x < 752 and 329 < y < 391 :
                self.clignotant_info = {"cligno" : 1, "etat" : True, "allume" : "droite", "start" : int(time())} 
                #permet d'envoyer l'information via mqtt
                self.mqtt_thread_handler.add_message("aide/clignotant", "da")

        #si on est sur l'onglet systeme
        if systeme_loop :
            for sw in switch_dict.items() :
                if sw[1]["position"][0] <= x <= sw[1]["position"][0] + 100 and sw[1]["position"][1] <= y <= sw[1]["position"][1] + 50:
                    sw[1]["etat"] = not sw[1]["etat"]
                    redirection_effet_bouton(self, sw)
            
            if self.info_switch_3_etat_regulateur["position"][0] < x < self.info_switch_3_etat_regulateur["position"][0] + 220//3 and self.info_switch_3_etat_regulateur["position"][1] < y < self.info_switch_3_etat_regulateur["position"][1] + 80 :
                self.info_switch_3_etat_regulateur["etat"] = "regulateur"
                self.info_regulateur_limitateur["affichage"] = True
                self.vitesse_consigne = self.vitesse
                #permet d'envoyer l'information via mqtt
                self.mqtt_thread_handler.add_message("aide/reg_lim", "ra") #on n'envoi pas la vitesse de consigne car à l'activation du mode, la vitesse de consigne est éguale à la vitesse
            elif self.info_switch_3_etat_regulateur["position"][0] + 220//3 < x < self.info_switch_3_etat_regulateur["position"][0] + 2*220//3 and self.info_switch_3_etat_regulateur["position"][1] < y < self.info_switch_3_etat_regulateur["position"][1] + 80 :
                self.info_switch_3_etat_regulateur["etat"] = "neutre"
                self.info_regulateur_limitateur["affichage"] = False
                #permet d'envoyer l'information via mqtt
                self.mqtt_thread_handler.add_message("aide/reg_lim", "e")
            elif self.info_switch_3_etat_regulateur["position"][0] + 2*220//3 < x < self.info_switch_3_etat_regulateur["position"][0] + 220 and self.info_switch_3_etat_regulateur["position"][1] < y < self.info_switch_3_etat_regulateur["position"][1] + 80 :
                self.info_switch_3_etat_regulateur["etat"] = "limitateur"
                self.info_regulateur_limitateur["affichage"] = True
                self.vitesse_consigne = self.vitesse
                #permet d'envoyer l'information via mqtt
                self.mqtt_thread_handler.add_message("aide/reg_lim", "la")
            
        

        #test clic pour les boutons toujours allumés en bas de l'ecran
        #clic bouton affichage
        if 0 < x < 272 and 403 < y < 470 and affichage_loop == False :
            affichage_loop = True
            navigation_loop = False
            systeme_loop = False
        #clic bouton navigation
        elif 273 < x < 526 and 403 < y < 470 and navigation_loop == False :
            affichage_loop = False
            navigation_loop = True
            systeme_loop = False
        #clic bouton parametre
        elif 527 < x < 800 and 403 < y < 470 and systeme_loop == False :
            affichage_loop = False
            navigation_loop = False
            systeme_loop = True
        

    def test_clic_bouton_regulateur_limitateur(self, event_type, x, y) :
        for signe in self.info_regulateur_limitateur["boutons"].items() :
            if signe[1]["etat"] == False and event_type == MOUSEBUTTONDOWN and signe[1]["position"][0] < x < signe[1]["position"][0]+88 and signe[1]["position"][1] < y < signe[1]["position"][1]+88:
                signe[1]["etat"] = True
            elif signe[1]["etat"] and event_type == MOUSEBUTTONUP :
                signe[1]["etat"] = False
                if signe[0] == "plus" and self.vitesse_consigne < VITESSE_MAX:
                    self.vitesse_consigne+=1
                elif signe[0] == "moins" and self.vitesse_consigne > 1 :
                    self.vitesse_consigne-=1
                #permet d'envoyer l'information via mqtt
                self.mqtt_thread_handler.add_message("aide/vitesse_consigne", f"{self.vitesse_consigne}")
