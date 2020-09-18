from core.element import Element
from random import randint


class Mouton(Element):

    nom = "Mouton"
    gain_nouritture = 4
    taux_reproduction = 4

    def __init__(self,position):
        self.energie = randint(1,self.gain_nouritture*2)
        self.pos = position


    def action(self):
        pass  
        
    def variationEnergie(self,herbe): # Oula cette fonction est a refaire ^^ D'ailleurs, c'est dans self.action() qu'il faut coder ça
        if self.position() != "de tout les blocs d'herbe"():
            self.energie-=1
        else:
            self.energie+=gain_nouritture
            herbe.dead()
        return self.energie