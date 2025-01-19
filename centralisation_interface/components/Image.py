from module_import import *
from config import *
from utils.utils import *


class Image :
    def __init__(
            self,
            label: str,  # Nom de l'objet pour le récupérer facilement
            image_path: str,  # Chemin de l'image de l'icône (facultatif)
            show: bool, 
            callback_action: callable,  # Fonction appelée lors d'un clic
            callback_mqtt_response: callable,  # Fonction appelée pour gérer la réponse MQTT
            **kwargs  # Paramètres supplémentaires
    ):
        self.label = label
        self.show = show
        self.position = (0,0)
        self.kwargs = kwargs
        # Callback
        self.callback_action = callback_action
        self.callback_mqtt_response = callback_mqtt_response
        # Surface de texte et rectangle associé
        self.image = self.get_pygame_image(image_path)


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
            return pygame.image.load(f"{CURRENT_PATH}/assets/images/{path}").convert_alpha()
        except FileNotFoundError:
            raise FileNotFoundError(f"L'image avec ce chemin '{path}' est introuvable dans le dossier '/assets/images/'.")

