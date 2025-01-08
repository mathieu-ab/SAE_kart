from scripts.fonctions import *
from scripts.import_variable import *


class Interface :
    def __init__(self):
        #initialisation pygame (interface graphique) 
        pygame.init()
        pygame.display.set_caption("Tableau de bord Kart") #changement du titre de la fenêtre
        pygame.mouse.set_visible(False)

        #Ouverture de la fenêtre Pygame
        self.largeur_ecran, self.hauteur_ecran = 800, 480
        self.window = pygame.display.set_mode((800,480)) #création d'une fenêtre en plein écran
        self.clock = pygame.time.Clock() #clock utile pour bloquer la boucle du jeu et limiter la vitesse de la boucle (même principe que sleep du module time)
        self.images = {} #dictionnaire qui va contenir les objects des images
        self.fonts = {} #dictionnaire qui va contenir les objects des images

        #importation des images
        self.images["background_affichage_dark"] = import_image("/assets/images/affichage/background_affichage_dark.png")
        # self.images["background_affichage_light"] = import_image("/assets/images/affichage/background_affichage_light.png")

        #importation des fonts
        self.fonts["font_normal"] = import_font("/assets/fonts/Roboto-Bold.ttf", 37)
        self.fonts["font_mode_conduite"] = import_font("/assets/fonts/Roboto-Bold.ttf", 24)
        self.fonts["font_nombres"] = import_font("/assets/fonts/Seven-Segment.ttf", 50)
        self.fonts["font_vitesse"] = import_font("/assets/fonts/7-segment-bold.ttf", 160)

        self.dark_mode = {"etat" : self.images["background_affichage_dark"], "color" : (0,0,0), "anti_color" : (255,255,255)}

        #variable importé des autre partie du projet SAE
        self.vitesse = 17
        self.wifi_etat = True #true = connecté
        self.mode_conduite = "normal"
        self.temperature = 70


    def start(self) :
        global main_loop, affichage_loop
        while main_loop :
            while affichage_loop : #boucle du menu
                #Limitation de vitesse de la boucle
                self.clock.tick(fps) 

                #position de la sourie pour le clic
                X, Y = pygame.mouse.get_pos()

                #event du clavier/de la fenêtre
                keys = pygame.key.get_pressed() #on récupère tout les touches du clavier (keys[] = True si la touche est préssé)
                for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                    if event.type == QUIT or keys[K_ESCAPE] :     #Si on ferme le jeu, on sort des 2 boucles (principal et menu) ce qui ferme le jeu
                        main_loop = False
                        affichage_loop = False
                    if event.type == pygame.FINGERUP :
                        self.test_clic(X, Y)   

                #event clic
                
                #affichage des images
                self.window.blit(self.dark_mode["etat"], (0,0)) #image du background
                affichage_etat_wifi(self)
                affichage_mode_conduite(self)
                
               
                #affichage des textes
                affichage_heure(self)
                #affichag vitesse
                affichage_texte(self.window, f"{self.vitesse}", self.fonts["font_vitesse"], (380, 130), self.dark_mode["anti_color"])
                #affichag temperature
                affichage_texte(self.window, f"{self.temperature}", self.fonts["font_nombres"], (698, 215), self.dark_mode["anti_color"])
                affichage_texte(self.window, f"°C", self.fonts["font_normal"], (740, 212), self.dark_mode["anti_color"])
                affichage_texte(self.window, f"ECO", self.fonts["font_mode_conduite"], (92, 65), self.dark_mode["anti_color"])
                affichage_texte(self.window, f"NORMAL", self.fonts["font_mode_conduite"], (270, 65), self.dark_mode["anti_color"])
                affichage_texte(self.window, f"SPORT", self.fonts["font_mode_conduite"], (451, 65), self.dark_mode["anti_color"])


                #Rafraîchissement de l'écran
                pygame.display.flip()



    def test_clic(self, x, y) :
        # # test clic dark mode
        # if 15 < x < 67 and 15 < y < 67 and pygame.MOUSEBUTTONDOWN :
        #     if self.dark_mode["etat"] == self.images["background_affichage_dark"]:
        #         self.dark_mode = {"etat" : self.images["background_affichage_light"], "color" : (255,255,255), "anti_color" : (0,0,0)}
        #     else :
        #         self.dark_mode = {"etat" : self.images["background_affichage_dark"], "color" : (0,0,0), "anti_color" : (255,255,255)}

        #test clic mode conduite
        for info_mode_item in info_mode_conduite.items() : #boucle pour les 3 boutons. La dernière condition est pour éviter d'envoyer un rechanger au même mode de conduite
            if info_mode_item[1] < x < info_mode_item[1] + 134 and 36 < y < 93 and pygame.MOUSEBUTTONDOWN and self.mode_conduite != info_mode_item[0]:
                self.mode_conduite = info_mode_item[0]
                print(f"nouveau mode de conduite : {self.mode_conduite} (info envoyé)")