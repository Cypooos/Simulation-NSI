from core.creatures.creature import Creature
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
        pass

