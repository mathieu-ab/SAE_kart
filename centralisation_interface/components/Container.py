from module_import import *
from config import *
from components.Text import Text

class Container :
    def __init__(
            self,
            label: str, #nom de l'objet pour poivoir le récupéré facilement
            show_label: str, #affiche ou non le label du container en haut à droite
            position: tuple,
            size: tuple,
            show: bool,
            allignement: str #defini l'allignement des object dans le container ["horizontal", "vertical"]
    ):
        self.label = label
        self.position = position
        self.size = size
        self.show = show #affiche ou non le container (le carré autour) Les objets à l'interieur seront toujours affiché
        self.allignement = allignement
        self.objects = []
        if show_label :
            self.add_object(Text(
                    label=f"Title_container_{self.label}",
                    text=self.label,
                    font_name="Roboto-Bold",
                    font_size=11,
                    color=dark_light_mode["text"][dark_light_mode["etat"]],
                    justify="left"
                    ),
                relative_position=(10,10))
        self.pygame_rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])



    def add_object(self, object, relative_position) :
        self.objects.append({"object" : object,
                            "relative_position" : relative_position})
        if relative_position == None :
            self.reCalcule_position()
        else :
            self.objects[-1]["object"].set_position((
                self.position[0]+relative_position[0],
                self.position[1]+relative_position[1]
            ))



    def reCalcule_position(self) :
        nb_object = self.get_nb_not_relative_object()
        if self.allignement == "horizontal" :
            priority_axe = 0
        else :
            priority_axe = 1

        length_total_objects = 0 #somme de longeur des object selon l'axe principale d'allignement
        for objt in self.objects :
            if objt["relative_position"] == None :
                length_total_objects+=objt["object"].get_size()[priority_axe] #on obtient la taille principale de l'objet en fonction de son allignement (pour horizontal, on prend l'axe x)
        
        left_space_length = (self.size[priority_axe]-length_total_objects)/(nb_object+1)
        if left_space_length < 0 :
            print(f"Warning : l'objet {self.label} contient des object qui dépasse du container. Taille cumulé objet : {length_total_objects}, taille container : {self.size[priority_axe]}")
        
        cumule_position = left_space_length
        for objt in self.objects :
            if objt["relative_position"] == None :
                #calcule en x et y de la nouvelle position de l'object
                new_pos_object = [self.position[0],self.position[1]]
                new_pos_object[priority_axe] += cumule_position
                new_pos_object[1-priority_axe] = self.position[1-priority_axe]+(self.size[1-priority_axe]-objt["object"].get_size()[1-priority_axe])/2
                cumule_position+=objt["object"].get_size()[priority_axe]+left_space_length
                objt["object"].set_position(new_pos_object)
    
    def get_nb_not_relative_object(self) :
        nb_object = 0
        for objt in self.objects :
            if objt["relative_position"] == None :
                nb_object+=1
        return nb_object

    
    def get_object(self, object_label) :
        for objt in self.objects :
            if objt["object"].label == object_label :
                return objt["object"]
        print(f"Erreur : L'objet {object_label} n'a pas été trouvé dans le container {self.label}")

    def draw(self, window) :
        if self.show :
            pygame.draw.rect(
                window,
                dark_light_mode["container"][dark_light_mode["etat"]],
                self.pygame_rect,
                border_radius=10)
     
        for objt in self.objects :
            objt["object"].draw(window)