################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################

from random import randint

#######################################################################################################################################

################################################ CREATION DE LA CLASSE HERBE ##########################################################
class Herbe():
    """
    La classe herbe est la classe qui s'occupe de la gestion de l'herbe.

    Instances de classe:
        nom: nom permettant d'appeler l'herbe dans les autres fichiers.
        max_repousse: valeur maximum de repousse de l'herbe.

    Attributs :
        quantité : valeur aléatoire aléatoire donnant une quantité d'herbe entre 0 et 100.
        monde: valeur contenant le pourcentage d'herbe dans le monde (définie dans la classe monde).

    Methodes :
        getColor() : crée les variations de couleurs pour l'herbe et renvoie un tuple des valeurs des couleurs RGB.
        get_Quantite() : retourne la quantité du bloc d'herbe demandé.
        action() : regénère l'herbe
        dead(): gère la "mort" d'un bloc d'herbe
    """

    # Création des instances de classe d'Herbe
    nom = "Herbe"
    max_repousse = 100

############################ CREATION DE LA FONCTION D'INITIALISATION DE LA CLASSE HERBE AVEC SES ATTRIBUTS ############################

    # Initialisation de la classe Herbe et de ses atttributs
    def __init__(self,monde):
        self.quantite = randint(0,self.max_repousse)
        self.monde = monde

#######################################################################################################################################

############################################# DEFINITION DES METHODES DE LA CLASSE HERBE ###############################################
    # Méthode créant des variations de couleurs pour l'herbe et renvoie des valeurs de chaque couleur primaire
    def getColor(self):
        """
        Retourne la couleur de l'herbe pour PygameGUI.
        """
        # 100% verte : rgb 66, 245, 72
        # 100% morte : rgb 161, 140, 72
        ratio = self.quantite / self.max_repousse
        red = 66*ratio+161*(1-ratio)
        vert = 245*ratio+140*(1-ratio)
        bleu = 72*ratio+72*(1-ratio)
        return (red,vert,bleu)

    #Méthode retournant la quantité du bloc d'herbe demandé.
    def getQuantite(self):
        return self.quantite

    #Méthode régénérant l'herbe, appellée dans monde.py
    def action(self):
        """
        Régéneration d'une quatite d'herbe.
        """
        self.quantite += 1
        if self.quantite > self.max_repousse:self.quantite = self.max_repousse

    #Méthode gérant la "mort" d'un bloc d'herbe
    def dead(self):
        self.quantite = 0

#######################################################################################################################################

#######################################################################################################################################