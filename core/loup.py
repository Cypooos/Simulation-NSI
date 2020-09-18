from core.element import Element
from random import randint

class Loup(Element):

    gain_nouritture = 19
    taux_reproduction = 5

    def __init__(self):
        self.energie = randint(1,self.gain_nouritture*2)


    def action(self):
        pass

