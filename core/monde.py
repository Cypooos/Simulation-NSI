from core.environnement.herbe import Herbe # importation des modules necessaires
from core.creatures.loup import Loup
from core.creatures.mouton import Mouton
from random import randint

class Monde:

    """
    La classe qui s'occupe de la simulation

    Attributs :
        dimentions : tuple indiquant la taille de la map
        carte : tableau a 2 dimentions contenant l'Herbe
        carte_entitee = liste d'instance qui herite de Animal
    Methodes :
        iteration() : execute une iteration du monde
        get_entitee_at(position) : retourne une liste des entitees situe en postion
        get_entitee_of(type_) : retourne une liste de toute les entitee de type <type_>
        get_herbee_at(position) : retourne l'herbe en position <position>
        generate(entite,pourcentage): retourne une liste d'entite instancie pour chaque position de self.dimentions
    """

    def __init__(self,dimentions=(20,20)):
        self.dimentions = dimentions
        self.carte = self.generate(Herbe,100) # generation du monde a 100% d'herbe
        self.carte_entitee = self.generate(Loup,10) # genere un tableau de loup contenant 10% de loup
        self.carte_entitee.extend(self.generate(Mouton,30)) # genere un tableau de moutons contenant 30% de moutons

    def iteration(self): # fonction iteraction lancer automatiquement dans GUI.py ou chaque entite lance son action
        """
        Execute une iteration du monde.
        """
        self.carte_entitee_buf = []

        for x in self.carte_entitee:
            if self.carte_entitee.count(x) > 1: self.carte_entitee.remove(x)

        # Action de l'herbe (grandir)
        for y in self.carte:
            for element in y:
                element.action()
        # Action des animaux
        for x in self.carte_entitee:
            x.action()
        self.carte_entitee.extend(self.carte_entitee_buf) # ajout des naissances, car si on les ajoutes directement ils se font executer. 


    def get_entites_at(self,position): # Fonction qui retourne une liste des entitees en position demander en parametre
        """
        Retourne les entites situe en <position>. Retourner None sinon
        """
        Entites_En_Position = []
        for entites in self.carte_entitee:
            if entites.pos[0]==position[0] and entites.pos[1]==position[1]:
                Entites_En_Position.append(entites)
        if Entites_En_Position == []:return None
        return Entites_En_Position

    def get_entites_of(self,type_):# retourne une liste de toute les entitee d'une class
        """
        Retourne les entites de type <type>. Retourner None sinon
        """
        return [x for x in self.carte_entitee if isinstance(x,type_)]

    def get_herbe_at(self,position): # retourne une liste contenant la position de chaque herbe
        """
        Obtenir l'Herbe en <position>
        """
        return self.carte[position[0]][position[1]]

    def generate(self,entite,pourcentage): # genere toute les entitees ( herbe, mouton, loup)
        """
        Genere pourcentage de entite sur des positions de self.dimentions.
        Si l'entitee est de l'herbe, elle retourne un tableau a 2 dimentions d'herbe.
        """
        if entite == Herbe:
            return [[Herbe(self) for y in range(self.dimentions[1]) ]for x in range(self.dimentions[0])]
        else:
            return [entite([randint(0,self.dimentions[0]-1),randint(0,self.dimentions[1]-1)],self) for x in range(self.dimentions[0]+self.dimentions[1]) if randint(0,100)<pourcentage]







