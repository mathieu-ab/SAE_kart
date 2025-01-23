from module_import import *
from config import *
from utils.utils import *

class Switch:
    def __init__(
            self,
            label: str,  # Nom de l'objet pour le récupérer facilement
            show: bool,  # Détermine si le switch est visible
            callback_action: callable,  # Fonction appelée lors d'un clic
            **kwargs  # Paramètres supplémentaires
    ):
        self.label = label
        self.position = (0,0)
        self.etat = True
        self.show = show
        self.kwargs = kwargs
        self.callback_action = callback_action

        # Dimensions par défaut du switch
        self.size = (71, 36)

        # Initialisation des propriétés internes
        self.animation_speed = 10
          # Position initiale du cercle

    def draw(self, window):
        if not self.show:
            return

        # Déterminer la couleur de fond du switch
        toggle_bg_color = (30, 144, 255) if self.etat else (169, 169, 169)
        pygame.draw.rect(window, toggle_bg_color, (self.position[0], self.position[1], self.size[0], self.size[1]), border_radius=25)

        # Calculer la position cible du contrôle
        target_position_x = self.position[0] + 3 if self.etat else self.position[0] + self.size[0] - 30 - 3

        # Animation de transition
        distance_control_target = abs(self.control_position_x - target_position_x)
        if distance_control_target > self.animation_speed:
            if self.control_position_x < target_position_x:
                self.control_position_x += self.animation_speed
            else:
                self.control_position_x -= self.animation_speed
        else:
            self.control_position_x = target_position_x

        # Dessiner le contrôle
        pygame.draw.ellipse(window, (255, 255, 255),
                            (self.control_position_x, self.position[1] + 3 + distance_control_target // 8,
                             30 + distance_control_target // 3, 30 - distance_control_target // 4))

    def toggle(self):
        self.etat = not self.etat

    def toggle_show(self):
        self.show = not self.show

    def set_position(self, new_position):
        self.position = new_position
        self.control_position_x = self.position[0] + (3 if self.etat else self.size[0] - 30 - 3)

    def get_size(self):
        return self.size

    def on_click(self, mouse_position) :
        if (self.position[0] < mouse_position[0] < (self.position[0]+self.size[0])) and (self.position[1] < mouse_position[1] < (self.position[1]+self.size[1])) :
            self.toggle()
            if self.callback_action != None:
                self.callback_action(self.etat,**self.kwargs)
    
    #cette méthode, même si elle n'est pas utile, dois être implémenté pour s'uniformiser avec les autres classes cliquable
    def on_release(self, mouse_position) :
        pass
