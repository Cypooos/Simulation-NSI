################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################

from core.creatures.creature import Creature # importation des modules necessaires
from core.creatures.mouton import Mouton
from random import randint

#######################################################################################################################################

################################################# CREATION DE LA CLASSE LOUP ##########################################################

#Création de la classe Loup qui hérite de la classe Creature
class Loup(Creature):
    """
    La classe Loup est la classe qui s'occupe de la gestion des loups.

    Attributs communs à toutes les instances:
        nom: nom permettant d'appeler les loups dans les autres fichiers.
        reproduction_energie: valeur énergétique nécessaire à un loup pour pouvoir se reproduire.
        start_energie: tuple de deux valeurs entre lesquelles on chosira un entier aléatoire qui donnera l'énergie
        d'un loup au départ.
        max_energie: le maximum d'énergie qu'un loup peut avoir.
        lose_energie: l'énergie que perd un loup à chaque itération.

    Attributs :
        energie : energie d'un loup au départ.
        pos: tuple contenant la position d'un loup au départ
        monde: valeur contenant le pourcentage de loups dans le monde (définie dans la classe monde).

    Methodes :
        action(): crée toutes les actions des loups (nourriture, reproduction, déplacement...)
    """

    # Création des attributs communs à toutes les instances
    nom = "Loup"
    reproduction_energie = 250
    start_energie = (80,130)
    gain_energie = (50,70)
    max_energie = 300
    lose_energie = (4,8)

############################ CREATION DE LA FONCTION D'INITIALISATION DE LA CLASSE LOUP AVEC SES ATTRIBUTS ############################

    # Initialisation des attributs de la class Loup
    def __init__(self,position,monde,energie=None):
        self.energie = energie
        if self.energie == None:self.energie = randint(self.start_energie[0],self.start_energie[1])
        self.pos = position
        self.monde = monde

#######################################################################################################################################

############################################ DEFINITION DE LA METHODE DE LA CLASSE LOUP ###############################################
    #Méthode gérant les actions des loups, appellée dans monde.py
    def action(self):
        """
        Méthode permettant au loup de manger de l'herbe, bouger et essayer de se reproduire.
        """

        # Si une position est retournée par la fonction
        if self.getAround(Mouton) != None:
            var = self.getAround(Mouton)
            self.pos[0] = var[0]
            self.pos[1] = var[1]

            # Si un mouton se trouve sur la position de self, mouton devient l'entitée en question
            mouton = [x for x in self.monde.get_entites_at(var) if isinstance(x,Mouton)][0]
            mouton.dead()
            self.energie += randint(self.gain_energie[0],self.gain_energie[1])

        # Sinon se déplacer aléatoirement
        else:
            self.pos[0]+=randint(-1,1)
            self.pos[1]+=randint(-1,1)

        #Si self.energie supérieur à max_energie, alors self.energie prend la valeur de max_energie
        if self.energie > self.max_energie:self.energie = self.max_energie

        self.energie-=randint(self.lose_energie[0],self.lose_energie[1])

        # Condition qui apelle la fonction de mort
        if self.energie <= 0:self.dead()

        self.pos[0] %= self.monde.dimentions[0]
        self.pos[1] %= self.monde.dimentions[1]

        # Condition pour la reproduction, si self.energie est supérieure à reproduction_energie
        if self.energie > self.reproduction_energie:
            self.energie //= 2
            self.monde.carte_entitee_buf.append(Loup([(self.pos[0]+randint(-1,1))%self.monde.dimentions[0],(self.pos[1]+randint(-1,1))%self.monde.dimentions[1]],self.monde,self.energie))

#######################################################################################################################################

#######################################################################################################################################





