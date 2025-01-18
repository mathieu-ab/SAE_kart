from module_import import *


class Container :
    def __init__(
            self,
            label: str,
            position: tuple,
            size: tuple,
            show: bool,
            allignement: str #defini l'allignement des object dans le container ["horizontal", "vertical"]
    ):
        self.label = label
        self.position = position
        self.size = size
        self.show = show
        self.allignement = allignement
        self.objects = []
        


    def add_object(self, object) :
        self.objects.append(object)
        self.reCalcule_position()



    def reCalcule_position(self) :
        nb_object = len(self.objects)
        #placement des objets en x
        if self.allignement == "horizontal" :
            priority_axe = 0 
        else :
            priority_axe = 1
        
        length_total_objects = 0 #somme de longeur des object selon l'axe principale d'allignement
        for objt in self.objects :
            length_total_objects+=objt.get_size()[priority_axe] #on obtient la taille principale de l'objet en fonction de son allignement (pour horizontal, on prend l'axe x)
        
        left_space_length = (self.size[priority_axe]-length_total_objects)//(nb_object+1)
        if left_space_length < 0 :
            print(f"Warning : l'objet {self.label} contient des object qui dépasse du container. Taille cumulé objet : {length_total_objects}, taille container : {self.size[priority_axe]}")
        
        i = 1
        cumule_position = left_space_length
        for objt in self.objects :
            #calcule en x et y de la nouvelle position de l'object
            new_pos_object = [0,0]
            new_pos_object[priority_axe] = left_space_length*i
            new_pos_object[1-priority_axe] = (self.size[1-priority_axe]-objt.get_size()[1-priority_axe])//2
            cumule_position+=objt.get_size()[priority_axe]+left_space_length
            objt.set_size(new_pos_object)
            i+=1