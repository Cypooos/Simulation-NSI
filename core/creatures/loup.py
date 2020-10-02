from core.creatures.creature import Creature
from core.creatures.mouton import Mouton
from random import randint


class Loup(Creature):

    nom = "Loup"
    reproduction_energie = 250
    start_energie = (80,130)
    gain_energie = (50,70)
    max_energie = 300
    lose_energie = (4,8)

    def __init__(self,position,monde,energie=None):
        self.energie = energie
        if self.energie == None:self.energie = randint(self.start_energie[0],self.start_energie[1])
        self.pos = position
        self.monde = monde


    def action(self):

        if self.getAround(Mouton) != None:
            var = self.getAround(Mouton)
            self.pos[0] = var[0]
            self.pos[1] = var[1]

            mouton = [x for x in self.monde.get_entites_at(var) if isinstance(x,Mouton)][0] # tuer le mouton
            mouton.dead()
            self.energie += randint(self.gain_energie[0],self.gain_energie[1])
        else:
            self.pos[0]+=randint(-1,1)
            self.pos[1]+=randint(-1,1)

        if self.energie > self.max_energie:self.energie = self.max_energie

        self.energie-=randint(self.lose_energie[0],self.lose_energie[1])
        if self.energie <= 0:self.dead() # mourrir

        self.pos[0] %= self.monde.dimentions[0]
        self.pos[1] %= self.monde.dimentions[1]

        
        if self.energie > self.reproduction_energie:
            self.energie //= 2
            self.monde.carte_entitee_buf.append(Loup([(self.pos[0]+randint(-1,1))%self.monde.dimentions[0],(self.pos[1]+randint(-1,1))%self.monde.dimentions[1]],self.monde,self.energie))







