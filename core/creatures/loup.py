from core.creatures.creature import Creature
from core.creatures.mouton import Mouton
from random import randint


class Loup(Creature):

    nom = "Loup"
    gain_nouritture = 30
    taux_reproduction = 5

    def __init__(self,position,monde):
        self.energie = randint(1,self.gain_nouritture*2)
        self.pos = position
        self.monde = monde


    def action(self):

        self.energie -= 1
        if self.energie <= 0:self.dead() # mourrir

        if self.getAround(Mouton) != None:
            var = self.getAround(Mouton)
            self.pos[0] = var[0]
            self.pos[1] = var[1]

            mouton = [x for x in self.monde.get_entites_at(var) if isinstance(x,Mouton)][0] # tuer le mouton
            mouton.dead()
            self.energie += randint(self.gain_nouritture,self.gain_nouritture*2)
        else:
            self.pos[0]+=randint(-1,1)
            self.pos[1]+=randint(-1,1)

        self.pos[0] %= self.monde.dimentions[0]
        self.pos[1] %= self.monde.dimentions[1]







