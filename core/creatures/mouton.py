"""
ProblÃ¨me de dÃ©placement des moutons (En Cours de RÃ©solution: AurÃ©lien)

Je pense que Ã§a vient de la nouvelle dÃ©finitio de Marc. On verra Ã§a ensemble demain
mais je vais commencer Ã  y rÃ©flÃ©chir.

"""

from core.creatures.creature import Creature
from core.environnement.herbe import Herbe
from random import randint


class Mouton(Creature):

    nom = "Mouton"
    taux_reproduction = 80
    start_energie = 20


    def __init__(self,position,monde,can_move=True):
        self.energie = randint(self.start_energie,self.start_energie*2)
        self.pos = position
        self.monde = monde
        self.can_move = can_move


    def action(self):
        """
        Mange de l'herbe, bouge et essaie de ce reproduire.
        Il gagne herbe.quantite energie quand il mange et ce reproduit quand il a assez d'energie
        """

        if not self.can_move:
            print("I can't get uppp")
            self.can_move = True
            return

        self.energie-=1 #perte d'energie par tour
        if self.energie <= 0:self.dead() # mourrir


        if self.getAround_Herbe(Herbe)!= None:
            var = self.getAround_Herbe(Herbe)
            self.pos[0] = var[0]
            self.pos[1] = var[1]

        self.pos[0] %= self.monde.dimentions[0]
        self.pos[1] %= self.monde.dimentions[1]

        herbe = self.monde.get_herbe_at(self.pos)
        if herbe == None:self.energie-=1
        else:
            self.energie += herbe.quantite
            herbe.dead()



