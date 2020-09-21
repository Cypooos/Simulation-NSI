
class Creature():

    nom = "Sans nom"

    def __init__(self,position,monde):
        self.pos=position
        self.monde = monde

    def action(self):
        pass

    def getColor(self): # la fonction getColor utillisé par PygameGUI
        if self.nom == "Loup":return (133, 133, 133)
        if self.nom == "Mouton":return (251, 196, 255)

