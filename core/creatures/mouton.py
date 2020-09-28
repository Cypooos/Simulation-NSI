from core.creatures.creature import Creature
from core.environnement.herbe import Herbe
from random import randint


class Mouton(Creature):

    nom = "Mouton"
    taux_reproduction = 4
    start_energie = 20
    lose_energi = (5,20)


    def __init__(self,position,monde):
        self.energie = randint(1,self.start_energie*2)
        self.pos = position
        self.monde = monde


    def action(self):
        """
        Mange de l'herbe, bouge et essaie de ce reproduire.
        Il gagne herbe.quantite energie quand il mange et ce reproduit quand il a plus de can_reproduce_from
        """
        herbe = self.monde.get_herbe_at(self.pos)
        if herbe == None:
            self.energie-=1
        else:
            self.energie += herbe.quantite
            herbe.dead()
        self.pos[0]+=1
        self.getAround(Herbe)