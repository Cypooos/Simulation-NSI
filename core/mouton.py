from core.element import Element
from random import randint


class Mouton(Element):

    gain_nouritture = 4
    taux_reproduction = 4

    def __init__(self):
        self.energie = randint(1,self.gain_nouritture*2)


    def action(self):
        pass  
        
    def variationEnergie(self,herbe):
        if self.position() != "de tout les blocs d'herbe"():
            self.energie-=1
        else:
            self.energie+=gain_nouritture
            herbe.dead()
        return self.energie