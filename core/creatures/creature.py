
class Creature():

    nom = "Sans nom"

    def __init__(self,position):
        self.pos=position

    def action(self,monde):
        pass

    def getColor(self): # la fonction getColor utillisé par PygameGUI
        if self.nom == "Loup":return (255,104,104)
        if self.nom == "Mouton":return (255,104,104)