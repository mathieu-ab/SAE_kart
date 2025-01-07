from scripts.fonctions import *
from scripts.import_variable import *


class Interface :
    def __init__(self):
        #initialisation pygame (interface graphique) 
        pygame.init()
        pygame.display.set_caption("Tableau de bord Kart") #changement du titre de la fenêtre

        #Ouverture de la fenêtre Pygame
        self.largeur_ecran, self.hauteur_ecran = 800, 480
        self.window = pygame.display.set_mode((800,480)) #création d'une fenêtre en plein écran
        self.clock = pygame.time.Clock() #clock utile pour bloquer la boucle du jeu et limiter la vitesse de la boucle (même principe que sleep du module time)
        self.images = {} #dictionnaire qui va contenir les objects des images
        self.fonts = {} #dictionnaire qui va contenir les objects des images

        #importation des images
        self.images["background_affichage_dark"] = import_image("/assets/images/affichage/background_affichage_dark.png")
        self.images["background_affichage_light"] = import_image("/assets/images/affichage/background_affichage_light.png")

        #importation des fonts
        self.fonts["font_heure"] = import_font("/assets/fonts/Roboto-Bold.ttf", 30)
        self.fonts["font_vitesse"] = import_font("/assets/fonts/7-segment-bold.ttf", 170)

        self.dark_mode = {"etat" : self.images["background_affichage_dark"], "color" : (0,0,0), "anti_color" : (255,255,255)}

        #variable importé des autre partie du projet SAE
        self.vitesse = 17


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
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.test_clic(X, Y)   

                #event clic
                
                 

                pygame.draw.rect(self.window, self.dark_mode["color"], (0,0, self.largeur_ecran, self.hauteur_ecran))
                #affichage des images
                self.window.blit(self.dark_mode["etat"], (0,0))

                #affichage des textes
                affichage_heure(self)
                #affichag vitesse
                affichage_texte(self.window, f"{self.vitesse}", self.fonts["font_vitesse"], (380, 120), self.dark_mode["anti_color"])


                #Rafraîchissement de l'écran
                pygame.display.flip()



    def test_clic(self, x, y) :
        #test clic dark mode
        if 15 < x < 67 and 15 < y < 67 and pygame.MOUSEBUTTONDOWN :
            if self.dark_mode["etat"] == self.images["background_affichage_dark"]:
                self.dark_mode = {"etat" : self.images["background_affichage_light"], "color" : (255,255,255), "anti_color" : (0,0,0)}
            else :
                self.dark_mode = {"etat" : self.images["background_affichage_dark"], "color" : (0,0,0), "anti_color" : (255,255,255)}