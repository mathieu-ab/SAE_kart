from scripts.fonctions import *
from scripts.import_variable import *


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
        self.images = {} #dictionnaire qui va contenir les objects des images
        self.fonts = {} #dictionnaire qui va contenir les objects des images

        #importation des images
        #images des backgrounds dark mode
        self.images["background_affichage_dark"] = import_image("/assets/images/affichage/background_affichage_dark.png")
        self.images["background_navigation_dark"] = import_image("/assets/images/navigation/background_navigation_dark.png")
        self.images["background_systeme_dark"] = import_image("/assets/images/systeme/background_systeme_dark.png")
        #images des backgrounds light mode
        self.images["background_affichage_light"] = import_image("/assets/images/affichage/background_affichage_light.png")
        self.images["background_navigation_light"] = import_image("/assets/images/navigation/background_navigation_light.png")
        self.images["background_systeme_light"] = import_image("/assets/images/systeme/background_systeme_light.png")
        #image des clignotant
        self.images["clignotant_droit_eteint_droit"] = import_image("/assets/images/clignotant/clignotant_droit_eteint.png")
        self.images["clignotant_droit_allume_droit"] = import_image("/assets/images/clignotant/clignotant_droit_allume.png")
        self.images["clignotant_droit_eteint_gauche"] = pygame.transform.rotate(self.images["clignotant_droit_eteint_droit"], 180)
        self.images["clignotant_droit_allume_gauche"] = pygame.transform.rotate(self.images["clignotant_droit_allume_droit"], 180)
        #images des + et moins du régulateur liitateur
        self.images["default_plus"] = import_image("/assets/images/systeme/default_plus.png")
        self.images["default_moins"] = import_image("/assets/images/systeme/default_moins.png")
        self.images["pressed_moins"] = import_image("/assets/images/systeme/pressed_moins.png")
        self.images["pressed_plus"] = import_image("/assets/images/systeme/pressed_plus.png")
        #bg rectangle rouge + icon message de prevention
        self.images["bg_prevention"] = import_image("/assets/images/affichage/bg_prevention.png")    

        #importation des fonts
        self.fonts["font_normal"] = import_font("/assets/fonts/Roboto-Bold.ttf", 33)
        self.fonts["font_mode_conduite"] = import_font("/assets/fonts/Roboto-Bold.ttf", 24)
        self.fonts["font_nombres"] = import_font("/assets/fonts/Roboto-Bold.ttf", 50)
        self.fonts["font_prevention"] = import_font("/assets/fonts/Roboto-Bold.ttf", 20)
        self.fonts["font_vitesse"] = import_font("/assets/fonts/7-segment-bold.ttf", 160)
        self.fonts["font_vitesse_consigne"] = import_font("/assets/fonts/7-segment-bold.ttf", 110)
        self.fonts["font_vitesse_navigation"] = import_font("/assets/fonts/7-segment-bold.ttf", 70)

        self.dark_mode = {"etat" : "dark", "color" : (0,0,0), "anti_color" : (255,255,255)}
        self.clignotant_info = {"cligno" : 1, "etat" : False, "allume" : None, "start" : None} #allume deviens "droite" ou "gauche" quand un clignotant est allumé. Sinon il reste en None
        self.index = 0
        self.vitesse_consigne = 0
        self.info_switch_3_etat_regulateur = {"etat" : "neutre", "position" : (80, 280), "position_x_rond" : [148]} #etat possible ["regulateur", "neutre", "limitateur"]
        #information pour les boutons de régulateur pour savoir quand un bouton est appuyé ou non
        self.info_regulateur_limitateur = {"boutons" : {
                "plus" : {
                    "etat" : False,
                    "position" : (670, 277)},
                "moins" : {
                    "etat" : False,
                    "position" : (363, 277)}
            },
            "affichage" : False}
        #variable des parametres
        self.format_heure = "24h"
        self.temperature_unite = "°C"

        #variable importé des autre partie du projet SAE
        self.vitesse = 17
        self.wifi_etat = True #true = connecté
        self.mode_conduite = "normal"
        self.temperature_batterie = 70
        self.temperature_moteur = 175
        self.batterie = 0.25



    def start(self) :
        while main_loop :
            while affichage_loop : #boucle du menu
                self.index+=1
                self.event_window()
                #Limitation de vitesse de la boucle
                self.clock.tick(fps) 

                #affichage des images
                self.window.blit(self.images["background_affichage_"+self.dark_mode["etat"]], (0,0)) #image du background
                affichage_etat_wifi(self)
                affichage_mode_conduite(self)
                affichage_batterie(self)
                affichage_clignotant(self)
                affichage_prevention(self)
               
                #affichage des textes
                affichage_heure(self)
                #affichage vitesse
                affichage_texte(self.window, f"{self.vitesse}", self.fonts["font_vitesse"], (380, 113), self.dark_mode["anti_color"])
                #affichage temperature batterie
                affichage_texte(self.window, f"{test_convertion_Celsius_to_Fahrenheit(self.temperature_batterie, self.temperature_unite)}", self.fonts["font_nombres"], (685, 170), self.dark_mode["anti_color"])
                affichage_texte(self.window, f"{self.temperature_unite}", self.fonts["font_normal"], (745, 170), self.dark_mode["anti_color"])
                #affichage temperature moteur
                affichage_texte(self.window, f"{test_convertion_Celsius_to_Fahrenheit(self.temperature_moteur, self.temperature_unite)}", self.fonts["font_nombres"], (685, 240), self.dark_mode["anti_color"])
                affichage_texte(self.window, f"{self.temperature_unite}", self.fonts["font_normal"], (745, 250), self.dark_mode["anti_color"])
                #affichage mode conduite texte
                affichage_texte(self.window, f"ECO", self.fonts["font_mode_conduite"], (92, 65), self.dark_mode["anti_color"])
                affichage_texte(self.window, f"NORMAL", self.fonts["font_mode_conduite"], (270, 65), self.dark_mode["anti_color"])
                affichage_texte(self.window, f"SPORT", self.fonts["font_mode_conduite"], (451, 65), self.dark_mode["anti_color"])
                #affichage batterie niveau
                affichage_texte(self.window, f"{int(self.batterie*100)}%", self.fonts["font_normal"], (70, 175), self.dark_mode["anti_color"])


                #Rafraîchissement de l'écran
                pygame.display.flip()


                #permet de tester toute les 10 secondes
                if self.index >= fps*10 :
                    if is_connected() :
                        self.wifi_etat = True
                    else :
                        self.wifi_etat = False
                    self.index = 0
                if self.index%(fps//2) == 0 :
                    changement_etat_clignotant(self)
                



            #boucle d'affichage de l'onglet navigation
            while navigation_loop :
                self.index+=1
                self.event_window()
                #Limitation de vitesse de la boucle
                self.clock.tick(fps) 

                #affichage des images
                self.window.blit(self.images["background_navigation_"+self.dark_mode["etat"]], (0,0)) #image du background
                affichage_clignotant(self)
                #affichage vitesse
                affichage_texte(self.window, f"{self.vitesse}", self.fonts["font_vitesse_navigation"], (388, 330), self.dark_mode["anti_color"])

                if self.index%(fps//2) == 0 :
                    changement_etat_clignotant(self)
                    self.index = 0
                #Rafraîchissement de l'écran
                pygame.display.flip()




            #boucle d'affichage de l'onglet parametre
            while systeme_loop :
                self.event_window()
                #Limitation de vitesse de la boucle
                self.clock.tick(fps) 
                #affichage des images
                self.window.blit(self.images["background_systeme_"+self.dark_mode["etat"]], (0,0)) #image du background
                
                #afichage des switchs
                for sw in switch_dict.values() :
                    affichage_switch(self, sw["position"], sw["etat"], sw["position_x_rond"])
                if self.info_regulateur_limitateur["affichage"] :
                    #affichage des boutçons plus et moins du limitateur et régulateur
                    affichage_bouton_regulateur_limitateur(self)
                    affichage_texte(self.window, f"{self.vitesse_consigne}", self.fonts["font_vitesse_consigne"], (570, 270), self.dark_mode["anti_color"])
                affichage_switch_3_etat(self, self.info_switch_3_etat_regulateur["position"], self.info_switch_3_etat_regulateur["etat"], self.info_switch_3_etat_regulateur["position_x_rond"])
                #Rafraîchissement de l'écran
                pygame.display.flip()






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
            if event.type == MOUSEBUTTONUP : # fonctionnement avec souris
                self.test_clic(X, Y)
            if systeme_loop :
                self.test_clic_bouton_regulateur_limitateur(event.type, X, Y)


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
