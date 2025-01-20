from module_import import *
from config import *
from utils.utils import *


class Text :
    def __init__(
            self,
            label: str, #nom de l'objet pour poivoir le récupéré facilement
            text: str,
            font_name: str,
            font_size: int,
            color: tuple,
            justify: str, #justify possible : ["center", "right", "left"]
            show: bool
    ) :
        self.label =label
        self.text = text
        self.old_text = text
        self.color = color
        self.position = (0,0)
        self.justify = justify
        self.show = show
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
            else :
                window.blit(self.text_surf, self.text_rect)

    def create_text_rect(self) :
        self.text_surf = self.font.render(self.text, True, self.color)
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

    

