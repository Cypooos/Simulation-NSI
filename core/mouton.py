from core.element import Element
from random import randint


class Mouton(Element):

    gain_nouritture = 4
    taux_reproduction = 4

    def __init__(self):
        self.energie = randint(1,self.gain_nouritture*2)


    def action(self):
        pass
        