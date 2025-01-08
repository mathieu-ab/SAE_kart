#import des modules
from pygame.locals import *
import pygame
import time
import os






#--|--# lists/variables
CURRENT_PATH = os.getcwd()

#loop pour passer d'une page à une autre
main_loop = True
affichage_loop = True


fps = 20
#coordonées des boutons des différent mode en x
info_mode_conduite = {"eco" : 281, "normal" : 375, "sport" : 469}
#listes pour avoir les dégradé de couleur
# color_green_to_red = list(Color("#61ff01").range_to(Color("#ccff01"),15))
# color_green_to_red.extend(list(Color("#ccff01").range_to(Color("#fff001"),15)))
# color_green_to_red.extend(list(Color("#fff001").range_to(Color("#ffae01"),15)))
# color_green_to_red.extend(list(Color("#ffae01").range_to(Color("#ff6101"),15)))
# color_green_to_red.extend(list(Color("#ff6101").range_to(Color("#ff0101"),15)))


