
class Creature():

    nom = "Sans nom"

    def __init__(self,position,monde):
        self.pos=position
        self.monde = monde

    def action(self):
        self.pos[0]+=1

    def getColor(self): # la fonction getColor utillise par PygameGUI
        if self.nom == "Loup":return (133, 133, 133),0.5
        if self.nom == "Mouton":return (251, 196, 255),0.4

    def getAround(self,entite_to_seek):
        """
        Retourne la position des entites a cote de soi qui sont de type entite_to_seek
        """
        for x in range(-1,2):
            for y in range(-1,2):
                if x==y==0:continue # ne pas tester sa propre position
                pos_to_seek = ((self.pos[0]+x )%self.monde.dimentions[0],(self.pos[1]+y )%self.monde.dimentions[1])

                if  self.monde.get_entites_at(pos_to_seek) == None:continue
                if any([isinstance(x, entite_to_seek) for x in self.monde.get_entites_at(pos_to_seek)]):
                    return pos_to_seek
        return None


    def getAround_Herbe(self,entite_to_seek):
        """
        Retourne la position des entites a cote de soi qui sont de type entite_to_seek
        """
        liste=[]
        for x in range(-1,2):
            for y in range(-1,2):
                if x==y==0:continue # ne pas tester sa propre position
                pos_to_seek = [(self.pos[0]+x )%self.monde.dimentions[0],(self.pos[1]+y )%self.monde.dimentions[1]]

                if (self.monde.get_herbe_at(pos_to_seek)):
                    liste.append(self.monde.get_herbe_at(pos_to_seek))

        herbe_max = sorted(liste, key=lambda entite_to_seek: entite_to_seek.getQuantite(), reverse=True)
        for x in range(-1,2):
            for y in range(-1,2):
                if x==y==0:continue
                pos_to_seek = [(self.pos[0]+x )%self.monde.dimentions[0],(self.pos[1]+y )%self.monde.dimentions[1]]

                if self.monde.get_herbe_at(pos_to_seek) == herbe_max[0]:
                    print(pos_to_seek)
                    return pos_to_seek



    def dead(self):
        for i,x in enumerate(self.monde.carte_entitee):
            if x == self:
                del self.monde.carte_entitee[i]
                break