import copy
"""
Probleme de deplacement des moutons (En Cours de RÃ©solution: AurÃ©lien)

Je pense que Ã§a vient de la nouvelle dÃ©finitio de Marc. On verra Ã§a ensemble demain
mais je vais commencer Ã  y rÃ©flÃ©chir.

"""

from core.creatures.creature import Creature
from core.environnement.herbe import Herbe
from random import randint


class Mouton(Creature):

    nom = "Mouton"
    reproduction_energie = 160
    start_energie = (80,130)
    max_energie = 200
    lose_energie = (10,30)


    def __init__(self,position,monde,energie = None):
        self.energie = energie
        if self.energie == None:self.energie = randint(self.start_energie[0],self.start_energie[1])
        self.pos = position
        self.monde = monde


    def action(self):
        """
        Mange de l'herbe, bouge et essaie de ce reproduire.
        Il gagne herbe.quantite energie quand il mange et ce reproduit quand il a assez d'energie
        """

        herbe = self.monde.get_herbe_at(self.pos)
        self.energie += herbe.quantite
        herbe.dead()

        if self.energie > self.max_energie:self.energie = self.max_energie

        self.energie-=randint(self.lose_energie[0],self.lose_energie[1])
        if self.energie <= 0:self.dead() # mourrir

        var = self.getAround_Herbe()
        self.pos[0] = var[0]
        self.pos[1] = var[1]

        self.pos[0] %= self.monde.dimentions[0]
        self.pos[1] %= self.monde.dimentions[1]

        if self.energie > self.reproduction_energie:
            self.energie //= 2
            self.monde.carte_entitee_buf.append(Mouton([(self.pos[0]+randint(-1,1))%self.monde.dimentions[0],(self.pos[1]+randint(-1,1))%self.monde.dimentions[1]],self.monde,self.energie))




