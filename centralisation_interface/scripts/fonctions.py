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
    affichage_texte(self.window, f"{heure}{warning}{minutes}", self.fonts["font_normal"], (728, 25), self.dark_mode["anti_color"])


def affichage_etat_wifi(self) :
    if self.wifi_etat :
        pygame.draw.circle(self.window, (26, 237, 21), (155, 35), 4)
    else :
        pygame.draw.line(self.window, (255,40,40), (155 - 5, 35-5), (155 + 5, 35+5), 3)
        pygame.draw.line(self.window, (255,40,40), (155-5, 35 + 5), (155+5, 35 - 5), 3)


def affichage_mode_conduite(self) :
    #on dessine un rectangle et 2 cercle pour simuler un rectangle à bord arrondie

    for info_mode_item in info_mode_conduite.items() :
        if info_mode_item[0] == self.mode_conduite :
            color = (103, 246, 99)
        else :
            color = (177, 177, 177)
        pygame.draw.circle(self.window, color, (info_mode_item[1] + 11, 90 + 11), 11)  # Cercle gauche
        pygame.draw.circle(self.window, color, (info_mode_item[1] + 72 - 11, 90 + 11), 11)  # Cercle droit
        # Dessiner le rectangle central (sans les coins)
        pygame.draw.rect(self.window, color, (info_mode_item[1] + 11, 90, 72 - 2 * 11, 22))