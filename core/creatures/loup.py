from core.creatures.creature import Creature
from core.creatures.mouton import Mouton
from random import randint


class Loup(Creature):

    nom = "Loup"
    gain_nouritture = 19
    taux_reproduction = 5

    def __init__(self,position,monde):
        self.energie = randint(1,self.gain_nouritture*2)
        self.pos = position
        self.monde = monde


    def action(self):
        if self.getAround(Mouton) != None:
            var = self.getAround(Mouton)
            self.pos[0] = var[0]
            self.pos[1] = var[1]







