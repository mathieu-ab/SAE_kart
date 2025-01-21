from config import *


def import_image(chemin) :
    return pygame.image.load(CURRENT_PATH + chemin).convert_alpha()

def import_font(chemin, size) :
    return pygame.font.Font(CURRENT_PATH + chemin, size)




    

def redirection_effet_bouton(self, sw) :
    if sw[0] == "detection_ligne_blanche" :
        self.mqtt_thread_handler.add_message("aide/ligne_blanche", is_activate(sw[1]['etat']))
    elif sw[0] == "detection_obstacle" :
        self.mqtt_thread_handler.add_message("aide/obstacle", is_activate(sw[1]['etat']))
    elif sw[0] == "endormissement" :
        self.mqtt_thread_handler.add_message("aide/endormissement", is_activate(sw[1]['etat']))
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



def is_activate(etat) :
    if etat :
        return "a"
    return "d"

##------------Fonction d'affichage--------------------##


#fonction qui va afficher du texte selon les critères en paramètres
def affichage_texte(window, text, font, pos, color) :
        text_surf = font.render(text, True, color) #(1, 236, 164) est la couleur en (R,V,B)
        #on utilise get_rect pour pouvoir center le text avce "center = "
        window.blit(text_surf, text_surf.get_rect(center = pos))








def affichage_mode_conduite(self) :
    #on dessine un rectangle et 2 cercle pour simuler un rectangle à bord arrondie
    for info_mode_item in info_mode_conduite.items() :
        if info_mode_item[0] == self.mode_conduite :
            color = COLOR_MODE_CONDUITE[self.dark_mode["etat"]]["selected"]
        else :
            color = COLOR_MODE_CONDUITE[self.dark_mode["etat"]]["not selected"]
        pygame.draw.rect(self.window, color, pygame.Rect(info_mode_item[1], 36, 99, 47), border_radius=11)

def affichage_activation_charge(self) :
    if self.activation_charge_info["etat"] :
        color = COLOR_MODE_CONDUITE[self.dark_mode["etat"]]["selected"]
        pygame.draw.rect(self.window, color, pygame.Rect(424, 39, 99, 47), border_radius=11)
    else :
        color = COLOR_MODE_CONDUITE[self.dark_mode["etat"]]["not selected"]
    pygame.draw.rect(self.window, color, pygame.Rect(424, 39, 99, 47), border_radius=11)

        
def affichage_batterie(self) :
     #calcule de la couleur en fonction du poursentage de charge de la batterie
     pygame.draw.rect(
         self.window,
         hex_to_rgb(color_green_to_red[int((1-self.batterie)*len(color_green_to_red))]),
         pygame.Rect(144, 150+int((1-self.batterie)*150), 72, int(self.batterie*150)),
         border_radius=5)

def changement_etat_clignotant(self) :
    if self.clignotant_info["allume"] != None  :
        self.clignotant_info["etat"] = not self.clignotant_info["etat"] 
        self.clignotant_info["cligno"]+=1
        if self.clignotant_info["cligno"] == 6 :
            self.clignotant_info["allume"] = None
            self.mqtt_thread_handler.add_message("aide/clignotant", "e")

def affichage_clignotant(self) :
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


#---------------------NEW---------------------
def get_font_by_cache(font_name: str, font_size: int) -> pygame.font.Font:
    """
    Récupère une police Pygame en utilisant un système de cache pour éviter de 
    charger plusieurs fois la même police avec les mêmes paramètres.

    Args:
        font_name (str): Le nom de la police (sans l'extension .ttf).
        font_size (int): La taille de la police à charger.

    Returns:
        pygame.font.Font: Une instance de la police Pygame correspondant au nom et à la taille spécifiés.
    """
    # Vérification dans le cache
    for font in font_cache:
        # Si une police avec le même nom et la même taille est trouvée, la renvoyer
        if font["name"] == font_name and font["size"] == font_size:
            return font["pygame_font"]

    # Si la police n'est pas dans le cache, la charger depuis un fichier
    try:
        pygame_font = pygame.font.Font(f"{CURRENT_PATH}/assets/fonts/{font_name}.ttf", font_size)
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier de police '{font_name}.ttf' est introuvable dans le dossier '/assets/fonts/'.")

    # Ajouter la police chargée au cache
    font_cache.append({
        "name": font_name,
        "size": font_size,
        "pygame_font": pygame_font
    })

    # Retourner la police chargée
    return pygame_font

def update_heure(self) :
    #calcule de l'heure actuelle
    # Obtenir l'heure actuel en seconde
    local_time = localtime()
    heure = f"{local_time.tm_hour:02}"
    minutes = f"{local_time.tm_min:02}"  # Minutes locales formatées

    # Clignotement des deux points
    warning = ":" if int(time()) % 2 == 0 else " "

    # Formatage de l'heure en 12h ou 24h
    if self.format_heure == "12h":
        sup = "PM" if int(heure) >= 12 else "AM"
        heure = 12 if int(heure) == 12 or heure == 0 else int(heure) % 12
    else:
        sup = ""
    self.container_storage["affichage"]["Heure Wifi"].get_object("Heure").text = f"{heure}{warning}{minutes}{" "*len(sup)}"
    self.container_storage["affichage"]["Heure Wifi"].get_object("PMAM").text = f"{sup}"

def etat_wifi(self, is_connected) :
    if is_connected :
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Connected").show = True
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Not Connected 1").show = False
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Not Connected 2").show = False
    else :
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Connected").show = False
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Not Connected 1").show = True
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Not Connected 2").show = True


def test_connection(self):
    def check():
        try:
            socket.create_connection((IP_BROKER_MQTT, 1883), timeout=3)
            etat_wifi(self, True)
        except OSError:
            etat_wifi(self, False)

    thread = threading.Thread(target=check, daemon=True)
    thread.start()

def hex_to_rgb(hex_color):
    # Supprime le caractère '#' si présent
    hex_color = str(hex_color).replace("#", "")
    # Convertit en trois entiers (rouge, vert, bleu)
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def test_convertion_Celsius_to_Fahrenheit(temperature_c, unite) : 
    if unite == "°F" :
        return int((temperature_c*1.8) + 32)
    else :
        return temperature_c