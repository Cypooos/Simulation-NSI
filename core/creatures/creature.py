
class Creature():

    nom = "Sans nom"

    def __init__(self,position):
        self.pos=position

    def action(self,monde):
        pass

    def getColor(self): # la fonction getColor utillisé par PygameGUI
        if self.nom == "Loup":return (133, 133, 133)
        if self.nom == "Mouton":return (251, 196, 255)