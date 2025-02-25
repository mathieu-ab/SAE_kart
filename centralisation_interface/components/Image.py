from module_import import *
from config import *
from utils.utils import *


class Image :
    def __init__(
            self,
            label: str,  # Nom de l'objet pour pouvoir le récupérer facilement
            image_path: str,  # Chemin de l'image de l'icône (facultatif)
            show: bool,  # Indique si l'objet doit être affiché ou non
            callback_action: callable,  # Fonction à appeler lorsqu'un clic est effectué
            dark_light: bool,  # Indique si l'icône doit s'adapter au thème clair/sombre
            **kwargs  # Paramètres supplémentaires pour configurer l'objet
    ):
        self.label = label
        self.show = show
        self.position = (0,0)
        self.kwargs = kwargs
        self.callback_action = callback_action
        self.dark_light = dark_light
        self.image_path = image_path
        self.image = self.get_pygame_image(image_path)
        self.size = self.image.get_size()

    def draw(self, window) :
        if self.show :
            window.blit(self.image, self.position)

    def toggle_show(self) :
        self.show = not self.show

    def get_size(self) :
        return self.image.get_size()
    
    def set_position(self, new_position) :
        self.position = new_position
        
    def get_pygame_image(self, path) :
        try:
            if self.dark_light :
                dlm = dark_light_mode["etat"]
            else :
                dlm = ""
            return pygame.image.load(f"{CURRENT_PATH}/assets/images/{path}{dlm}.png").convert_alpha()
        except FileNotFoundError:
            raise FileNotFoundError(f"L'image avec ce chemin '{CURRENT_PATH}/assets/images/{path}{dlm}.png' est introuvable.")

    def change_image(self, new_img_path) :
        self.image = self.get_pygame_image(new_img_path)
        self.image_path = new_img_path

    def on_release(self, mouse_position) :
        if (self.position[0] < mouse_position[0] < (self.position[0]+self.size[0])) and (self.position[1] < mouse_position[1] < (self.position[1]+self.size[1])) and self.show :
            if self.callback_action != None :
                self.callback_action(**self.kwargs, etat="release")
        else :
            self.callback_action(**self.kwargs, etat="release_outside")
        
    def on_click(self, mouse_position) :
        if (self.position[0] < mouse_position[0] < (self.position[0]+self.size[0])) and (self.position[1] < mouse_position[1] < (self.position[1]+self.size[1])) and self.show :
            if self.callback_action != None :
                self.callback_action(**self.kwargs, etat="click")

    def update_color(self) :
        if self.dark_light :
            self.image = self.get_pygame_image(self.image_path)

    def set_absolute_path(self, new_img_path) :
        try:
            self.image = pygame.image.load(new_img_path).convert_alpha()
        except FileNotFoundError:
            raise FileNotFoundError(f"L'image avec ce chemin '{new_img_path}' est introuvable.")
        self.image_path = new_img_path

    def set_size(self, size) :
        self.image = pygame.transform.scale(self.image, size)