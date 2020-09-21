from core.environnement.herbe import Herbe
from core.creatures.loup import Loup
from core.creatures.mouton import Mouton

from random import randint

class Monde:

    """
    La classe qui s'occupe de XXX
    """

    def __init__(self,dimentions=(20,20)):
        self.dimentions = dimentions
<<<<<<< Updated upstream
        self.carte = self.generate(Herbe,100) # generation du monde Ã  100% d'herbe
        self.carte_entitee = self.generate(Loup,10) # gÃ©nÃ¨re un tableau de loup contenant 10% de loup
        self.carte_entitee.extend(self.generate(Mouton,30)) # gÃ©nÃ¨re un tableau de moutons contenant 30% de moutons
=======
        self.carte = self.generate(Herbe,100) # generation du monde à 100% d'herbe
        self.carte_entitee = self.generate(Loup,15) # génère un tableau de loup contenant 10% de loup
        self.carte_entitee.extend(self.generate(Mouton,30)) # génère un tableau de moutons contenant 30% de moutons
>>>>>>> Stashed changes

    def iteration(self):
        """
        Execute une iteration du monde.
        """
        # Action de l'herbe (grandir)
        for y in self.carte:
            for x in y:
                self.carte[y][x].action()
        # Action des animaux
        for x in self.carte_entitee:
            x.action()

    def get_entites(self,position):

        Entites_En_Position=[]
        for entites in self.carte_entitee:
            if entites.pos==position:
                Entites_En_Position.append(entites)
        """
<<<<<<< Updated upstream
        Retourne une liste des entitee situÃ© en <position>. Retourner un tableau vide sinon
=======
        Retourne une liste des entites situé en <position>. Retourner un tableau vide sinon
>>>>>>> Stashed changes
        """
        return Entites_En_Position

    def get_herbe(self,position):
        """
        Obtenir l'Herbe en <position>
        """
        return self.carte[position[1]][position[0]]

    def generate(self,entite,pourcentage):
        """
        GÃ©nÃ¨re pourcentage de entitÃ© sur des positions de self.dimentions par self.dimentions
        """
        if entite == Herbe:
            return [[Herbe() for y in range(self.dimentions[1]) ]for x in range(self.dimentions[0])]
        else:
            return [entite((randint(0,self.dimentions[0]),randint(0,self.dimentions[1]))) for x in range(self.dimentions[0]+self.dimentions[1]) if randint(0,100)<pourcentage]








