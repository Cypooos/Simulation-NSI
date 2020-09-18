from core.environnement.herbe import Herbe
from core.creatures.loup import Loup
from core.creatures.mouton import Mouton


class Monde:

    """
    La classe qui s'occupe de XXX
    """

    def __init__(self,dimentions=(20,20)):
        self.dimentions = dimentions
        self.carte = self.generate(Herbe,100) # generation du monde à 100% d'herbe
        loups = self.generate(Loup,10) # génère un tableau de loup contenant 10% de loup
        moutons = self.generate(Mouton,30) # génère un tableau de moutons contenant 30% de moutons
        self.carte_entitee = loups.extend(moutons) # tableau des loups et moutons

    def iteration(self):
        """
        Execute une iteration du monde.
        """
        # Action de l'herbe (grandir)
        for y in self.carte:
            for x in y:
                self.carte[y][x].action(self)
        # Action des animaux
        for x in self.carte_entitee:
            x.action(self)

    def get_entites(self,position):
        """
        Retourne une liste des entitee situé en <position>. Retourner un tableau vide sinon
        """
        return []
    
    def get_herbe(self,position):
        """
        Obtenir l'Herbe en <position>
        """
        return self.carte[position[1]][position[0]]

    def generate(self,entite,pourcentage):
        """
        Génère pourcentage de entité sur des positions de self.dimentions par self.dimentions
        """
        if entite == Herbe:
            return [[Herbe() for y in range(self.dimentions[1]) ]for x in range(self.dimentions[0])]


        else:return [entite((0,0)), entite((2,2)), entite((0,2))]

    
    





