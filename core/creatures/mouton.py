from core.creatures.creature import Creature
from core.environnement.herbe import Herbe
from random import randint


class Mouton(Creature):

    nom = "Mouton"
    taux_reproduction = 4
    start_energie = 20
    lose_energie = (5,20)


    def __init__(self,position,monde):
        self.energie = randint(self.start_energie,self.start_energie*2)
        self.pos = position
        self.monde = monde


    def action(self):
        """
        Mange de l'herbe, bouge et essaie de ce reproduire.
        Il gagne herbe.quantite energie quand il mange et ce reproduit quand il a plus de can_reproduce_from
        """
        
        self.energie -= randint(self.lose_energie[0],self.lose_energie[1])
        if self.energie <= 0:self.dead() # mourrir

        herbe = self.monde.get_herbe_at(self.pos)
        if herbe == None:self.energie-=1
        else:
            self.energie += herbe.quantite
            herbe.dead()
        i=randint(0,1)
        if i==0:
            self.pos[0]+=randint(-1,1)
        else:
            self.pos[1]+=randint(-1,1)

        self.pos[0] %= self.monde.dimentions[0]
        self.pos[1] %= self.monde.dimentions[1]
        #self.getAround(Herbe)