from random import randint

class Herbe():

    nom = "Herbe"
    max_repousse = 100

    def __init__(self,monde):
        self.quantite = randint(0,self.max_repousse)
        self.monde = monde

    def getColor(self):
        """
        Retourne la couleur de l'herbe pour PygameGUI
        """
        # 100% verte : rgb 66, 245, 72
        # 100% morte : rgb 161, 140, 72
        ratio = self.quantite / self.max_repousse

        red = 66*ratio+161*(1-ratio)
        vert = 245*ratio+140*(1-ratio)
        bleu = 72*ratio+72*(1-ratio)
        return (red,vert,bleu)

    def getQuantite(self):
        return self.quantite

    def action(self): # L'herbe ne ce deplace pas, juste regenere.
        """
        Regeneration d'une quatite d'herbe.
        """
        self.quantite += 1
        if self.quantite > self.max_repousse:self.quantite = self.max_repousse


    def dead(self):
        self.quantite = 0