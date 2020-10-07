################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################

from core.environnement.herbe import Herbe
from core.creatures.loup import Loup
from core.creatures.mouton import Mouton
from random import randint

#######################################################################################################################################

################################################# CREATION D'UNE CLASSE MONDE #########################################################

class Monde:

    """
    La classe monde est la classe qui s'occupe de la simulation.

    Attributs :
        dimentions : tuple indiquant la taille de la carte
        carte : un tableau à 2 dimentions qui contient l'Herbe
        carte_entitee = liste d'instance qui herite de créature

    Methodes :
        iteration() : exécute une iteration du monde
        get_entitee_at(position) : retourne une liste des entitées d'une position demandée.
        get_entitee_of(type_) : retourne une liste de toutes les entitées d'un certain type.
        get_herbe_at(position) : retourne l'herbe d'une position demandée.
        generate(entite,pourcentage): retourne une liste d'entite instancie pour chaque position de self.dimentions
    """

############################ CREATION DE LA FONCTION D'INITIALISATION DE LA CLASSE MONDE AVEC SES ATTRIBUTS ############################

    def __init__(self,dimentions=(20,20)):

        #Initialisation des attributs
        self.dimentions = dimentions
        self.carte = self.generate(Herbe,100) # Génération du monde à 100% d'herbe
        self.carte_entitee = self.generate(Loup,10) # Génère un tableau contenant 10% de loups
        self.carte_entitee.extend(self.generate(Mouton,30)) # Génère un tableau contenant 30% de moutons

########################################################################################################################################

############################################# DEFINITION DES METHODES DE LA CLASSE MONDE ###############################################

    #Création d'une méthode itération lancée automatiquement dans le fichier GUI.py
    def iteration(self):
        """
        Execute une iteration du monde où chaque entité lance son action.
        """
        self.carte_entitee_buf = []

        for x in self.carte_entitee:
            if self.carte_entitee.count(x) > 1: self.carte_entitee.remove(x)

        # Action de l'herbe
        for y in self.carte:
            for element in y:
                element.action()

        # Action des animaux
        for x in self.carte_entitee:
            x.action()
        self.carte_entitee.extend(self.carte_entitee_buf) # ajout des naissances, car si on les ajoutes directement ils se font executer.


    # Méthode qui retourne une liste d'entités à une position demandée en paramètres
    def get_entites_at(self,position):
        """
        Retourne les entites situées à une certaine position et retourne None sinon.
        """
        Entites_En_Position = []
        for entites in self.carte_entitee:
            # Si la position en paramètre est égale à la position d'une entitée, alors on rajoute cette dernière à la liste.
            if entites.pos[0]==position[0] and entites.pos[1]==position[1]:
                Entites_En_Position.append(entites)
        if Entites_En_Position == []:return None
        return Entites_En_Position

    # Méthode qui retourne une liste de toute les entitées d'une classe
    def get_entites_of(self,type_):
        """
        Retourne les entitées d'un certain type et retourne None sinon.
        """
        return [x for x in self.carte_entitee if isinstance(x,type_)]

    # Méthode qui retourne une liste contenant la position de chaque bloc d'herbe
    def get_herbe_at(self,position):
        """
        Renvoie l'herbe à une certaine position.
        """
        return self.carte[position[0]][position[1]]


    # Méthode générant toutes les entitées( herbe, mouton, loup)
    def generate(self,entite,pourcentage):
        """
        Génère un pourcentage d'entitées sur des positions de self.dimentions.
        Si l'entitée est de l'herbe, elle retourne un tableau à 2 dimentions d'herbe.
        """
        if entite == Herbe:
            return [[Herbe(self) for y in range(self.dimentions[1]) ]for x in range(self.dimentions[0])]
        else:
            return [entite([randint(0,self.dimentions[0]-1),randint(0,self.dimentions[1]-1)],self) for x in range(self.dimentions[0]+self.dimentions[1]) if randint(0,100)<pourcentage]

###################################################################################################################################################################################################

###################################################################################################################################################################################################




