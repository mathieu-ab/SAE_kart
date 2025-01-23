from module_import import *
from config import *
from utils.utils import *


class Shape :
    def __init__(
        self,
        label: str,  # Nom de l'objet pour pouvoir le récupérer facilement
        shape: str,  # Options possibles : "circle", "rectangle", "line"
        color: tuple,  # Couleur de l'objet sous forme de tuple (R, G, B)
        show: bool,  # Indique si l'objet doit être affiché ou non
        **kwargs  # Paramètres supplémentaires pour configurer l'objet
    ) :
        self.label =label
        self.color = color
        self.show = show
        self.shape = shape
        self.kwargs = kwargs
        self.position = (0,0)

    def draw(self, window) :
        if self.show :
            if self.shape == "rectangle" :
                pygame.draw.rect(window, self.color, (self.position[0], self.position[1], self.kwargs["size"][0], self.kwargs["size"][1]), border_radius=self.kwargs["border_radius"])
            elif self.shape == "circle" : 
                pygame.draw.circle(window, self.color, self.position, self.kwargs["radius"])
            elif self.shape == "line" :
                pygame.draw.line(window, self.color, self.position, (self.position[0]+self.kwargs["end_pos"][0], self.position[1]+self.kwargs["end_pos"][1]), self.kwargs["width"])

    def toggle_show(self) :
        self.show = not self.show

    def get_size(self) :
        return self.text_surf.get_size()
    
    def set_position(self, new_position) :
        self.position = new_position
    
    def change_color(self, new_color) :
        self.color = new_color

    

