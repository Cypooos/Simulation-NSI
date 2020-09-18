from core.creature import Creature


# pas besoin de hÃ©ritÃ© de Element, L'herbe est si diffÃ©rente.
class Herbe():

    nom = "Herbe"
    duree_repousse = 30

    def __init__(self):
        self.quantite = 0

    def action(self): # L'herbe ne ce dÃ©place pas, juste regÃ©nÃ¨re.
        self.quantite += 1

    def dead(self):
        self.quantite = 0