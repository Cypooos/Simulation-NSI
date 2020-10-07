################################################# CREATION D'UNE CLASSE MONDE #############################################################

class Creature(): #creation de la class Creature
    """
    La classe Créature est la classe gérant les aimaux et de laquelle ils héritent.

    Attributs :
        pos: tuple contenant la position d'une créature au départ
        monde: valeur contenant le pourcentage d'une créature dans le monde (définie dans la classe monde).

    Methodes :
        action(): appellée dans monde, elle est écrasée par les méthodes de loup et mouton.
        getColor(): crée la couleur et la taille des points repérsentants les créatures sur PygameGUI
        getAround():recherchant des entitées autour de l'entitée self en paramètre (8 blocs autours)
        getAroundHerbe(): recherche les blocs d'herbe qui ont la plus grande quantite autour de l'entité self en parametre (4 blocs pas de diagonale)
        dead(): gère la mort des entités.

    """
############################ CREATION DE LA FONCTION D'INITIALISATION DE LA CLASSE CREATURE AVEC SES ATTRIBUTS ############################

    # Initialisation des attributs de la classe Creature
    def __init__(self,position,monde):
        self.pos=position
        self.monde = monde

###########################################################################################################################################

############################################ DEFINITION DES METHODES DE LA CREATURE #######################################################

    # Méthode action appellée dans monde.py mais ecraser par les méthodes de loup et mouton.
    def action(self):
        self.pos[0]+=1

    # Méthode getColor crée la couleur et la taille des points repérsentants les créatures sur PygameGUI
    def getColor(self):
        if self.nom == "Loup":return (234,227,226),0.5
        if self.nom == "Mouton":return (255,88,149),0.4

    # Méthode recherchant des entitées autour de l'entitée self en paramètre (8 blocs autour)
    def getAround(self,entite_to_seek):
        """
        Retourne la position des entites proches d'une entité self qui sont de type "entite_to_seek"
        """
        for x in range(-1,2):
            for y in range(-1,2):

                # Ne teste pas sa propre position
                if x==y==0:continue
                pos_to_seek = ((self.pos[0]+x )%self.monde.dimentions[0],(self.pos[1]+y )%self.monde.dimentions[1])

                # Si il n'y a pas d'entité à la position que l'on recherche, on continue.
                if  self.monde.get_entites_at(pos_to_seek) == None:continue

                #Si il y a une entité dans la liste, on la retourne par la fonction get_entites_at
                if any([isinstance(x, entite_to_seek) for x in self.monde.get_entites_at(pos_to_seek)]):

                    #Si c'est un mouton, on retourne la position de l'entité
                    return pos_to_seek
        return None

    # Méthode qui recherche les blocs d'herbe qui ont la plus grande quantite autour de l'entité self en parametre (4 blocs pas de diagonale)
    def getAround_Herbe(self):
        """
        Retourne la position les blocs d' herbe qui ont la plus grande quantité à proximité.
        """
        liste=[]
        for x in range(-1,2):
            for y in range(-1,2):

                # Ne teste pas sa propre position
                if x==y==0:continue

                # Ne teste pas les coins pour les moutons
                if x==-1 and y==-1:continue
                if x==1 and y==-1:continue
                if x==1 and y==1:continue
                if x==-1 and y==1:continue

                pos_to_seek = [(self.pos[0]+x )%self.monde.dimentions[0],(self.pos[1]+y )%self.monde.dimentions[1]]

                # Si il y a des blocs d'herbe, ajout de l'objet dans la liste "liste"
                if (self.monde.get_herbe_at(pos_to_seek)):
                    liste.append(self.monde.get_herbe_at(pos_to_seek))

        # Tri de la liste en fonction de la quantité
        herbe_max = sorted(liste, key=lambda entite_to_seek: entite_to_seek.getQuantite(), reverse=True)

        for x in range(-1,2):
            for y in range(-1,2):

                # Ne pas tester sa propre position
                if x==y==0:continue
                pos_to_seek = [(self.pos[0]+x )%self.monde.dimentions[0],(self.pos[1]+y )%self.monde.dimentions[1]]

                #Si l'objet est égal à l'indice 0 dans herbe_max
                if self.monde.get_herbe_at(pos_to_seek) == herbe_max[0]:

                    # Retourne la position du bloc d'herbe en question
                    return pos_to_seek

    #Méthode de mort des entités.
    def dead(self):
        for i,x in enumerate(self.monde.carte_entitee):
            if x == self:
                del self.monde.carte_entitee[i]
                break

###########################################################################################################################################

###########################################################################################################################################