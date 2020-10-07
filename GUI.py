# importation des modules necessaires
import pygame
from core.creatures.mouton import Mouton
from core.creatures.loup import Loup

class PygameGui(): #creation de la class PygameGui

    speed = 0

    def __init__(self,monde,size=(300,300)): #creation des attributs de la class PygameGui
        self.screen = None
        self.monde = monde
        self.running = False
        self.size = size
        pygame.init()
        self.dt = 0

    def draw(self): #fonction de dessin graphisme
        square_tile_sizeX = self.size[0]/self.monde.dimentions[0]
        square_tile_sizeY = self.size[1]/self.monde.dimentions[1]
        # dessiner l'environnement
        for x,ligne in enumerate(self.monde.carte):
            for y,element in enumerate(ligne):
                pygame.draw.rect(self.screen,element.getColor(),(square_tile_sizeX*x, square_tile_sizeY*y, square_tile_sizeX, square_tile_sizeY))

        # dessiner les creatures
        for creature in self.monde.carte_entitee:
            pixel_pos_X = int(creature.pos[0]*square_tile_sizeX+square_tile_sizeX/2) # ajout de 0.5 pour obtenir le centre de la case
            pixel_pos_Y = int(creature.pos[1]*square_tile_sizeY+square_tile_sizeY/2) # ajout de 0.5 pour obtenir le centre de la case
            pygame.draw.circle(self.screen, creature.getColor()[0], (pixel_pos_X,pixel_pos_Y), int(min(square_tile_sizeX,square_tile_sizeY)*creature.getColor()[1]))
        pygame.display.flip()

    def start(self): # # lancement de la boucle principale
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Simulation')
        self.__mainLoop()

    def __mainLoop(self): # definition de la boucle principale
        self.running = True
        clock = pygame.time.Clock()
        exec_= 0

        while self.running: #tant que la boucle principale est en cours d'excution
            self.dt = clock.tick()/1000 # Calculation du delaTime utile pour les transitions
            exec_ += self.dt

            if exec_ > self.speed: # Execution automatique d'une ietration tout les self.speed secondes
                self.monde.iteration()
                exec_ = 0

                self.draw()

            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:self.quit();break # creation de l'evenement quitter
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:self.left_click(pos) # si l'evenement est egal au click gauche
                    if event.button == 3:self.right_click(pos) # si l'evenement est egal au click  droit


            keys = pygame.key.get_pressed()
            if keys[pygame.K_l]:self.left_click(pos)
            if keys[pygame.K_r]:self.right_click(pos)


    def left_click(self,pos): # Que faire sur l'event de click gauche
        self.monde.carte_entitee.append(Mouton([(pos[0]*self.monde.dimentions[0])//self.size[0],(pos[1]*self.monde.dimentions[1])//self.size[1]],self.monde))

    def right_click(self,pos): # Que faire sur l'event de click doit
        self.monde.carte_entitee.append(Loup([(pos[0]*self.monde.dimentions[0])//self.size[0],(pos[1]*self.monde.dimentions[1])//self.size[1]],self.monde))

    def quit(self): # fermeture de la fenetre
        pygame.quit()
        self.running = False
        exit()
