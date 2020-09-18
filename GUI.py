import pygame


class PygameGui():

    def __init__(self,monde,sizeX=120,sizeY=100):
        self.screen = None
        self.monde = monde
        self.running = False
        self.size = (sizeX,sizeY)
        pygame.init()

    def draw(self):
        pass

    def start(self): # start the main loop
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Simulation')
        self.__mainLoop()

    def __mainLoop(self): # the main loop
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:self.quit()
                


    def click(self,pos): # What to do on a click
        pass

    def key_press(self,key): # what to do on a key press
        pass

    def quit(self): # Closing the window
        pygame.quit()
        self.running = False
