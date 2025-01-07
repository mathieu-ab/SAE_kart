from scripts.import_variable import *
#--|--# fonctions

def import_image(chemin) :
    return pygame.image.load(CURRENT_PATH+chemin).convert_alpha()

def import_font(chemin, size) :
    return pygame.font.Font(CURRENT_PATH+chemin, size)


#fonction qui va afficher du texte selon les critères en paramètres
def affichage_texte(window, text, font, pos, color) :
        text_surf = font.render(text, True, color) #(1, 236, 164) est la couleur en (R,V,B)
        #on utilise get_rect pour pouvoir center le text avce "center = "
        window.blit(text_surf, text_surf.get_rect(center = pos))


def affichage_heure(self) :
    #calcule de l'heure actuelle
    # Obtenir l'heure actuel en seconde
    local_time = time.localtime()
    heure = f"{local_time.tm_hour:02}"  # Heure locale (avec deux chiffres)
    minutes = f"{local_time.tm_min:02}"  # Minutes locales (avec deux chiffres)
    #affichage d l'heure actuelle
    if int(time.time()) % 2 == 0 : 
        warning = ":"
    else :
        warning = " "
    affichage_texte(self.window, f"{heure}{warning}{minutes}", self.fonts["font_heure"], (728, 25), self.dark_mode["anti_color"])


