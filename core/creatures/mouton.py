from core.creatures.creature import Creature
from random import randint


class Mouton(Creature):

    nom = "Mouton"
    gain_nouritture = 4
    taux_reproduction = 4

    def __init__(self,position):
        self.energie = randint(1,self.gain_nouritture*2)
        self.pos = position


    def action(self,monde): # Oula cette fonction est a refaire ^^ D'ailleurs, c'est dans self.action() qu'il faut coder Ã§a
        herbe = monde.get_herbe(self.pos)
        if herbe == None: self.energie-=1
        else:
            self.energie += self.gain_nouritture
            herbe.dead()