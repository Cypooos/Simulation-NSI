from core.mouton import Mouton

from core.herbe import Herbe
from core.loup import Loup
from core.mouton import Mouton


class Monde:

    """
    La classe qui s'occupe de XXX
    """

    def __init__(self,dimentions=(20,20)):
        self.dimentions = dimentions
        self.carte = self.generate_world(60,30,10) # generation du monde à 60% d'herbe, 30% de mouton et 10% loups

    def iteration(self):
        """
        Execute une iteration du monde.
        """
        pass

    def generate_world(self,prct_herbes,prct_moutons,prct_loups):
        return [
            [[],[],[]],
            [[],[],[]],
            [[],[],[]],
            [[],[],[]],
            [[],[],[]],
        ]

    
    





