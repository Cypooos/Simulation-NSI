from core.element import Element


# pas besoin de hérité de Element, L'herbe est si différente.
class Herbe():

    nom = "Herbe"
    duree_repousse = 30

    def __init__(self):
        self.quantite = 0

    def action(self): # L'herbe ne ce déplace pas, juste regénère.
        self.quantite += 1

    def dead(self):
        self.quantite = 0