
class Creature():

    nom = "Sans nom"

    def __init__(self,position,monde):
        self.pos=position
        self.monde = monde

    def action(self):  # methode action appeler danss monde mais ecraser par les sous class
        self.pos[0]+=1

    def getColor(self): # la fonction getColor utillise par PygameGUI
        if self.nom == "Loup":return (234,227,226),0.5
        if self.nom == "Mouton":return (255,88,149),0.4

    def getAround(self,entite_to_seek):  # fonction de recherche des entitees autour de l'entitee self en parametre (8 blocs autour)
        """
        Retourne la position des entites a cote de soi qui sont de type entite_to_seek
        """
        for x in range(-1,2):
            for y in range(-1,2):
                if x==y==0:continue # ne pas tester sa propre position
                pos_to_seek = ((self.pos[0]+x )%self.monde.dimentions[0],(self.pos[1]+y )%self.monde.dimentions[1])

                if  self.monde.get_entites_at(pos_to_seek) == None:continue
                if any([isinstance(x, entite_to_seek) for x in self.monde.get_entites_at(pos_to_seek)]):
                    return pos_to_seek # retour de la position de l'entitee en question si c'est un mouton
        return None


    def getAround_Herbe(self):  # fonction de recherche des blocs herbes ayant la plus grande quantite autour de l'entitee self en parametre (4 bloc pas de diagonal)
        """
        Retourne la position des herbes Ã  cote de soi.
        """
        liste=[]
        for x in range(-1,2):
            for y in range(-1,2):
                if x==y==0:continue # ne pas tester sa propre position
                if x==-1 and y==-1:continue #ne pas tester les coins pour les moutons
                if x==1 and y==-1:continue
                if x==1 and y==1:continue
                if x==-1 and y==1:continue

                pos_to_seek = [(self.pos[0]+x )%self.monde.dimentions[0],(self.pos[1]+y )%self.monde.dimentions[1]]

                if (self.monde.get_herbe_at(pos_to_seek)):
                    liste.append(self.monde.get_herbe_at(pos_to_seek))

        herbe_max = sorted(liste, key=lambda entite_to_seek: entite_to_seek.getQuantite(), reverse=True)

        for x in range(-1,2):
            for y in range(-1,2):
                if x==y==0:continue
                pos_to_seek = [(self.pos[0]+x )%self.monde.dimentions[0],(self.pos[1]+y )%self.monde.dimentions[1]]
                if self.monde.get_herbe_at(pos_to_seek) == herbe_max[0]:
                    return pos_to_seek # retour de la position du bloc d'herbe en question

    def dead(self): #fonction de mort des entitees
        for i,x in enumerate(self.monde.carte_entitee):
            if x == self:
                del self.monde.carte_entitee[i]
                break