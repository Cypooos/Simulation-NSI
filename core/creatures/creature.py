
class Creature():

    nom = "Sans nom"

    def __init__(self,position,monde):
        self.pos=position
        self.monde = monde

    def action(self):
        self.pos[0]+=1




    def getColor(self): # la fonction getColor utillisÃƒÂ© par PygameGUI
        if self.nom == "Loup":return (133, 133, 133)
        if self.nom == "Mouton":return (251, 196, 255)




    def getAround(self,entite_to_seek):
        """
        Retourne la position des entites a cote de soi qui sont de type entite_to_seek
        """
        for x in range(-1,2):
            for y in range(-1,2):
                if x==y==0:
                    continue # ne pas tester sa propre position
                pos_to_seek = ((self.pos[0]+x )%self.monde.dimention[0],(self.pos[1]+y )%self.monde.dimention[1])

                if isinstance(self.monde.get_entite_at(pos_to_seek), entite_to_seek):
                    return x,y
        return None
