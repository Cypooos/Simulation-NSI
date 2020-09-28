from core.environnement.herbe import Herbe
from core.creatures.loup import Loup
from core.creatures.mouton import Mouton
from random import randint

class Monde:

    """
    La classe qui s'occupe de la simulation
    """

    def __init__(self,dimentions=(20,20)):
        self.dimentions = dimentions
        self.carte = self.generate(Herbe,100) # generation du monde a 100% d'herbe
        self.carte_entitee = self.generate(Loup,15) # genere un tableau de loup contenant 10% de loup
        self.carte_entitee.extend(self.generate(Mouton,30)) # genere un tableau de moutons contenant 30% de moutons

    def iteration(self):

        """
        Execute une iteration du monde.
        """
        # Action de l'herbe (grandir)
        for y in self.carte:
            for element in y:
                element.action()
        # Action des animaux
        for x in self.carte_entitee:
            x.action()


    def get_entite_at(self,position):
        """
        Retourne une entitee situe en <position>. Retourner None sinon
        """
        Entites_En_Position = None
        for entites in self.carte_entitee:
            if entites.pos[0]==position[0] and entites.pos[1]==position[1]:
                Entites_En_Position = entites
        return Entites_En_Position

    def get_entites_of(self,type_):
        """
        Retourne les entites de type <type>. Retourner None sinon
        """
        return [x for x in self.carte_entitee if isinstance(x,type_)]

    def get_herbe_at(self,position):
        """
        Obtenir l'Herbe en <position>
        """
        return self.carte[position[0]][position[1]]

    def generate(self,entite,pourcentage):
        """
        Genere pourcentage de entite sur des positions de self.dimentions
        """
        if entite == Herbe:
            return [[Herbe(self) for y in range(self.dimentions[1]) ]for x in range(self.dimentions[0])]
        else:
            return [entite([randint(0,self.dimentions[0]-1),randint(0,self.dimentions[1]-1)],self) for x in range(self.dimentions[0]+self.dimentions[1]) if randint(0,100)<pourcentage]








