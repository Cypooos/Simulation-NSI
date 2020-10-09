################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################
from core.creatures.creature import Creature #import de la class Creature pour héritage
from core.environnement.herbe import Herbe  # autre import necessaire
from random import randint

#######################################################################################################################################

################################################ CREATION DE LA CLASSE MOUTON #########################################################
class Mouton(Creature):
    """
    La classe Mouton est la classe qui s'occupe de la gestion des moutons.

    Attributs communs à toutes les instances:
        nom: nom permettant d'appeler les moutons dans les autres fichiers.
        reproduction_energie: valeur énergétique nécessaire à un mouton pour pouvoir se reproduire.
        start_energie: tuple de deux valeurs entre lesquelles on chosira un entier aléatoire qui donnera l'énergie
        d'un mouton au départ.
        max_energie: le maximum d'énergie qu'un mouton peut avoir.
        lose_energie: l'énergie que perd un mouton à chaque itération.

    Attributs :
        energie : energie d'un mouton au départ.
        pos: tuple contenant la position d'un moutonau départ
        monde: valeur contenant le pourcentage de moutons dans le monde (définie dans la classe monde).

    Methodes :
        action(): crée toutes les actions des moutons (nourriture, reproduction, déplacement...)
    """

    # Création des attributs communs à toutes les instances
    nom = "Mouton"
    reproduction_energie = 160
    start_energie = (80,130)
    max_energie = 200
    lose_energie = (10,30)

############################ CREATION DE LA FONCTION D'INITIALISATION DE LA CLASSE MOUTON AVEC SES ATTRIBUTS ############################

    # Initialisation des attributs
    def __init__(self,position,monde,energie = None):
        self.energie = energie
        if self.energie == None:self.energie = randint(self.start_energie[0],self.start_energie[1])
        self.pos = position
        self.monde = monde

#######################################################################################################################################

############################################ DEFINITION DE LA METHODE DE LA CLASSE MOUTON #############################################

    #Méthode gérant les actions des moutons, appellée dans monde.py
    def action(self):
        """
        Méthode permettant au mouton de manger de l'herbe, bouger et essayer de se reproduire
        Il gagne herbe.quantite d'énergie quand il mange et se reproduit quand il a en a assez.
        """
        herbe = self.monde.get_herbe_at(self.pos)
        self.energie += herbe.quantite
        herbe.dead()

        #Si self.energie est supérieure à max_energie, alors self.energie prend la valeur de max_energie.
        if self.energie > self.max_energie:self.energie = self.max_energie

        self.energie-=randint(self.lose_energie[0],self.lose_energie[1])

        # Condition qui appelle la fonction de mort
        if self.energie <= 0:self.dead()

        var = self.getAround_Herbe()
        self.pos[0] = var[0]
        self.pos[1] = var[1]

        self.pos[0] %= self.monde.dimentions[0]
        self.pos[1] %= self.monde.dimentions[1]

        # Condition pour la reproduction, si self.energie est supérieure à reproduction_energie
        if self.energie > self.reproduction_energie:
            self.energie //= 2
            self.monde.carte_entitee_buf.append(Mouton([(self.pos[0]+randint(-1,1))%self.monde.dimentions[0],(self.pos[1]+randint(-1,1))%self.monde.dimentions[1]],self.monde,self.energie))

#######################################################################################################################################

#######################################################################################################################################




