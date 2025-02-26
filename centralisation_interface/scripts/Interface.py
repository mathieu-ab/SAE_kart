
from scripts.setup_draw import setup_draw
from module_import import *
from components import *
from config import *
from utils.utils import *
from callbacks import *

class Interface :
    def __init__(self):
        self.mqtt_thread_handler = None
        #initialisation pygame (interface graphique) 
        pygame.init()
        pygame.display.set_caption("Tableau de bord Kart") #changement du titre de la fenêtre
        if tactile : #si on est en mode ecran tactile on enlève la souris de l'écran
            pygame.mouse.set_visible(False)

        #Ouverture de la fenêtre Pygame
        self.window = pygame.display.set_mode((800,480)) #création d'une fenêtre en 800x480 qui est la taille de l'écran utilisé par la rapsberry
        self.clock = pygame.time.Clock() #clock utile pour bloquer la boucle et limiter la vitesse (même principe que sleep du module time)

        self.index = 0 #clock d'indice pour effectuer des tâches periodiquement
        self.index_nav = 0 #On utilise una autre clock pour garder une syncronisié entre l'update de l'image map.png par le gps et l'update de l'image sur le tableau de bord
        #dictionnaire des listes qui va contenir tout les object qui sont cliquable
        self.clickable_object = {
            "affichage" : [],
            "navigation" : [],
            "systeme" : []
        }
        #dictionnaire des listes qui va contenir tout les object à afficher
        self.container_storage = {
            "affichage" : {},
            "navigation" : {},
            "systeme" : {}
        }
        self.current_page = "affichage" #page à afficher
        #information utile pour gérer les clignotants
        self.clignotant = {"index_clignotant" : 1, #compteur pour changer l'etat du clignotant periodiquement
                           "cligno" : 1, #nombre d'acoup restant avant d'eteindre le clignotant
                           "etat" : False, #affiche l'etat du clignotant actuel
                           "allume" : None, #allume deviens "droite" ou "gauche" quand un clignotant est allumé. Sinon il reste en None
                           "start" : None #indique le temps avec time() au moment où le clignotant c'est déclanché
                           } 

        #paramètrage
        self.format_heure = "24h"
        self.temperature_unite = "°C"

        #variable importé des autre partie du projet SAE
        #une valeur par defaut est mise en attendant d'avoir des vrai informations
        self.vitesse = 17
        self.vitesse_consigne = 17
        self.temperature_batterie = 20
        self.temperature_moteur = 20
        self.eg_value = 0
        self.eg_choice = ["1120-", 84]
        setup_draw(self)

    #méthode pour déssiner les objets
    #tout les object sont dans des containers. chaque container à une méthode draw pour dessiner les object à l'interrieur. 
    #il est donc possible de mettre des container dans d'autre container
    def draw(self) :
        if self.current_page == "eg" : 
            image = pygame.image.load(f"{CURRENT_PATH}/assets/images/affichage/easter_egg/images{[['1120-', 84], ['1119-', 81], ['1119_21-', 78], ['1119_1-', 89]].index(self.eg_choice)}./{self.eg_choice[0]}{self.eg_value}.png")
            image = pygame.transform.scale(image, (800, 480))
            self.window.blit(image, (0,0))
            if self.eg_value == self.eg_choice[1] :
                self.eg_value = 0
            else :
                self.eg_value+=1
        else :
            for container in self.container_storage[self.current_page].values() :
                container.draw(self.window)

    #boucle principale de l"interface
    def start(self) :
        while main_loop :
            self.index+=1
            #captation des evenement de la fenêtre : si un clic est effectué, ou une touche appuyé
            self.event_window()
            #Limitation de vitesse de la boucle
            if self.current_page == "eg" :
                self.clock.tick(10) 
            else :
                self.clock.tick(fps) 
            #dessin de chaque objet
            self.draw()
            #test periodique de certain élément
            self.periodic_test()
            #Rafraîchissement de l'écran
            pygame.display.flip()

    #test periodique de certain élément
    def periodic_test(self) :
        #changepent d'etat des clignotant toute les 0.5 secondes (fps//2)
        if self.clignotant["index_clignotant"]%(fps//2) == 0 :
            self.clignotant["index_clignotant"] = 1
            update_clignotant(self)
        else :
            self.clignotant["index_clignotant"]+=1
        #toute les secondes on update l'heure
        if self.index % fps == 0:
            update_heure(self)
        #toute les 10 secondes on test si on est bien connecté au hotstop wifi
        if self.index % (fps*10) == 0 :
            test_connection(self)
            self.index = 0
        # if self.index_nav % (fps*TIME_UPDATE_NAV) == 0 :
        #     self.container_storage["navigation"]["Gps"].get_object("Image Nav").set_absolute_path(CURRENT_PATH[:-25]+"/GPS/map.png")
        #     self.container_storage["navigation"]["Gps"].get_object("Image Nav").set_size((435,290))

    def event_window(self) :
        global main_loop
        #event du clavier/de la fenêtre
        keys = pygame.key.get_pressed() #on récupère tout les touches du clavier (keys[] = True si la touche est préssé)
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE] :   #Si on ferme la fenêtre, on sort de la boucle principal
                if self.current_page == "eg" :
                    self.current_page  ="affichage"
                else :
                    main_loop = False
            if self.current_page == "eg" :
                return
            if event.type == MOUSEBUTTONDOWN : #appui
                if tactile:
                    # Convertir les coordonnées tactiles en pixels
                    X = int(event.x * pygame.display.get_surface().get_width())
                    Y = int(event.y * pygame.display.get_surface().get_height())
                else:
                    X, Y = event.pos  # Utiliser les coordonnées de la souris
                #pour chaque objet cliquable, on va dans la methode on_click
                for objt in self.clickable_object[self.current_page] :
                    objt.on_click((X, Y))
            elif event.type == MOUSEBUTTONUP : #relâchement
                if tactile:
                    # Convertir les coordonnées tactiles en pixels
                    X = int(event.x * pygame.display.get_surface().get_width())
                    Y = int(event.y * pygame.display.get_surface().get_height())
                else:
                    X, Y = event.pos  # Utiliser les coordonnées de la souris
                #pour chaque objet cliquable, on va dans la methode on_release
                for objt in self.clickable_object[self.current_page] :
                    objt.on_release((X, Y))