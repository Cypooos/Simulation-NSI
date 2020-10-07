import copy # importation des modules necessaires


from core.creatures.creature import Creature #import de la class Creature pour héritage
from core.environnement.herbe import Herbe  # autre import necessaire
from random import randint


class Mouton(Creature): #creation de la classe Mouton qui herite de la classe Creature

    nom = "Mouton"
    reproduction_energie = 160  # creation des attributs de Mouton
    start_energie = (80,130)
    max_energie = 200
    lose_energie = (10,30)


    def __init__(self,position,monde,energie = None): # initialisation des attributs
        self.energie = energie
        if self.energie == None:self.energie = randint(self.start_energie[0],self.start_energie[1])
        self.pos = position
        self.monde = monde


    def action(self): # methode action appeler danss monde
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




