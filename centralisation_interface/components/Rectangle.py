from module_import import *
from config import *
from utils.utils import *


class Rectangle :
    def __init__(
            self,
            label: str, #nom de l'objet pour poivoir le récupéré facilement
            size: tuple,
            color: tuple,
            border_radius: int,
            show: bool
    ) :
        self.label =label
        self.size = size
        self.color = color
        self.border_radius = border_radius
        self.show = show
        self.position = (0,0)

    def draw(self, window) :
        if self.show :
            pygame.draw.rect(window, self.color, (self.position[0], self.position[1], self.size[0], self.size[1]), border_radius=self.border_radius)

    def toggle_show(self) :
        self.show = not self.show

    def get_size(self) :
        return self.text_surf.get_size()
    
    def set_position(self, new_position) :
        self.position = new_position

    

