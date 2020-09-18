from core.element import Element



class Herbe(Element):

    duree_repousse = 30

    def __init__(self):
        self.pousse_time = 0
        self.quantite = 0

    def action(self):
        pass

    def dead(self):
        self.quantite -= 10