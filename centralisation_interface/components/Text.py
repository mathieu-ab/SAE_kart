from module_import import *


class Text :
    def __init__(
            self,
            window, #fenêtre
            text: str,
            font_name: str,
            font_size: int,
            visible: bool,
            color: tuple,
            position: tuple,
            justify: str #justify possible : ["center", "right", "left"]
    ) :
        self.text = text
        self.visible = visible
        self.color = color
        self.position = position
        self.justify = justify
        #obtenir un font dans le cache en fonction de la taille et du nom
        self.font = get_font_by_cache(font_name, font_size)
        self.create_text_rect()


    def update_affichage(self, window, new_text) :
        #affiche un texte variable dans le temps
        if self.visible :
            if self.text != new_text :#le texte à changé
                self.text = new_text
                self.create_text_rect()
                window.blit(self.text_surf, self.text_rect)
            else :
                window.blit(self.text_surf, self.text_rect)

    def create_text_rect(self) :
        self.text_surf = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surf.get_rect()
        if self.justify == "center":
            self.text_rect.center = self.position
        elif self.justify == "left":
            self. text_rect.midleft = self.position
        elif self.justify == "right":
            self.text_rect.midright = self.position

    #changer le texte en visible ou non
    def toggle_visible(self) :
        self.visible = not self.visible


    def get_size(self) :
        return self.text_surf.get_size()


