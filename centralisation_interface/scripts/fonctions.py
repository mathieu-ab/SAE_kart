from scripts.import_variable import *
#--|--# fonctions

def import_image(chemin) :
    return pygame.image.load(CURRENT_PATH+chemin).convert_alpha()

def import_font(chemin, size) :
    return pygame.font.Font(CURRENT_PATH+chemin, size)

def hex_to_rgb(hex_color):
    # Supprime le caractère '#' si présent
    hex_color = str(hex_color).replace("#", "")
    # Convertit en trois entiers (rouge, vert, bleu)
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def is_connected():
    try:
        # Tente de se connecter à un site web public connu
        socket.create_connection(("8.8.8.8", 53), timeout=3)  # 8.8.8.8 est un serveur DNS de Google
        return True
    except OSError:
        return False
    

def redirection_effet_bouton(self, sw) :
    if sw[0] == "detection_ligne_blanche" :
        print(f"{'activation' if sw[1]["etat"] else 'desactivation'} du mode detection ligne blanche")
    elif sw[0] == "detection_obstacle" :
        print(f"{'activation' if sw[1]["etat"] else 'desactivation'} du mode detection d'obstacle")
    elif sw[0] == "endormissement" :
        print(f"{'activation' if sw[1]["etat"] else 'desactivation'} du mode d'endormissement")
    elif sw[0] == "syst_heure" :
        if self.format_heure == "24h" :
            self.format_heure = "12h" 
        else :
            self.format_heure = "24h"
    elif sw[0] == "syst_unite" :
        if self.temperature_unite == "°F" :
            self.temperature_unite = "°C"
        else :
            self.temperature_unite = "°F"
    elif sw[0] == "syst_dark_mode" :
        if self.dark_mode["etat"] == "dark":
            self.dark_mode = {"etat" : "light", "color" : (255,255,255), "anti_color" : (0,0,0)}
        else :
            self.dark_mode = {"etat" : "dark", "color" : (0,0,0), "anti_color" : (255,255,255)}

def test_convertion_Celsius_to_Fahrenheit(temperature_c, unite) : 
    if unite == "°F" :
        return int((temperature_c*1.8) + 32)
    else :
        return temperature_c

##------------Fonction d'affichage--------------------##


#fonction qui va afficher du texte selon les critères en paramètres
def affichage_texte(window, text, font, pos, color) :
        text_surf = font.render(text, True, color) #(1, 236, 164) est la couleur en (R,V,B)
        #on utilise get_rect pour pouvoir center le text avce "center = "
        window.blit(text_surf, text_surf.get_rect(center = pos))


def affichage_heure(self) :
    #calcule de l'heure actuelle
    # Obtenir l'heure actuel en seconde
    local_time = localtime()
    heure = int(f"{local_time.tm_hour:02}")  # Heure locale (avec deux chiffres)
    minutes = f"{local_time.tm_min:02}"  # Minutes locales (avec deux chiffres)
    #affichage d l'heure actuelle
    #clignotement des 2 points
    if int(time()) % 2 == 0 : 
        warning = ":"
    else :
        warning = " "
    #affectation du format 12 ou 24h
    if self.format_heure == "12h" :
        if heure == 12 :
            heure = 12
            sup = "PM"
        if heure > 12 :
            heure = heure-12
            sup = "PM"
        else :
            sup = "AM"
    else :
        sup = ""
    affichage_texte(self.window, f"{heure}{warning}{minutes}{sup}", self.fonts["font_normal"], (709, 58), self.dark_mode["anti_color"])


def affichage_etat_wifi(self) :
    if self.wifi_etat :
        pygame.draw.circle(self.window, (26, 237, 21), (625, 70), 4)
    else :
        pygame.draw.line(self.window, (255,40,40), (625 - 5, 70-5), (625 + 5, 70+5), 3)
        pygame.draw.line(self.window, (255,40,40), (625-5, 70 + 5), (625+5, 70 - 5), 3)


def affichage_mode_conduite(self) :
    #on dessine un rectangle et 2 cercle pour simuler un rectangle à bord arrondie
    for info_mode_item in info_mode_conduite.items() :
        if info_mode_item[0] == self.mode_conduite :
            color = COLOR_MODE_CONDUITE[self.dark_mode["etat"]]["selected"]
        else :
            color = COLOR_MODE_CONDUITE[self.dark_mode["etat"]]["not selected"]
        pygame.draw.rect(self.window, color, pygame.Rect(info_mode_item[1], 36, 134, 57), border_radius=11)

        
def affichage_batterie(self) :
     #calcule de la couleur en fonction du poursentage de charge de la batterie
     pygame.draw.rect(
         self.window,
         hex_to_rgb(color_green_to_red[int((1-self.batterie)*len(color_green_to_red))]),
         pygame.Rect(144, 150+int((1-self.batterie)*150), 72, int(self.batterie*150)),
         border_radius=5)

def affichage_clignotant(self) :
    if self.clignotant_info["allume"] != None and self.clignotant_info["start"]+self.clignotant_info["cligno"] == int(time()) :
        self.clignotant_info["etat"] = not self.clignotant_info["etat"] 
        self.clignotant_info["cligno"]+=1
        if self.clignotant_info["cligno"] == 6 :
            self.clignotant_info["allume"] = None
            print(f"clignotant eteint (info envoyé)")

    if self.clignotant_info["etat"] and self.clignotant_info["allume"] == "gauche" :
        self.window.blit(self.images["clignotant_droit_allume_gauche"], (56, 329))
        self.window.blit(self.images["clignotant_droit_eteint_droit"], (655, 327))
    elif self.clignotant_info["etat"] and self.clignotant_info["allume"] == "droite" :
        self.window.blit(self.images["clignotant_droit_eteint_gauche"], (56, 329))
        self.window.blit(self.images["clignotant_droit_allume_droit"], (655, 327))
    elif self.clignotant_info["etat"] == False or self.clignotant_info["allume"] == None:
        self.window.blit(self.images["clignotant_droit_eteint_droit"], (655, 327))
        self.window.blit(self.images["clignotant_droit_eteint_gauche"], (56, 329))



def affichage_prevention(self) :
    i = 0
    for message in prevention_queue :
        affichage_message = True
        if message["end"] != None and message["start"]+message["end"] < int(time()) :
            affichage_message = False
            prevention_queue.pop(i)
        if affichage_message :
            self.window.blit(self.images["bg_prevention"], (247, 363-35*i))
            pygame.draw.rect(self.window, (251, 44, 44), pygame.Rect(247, 363-35*i, 363, 30), border_radius=6)
            affichage_texte(self.window, message["message"], self.fonts["font_prevention"], (428, 363-35*i+15), (255,255,255))
        i+=1

def affichage_bouton_regulateur_limitateur(self) :
    for signe in self.info_regulateur_limitateur["boutons"].items() :
        if signe[1]["etat"] :#on est en train d'appuyer sur le bouton
            self.window.blit(self.images["pressed_"+signe[0]], (signe[1]["position"][0]+5 ,signe[1]["position"][1]+5))
        else :
            self.window.blit(self.images["default_"+signe[0]], signe[1]["position"])



def affichage_switch(self, position, etat, position_x_rond) :
    # Vitesse d'animation
    ANIMATION_SPEED = 10

    # Initial state
    control_position_x = position_x_rond[0]
    # Déterminer la couleur de fond du switch
    toggle_bg_color = (30, 144, 255) if etat else (169, 169, 169)
    pygame.draw.rect(self.window, toggle_bg_color, (position[0], position[1], 71, 36), border_radius=25)
    
    # Calculer la position cible du contrôle
    target_position_x = position[0] + 3 if etat else position[0] + 71 - 30 - 3
    
    # Animation de transition
    distance_control_target = abs(control_position_x - target_position_x)
    if distance_control_target > ANIMATION_SPEED:
        if control_position_x < target_position_x:
            control_position_x += ANIMATION_SPEED
        else:
            control_position_x -= ANIMATION_SPEED
    else:
        control_position_x = target_position_x

    # Dessiner le contrôle
    pygame.draw.ellipse(self.window, (255, 255, 255), (control_position_x, position[1] + 3+distance_control_target//8, 30+distance_control_target//3, 30-distance_control_target//4))
    position_x_rond[0] = control_position_x



def affichage_switch_3_etat(self, position, etat, position_x_rond) :
    # Vitesse d'animation
    ANIMATION_SPEED = 20

    # Initial state
    control_position_x = position_x_rond[0]

    # Calculer la position cible du contrôle et couleur du bg
    if etat == "neutre" : 
        target_position_x = position[0] + 220//3 + 5
        toggle_bg_color = (169, 169, 169)
    elif etat == "regulateur" :
        target_position_x = position[0] + 5
        toggle_bg_color = (74, 255, 45)
    elif etat == "limitateur" :
        target_position_x = position[0] + 2*220//3 - 5
        toggle_bg_color = (255, 171, 30)
    # Déterminer la couleur de fond du switch
    pygame.draw.rect(self.window, toggle_bg_color, (position[0], position[1], 220, 80), border_radius=40)
    

    
    # Animation de transition
    distance_control_target = abs(control_position_x - target_position_x)
    if distance_control_target > ANIMATION_SPEED:
        if control_position_x < target_position_x:
            control_position_x += ANIMATION_SPEED
        else:
            control_position_x -= ANIMATION_SPEED
    else:
        control_position_x = target_position_x

    # Dessiner le contrôle
    pygame.draw.ellipse(self.window, (255, 255, 255), (control_position_x, position[1] + 5+distance_control_target//8, 70+distance_control_target//3, 70-distance_control_target//4))
    position_x_rond[0] = control_position_x



