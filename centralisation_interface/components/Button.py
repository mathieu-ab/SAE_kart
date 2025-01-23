from module_import import *
from config import *
from utils.utils import *
from components.Text import Text
from components.Image import Image


class Button :
    def __init__(
            self,
            label: str,  # Nom de l'objet pour le récupérer facilement
            text: str,  # Texte affiché sur le bouton
            font_name: str,  # Nom de la police
            font_size: int,  # Taille de la police
            icon_path: str,  # Chemin de l'image de l'icône (facultatif)
            state: str,  # Options possibles : ["normal", "pressed", "disabled"]
            size: tuple[int, int],  # Taille (width, height) du bouton
            dark_light: bool,  # Indique si l'icône doit s'adapter au thème clair/sombre
            callback_action: callable,  # Fonction appelée lors d'un clic
            auto_change_state: bool, # Indique si un click change l'etat du bouton automatiquement ou non
            **kwargs  # Paramètres supplémentaires
    ):
        self.label = label
        self.text = Text(
            label=f"Text_button_{label}",
            text=text,
            font_name=font_name,
            font_size=font_size,
            color=(dark_light_mode["text"][dark_light_mode["etat"]]),
            justify="left",
            show=True
            )
        self.font = get_font_by_cache(font_name, font_size)
        self.state = state if state in ["normal", "pressed", "disabled"] else "normal"  # Validation de l'état
        self.position = (0,0)
        self.position_icon = (0,0)
        self.position_text = (0,0)
        self.size = size
        self.kwargs = kwargs
        self.callback_action = callback_action
        self.auto_change_state = auto_change_state
        if icon_path != None :
            self.icon = Image(
                label=f"Image_button_{label}",
                image_path=icon_path,
                show=True,
                callback_action=None,
                dark_light=dark_light
                )
        else :
            self.icon = None
        self.pygame_rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])


    def draw(self, window) :
        #affiche un texte variable dans le temps
        pygame.draw.rect(
            window,
            dark_light_mode["button"][dark_light_mode["etat"]][self.state],
            self.pygame_rect,
            border_radius=10)
        if self.icon != None :
            self.icon.draw(window)
        self.text.draw(window)

    def get_size(self) :
        return self.size
    
    def set_position(self, new_position) :
        self.position = new_position
        self.pygame_rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        size_text = self.text.get_size()
        if self.icon != None :
            size_icon = self.icon.get_size()
            self.icon.set_position((
            self.position[0]+self.size[0]//2-(size_icon[0]+size_text[0]+5)//2,
            self.position[1]+self.size[1]//2-size_icon[1]//2
            ))
            empatement = 5
        else :
            size_icon = (0,0)
            empatement = 0

        if size_icon[0]+size_text[0] > self.size[0] :
            print(f"Warning : La taille du text + icon dépasse du bouton {self.label}")
        self.text.set_position((
            self.position[0]+self.size[0]//2-(size_icon[0]+size_text[0]+empatement)//2+size_icon[0]+empatement,
            self.position[1]+self.size[1]//2-size_text[1]//2
        ))

    def on_release(self, mouse_position) :
        if (self.position[0] < mouse_position[0] < (self.position[0]+self.size[0])) and (self.position[1] < mouse_position[1] < (self.position[1]+self.size[1])) :
            if self.callback_action != None and self.auto_change_state :
                self.callback_action(**self.kwargs)
        if self.auto_change_state :
            self.state = "normal"
        
    def on_click(self, mouse_position) :
        if (self.position[0] < mouse_position[0] < (self.position[0]+self.size[0])) and (self.position[1] < mouse_position[1] < (self.position[1]+self.size[1])) :
            if self.auto_change_state :
                self.state = "pressed"
            if self.auto_change_state == False and self.callback_action != None :
                self.callback_action(**self.kwargs)

    def update_color(self) :
        self.text.update_color()
        if self.icon != None :
            self.icon.update_color()
        


