from core.creature import Creature
from random import randint

# pas besoin de herite de Element, L'herbe est si differente.
class Herbe():

    nom = "Herbe"
    max_repousse = 30

    def __init__(self):
        self.quantite = randint(0,self.max_repousse)
    
    def getColor(self):
        """Retourne la couleur de l'herbe pour PygameGUI"""
        # 100% verte : rgb 66, 245, 72
        # 100% morte : rgb 191, 191, 101
        ratio = self.quantite / self.max_repousse

        red = 66*ratio+191*(1-ratio)
        vert = 245*ratio+191*(1-ratio)
        bleu = 72*ratio+101*(1-ratio)
        return (red,vert,bleu)

    def action(self,monde): # L'herbe ne ce deplace pas, juste regenere.
        self.quantite += 1
        if self.quantite > self.max_repousse:self.quantite = self.max_repousse
        

    def dead(self):
        self.quantite = 0