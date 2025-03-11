from config import *


def get_font_by_cache(font_name, font_size):
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
    self.container_storage["affichage"]["Heure Wifi"].get_object("Heure").text = f"{heure}{warning}{minutes}{' '*len(sup)}"
    self.container_storage["affichage"]["Heure Wifi"].get_object("PMAM").text = f"{sup}"

#ajustement de l'etat de la connection wifi
def etat_wifi(self, is_connected) :
    if is_connected :
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Connected").show = True
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Not Connected 1").show = False
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Not Connected 2").show = False
    else :
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Connected").show = False
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Not Connected 1").show = True
        self.container_storage["affichage"]["Heure Wifi"].get_object("Wifi Not Connected 2").show = True

#fonction pour tester la connection wifi
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
    

def draw_prevention_message(self_Interface) :
    for k in range(3) :        
        self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {k}").get_object(f"Prevention {k} text").text = ""
        self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {k}").get_object(f"Prevention {k} text").show = False
        self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {k}").get_object(f"Prevention {k} icon").show = False
        self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {k}").get_object(f"Prevention {k} Rectangle").show = False
        self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} Rectangle").clignotement = False
    for i in range(len(prevention_queue)) :
        self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} text").text = prevention_queue[i][0]
        self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} text").show = True
        self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} icon").show = True
        self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} Rectangle").show = True
        self_Interface.container_storage["affichage"]["Prevention"].get_object(f"Prevention {i}").get_object(f"Prevention {i} Rectangle").clignotement = prevention_queue[i][1]

