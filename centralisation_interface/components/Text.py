from module_import import *
from config import *
from utils.utils import *


class Text :
    def __init__(
            self,
            label: str,  # Nom de l'objet pour pouvoir le récupérer facilement avec get_object
            text: str,  # Texte à afficher
            font_name: str,  # Nom de la police utilisée pour le texte
            font_size: int,  # Taille de la police
            color: tuple,  # Couleur du texte sous forme de tuple (R, G, B)
            justify: str,  # Justification possible : ["center", "right", "left"]
            show: bool,  # Indique si l'objet doit être affiché ou non
            **kwargs  # Paramètres supplémentaires pour configurer l'objet
    ) :
        self.label =label
        self.text = text
        self.old_text = text
        self.color = color
        self.position = (0,0)
        self.justify = justify
        self.show = show
        self.kwargs = kwargs
        #obtenir un font dans le cache en fonction de la taille et du nom
        self.font = get_font_by_cache(font_name, font_size)
        self.create_text_rect()

    def draw(self, window) :
        if self.show :
            #affiche un texte variable dans le temps
            if self.old_text != self.text :#le texte à changé
                self.old_text = self.text
                self.create_text_rect()
                window.blit(self.text_surf, self.text_rect)
            #afficher un text static (inutile de recréé le text_rect)
            else :
                window.blit(self.text_surf, self.text_rect)

    def create_text_rect(self) :
        self.text_surf = self.font.render(f"{self.text}", True, self.color)
        size_text = self.text_surf.get_size()
        self.text_rect = self.text_surf.get_rect()
        if self.justify == "center":
            self.text_rect.center = (self.position[0], self.position[1]+size_text[1]//2)
        elif self.justify == "left":
            self. text_rect.midleft = (self.position[0], self.position[1]+size_text[1]//2)
        elif self.justify == "right":
            self.text_rect.midright = (self.position[0], self.position[1]+size_text[1]//2)

    def get_size(self) :
        return self.text_surf.get_size()
    
    def set_position(self, new_position) :
        self.position = new_position
        self.create_text_rect()

    def toggle_show(self) :
        self.show = not self.show
    
    def update_color(self) :
        self.color = dark_light_mode["text"][dark_light_mode["etat"]]
        self.create_text_rect()

    

