################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################

import pygame
from core.creatures.mouton import Mouton
from core.creatures.loup import Loup

#######################################################################################################################################

############################################### CREATION DE LA CLASSE PYGAMEGUI #######################################################

#Création de la classe PygameGui
class PygameGui():
    """
    La classe PygameGui est la classe qui s'occupe de la gestion de l'interface graphique.

    Instance de classe:
        speed: vitesse à laquelle des itérations sont réalisées.

    Attributs :
        screen: l'affichage de la fenêtre
        monde: la création du monde.
        running: lancement actif de pygame
        size: taille de la fenêtre

    Methodes :
        draw(): méthode dessinant le conteu de la fenêtre pygame.
        start(): méthode lancant la boucle principale.
        _mainLoop(): méthode de la boucle principale
        left_click(): réaction lorsque clic gauche
        right_click(): réaction lorsque clic droit
    """

    # Création de l'instance de classe de PygameGui
    speed = 0

################################# CREATION DE LA FONCTION D'INITIALISATION DE LA CLASSE PYGAMEGUI AVEC SES ATTRIBUTS ##################################

    #Initialisation de la classe PygameGui et de ses attributs
    def __init__(self,monde,size=(300,300)):
        self.screen = None
        self.monde = monde
        self.running = False
        self.size = size
        pygame.init()
        self.dt = 0

#######################################################################################################################################################

################################################## DEFINITION DES METHODES DE LA CLASSE PYGAMEGUI #####################################################

    #Méthode dessinant le contenu de la fenêtre
    def draw(self):
        square_tile_sizeX = self.size[0]/self.monde.dimentions[0]
        square_tile_sizeY = self.size[1]/self.monde.dimentions[1]

        # Dessin de l'environnement
        for x,ligne in enumerate(self.monde.carte):
            for y,element in enumerate(ligne):
                pygame.draw.rect(self.screen,element.getColor(),(square_tile_sizeX*x, square_tile_sizeY*y, square_tile_sizeX, square_tile_sizeY))

        #Dessin des créatures
        for creature in self.monde.carte_entitee:

            # Ajout de 0.5 pour obtenir le centre de la case
            pixel_pos_X = int(creature.pos[0]*square_tile_sizeX+square_tile_sizeX/2)

            # Ajout de 0.5 pour obtenir le centre de la case
            pixel_pos_Y = int(creature.pos[1]*square_tile_sizeY+square_tile_sizeY/2)
            pygame.draw.circle(self.screen, creature.getColor()[0], (pixel_pos_X,pixel_pos_Y), int(min(square_tile_sizeX,square_tile_sizeY)*creature.getColor()[1]))
        pygame.display.flip()

    # Méthode du lancement de la boucle principale
    def start(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Simulation d'un écosystème")
        self.__mainLoop()

    # Méthode de la boucle principale
    def __mainLoop(self):
        self.running = True
        clock = pygame.time.Clock()
        exec_= 0

        #Tant que la boucle principale est en cours d'excution
        while self.running:
            self.dt = clock.tick()/1000 # Calculation du delaTime utile pour les transitions
            exec_ += self.dt

            if exec_ > self.speed: # Execution automatique d'une ietration tout les self.speed secondes
                self.monde.iteration()
                exec_ = 0

                self.draw()

            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():

                 # Création de l'évènement quitter
                if event.type == pygame.QUIT:self.quit();break
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # Si clic gauche, on execute la raction liée à clic gauche
                    if event.button == 1:self.left_click(pos)

                    # Si clic droit, on execute la raction liée à clic droit
                    if event.button == 3:self.right_click(pos) #


            # Réaction après l'event de garder les touches Q (A sur Qwerty)ou D appuyées
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:self.left_click(pos)
            if keys[pygame.K_d]:self.right_click(pos)



    # Réaction après l'event de clic droit
    def left_click(self,pos):
        self.monde.carte_entitee.append(Mouton([(pos[0]*self.monde.dimentions[0])//self.size[0],(pos[1]*self.monde.dimentions[1])//self.size[1]],self.monde))

    # Réaction après l'event de clic droit
    def right_click(self,pos):
        self.monde.carte_entitee.append(Loup([(pos[0]*self.monde.dimentions[0])//self.size[0],(pos[1]*self.monde.dimentions[1])//self.size[1]],self.monde))

    # Fermeture de la fenêtre
    def quit(self):
        pygame.quit()
        self.running = False
        exit()

#######################################################################################################################################################

#######################################################################################################################################################