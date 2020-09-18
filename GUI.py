import pygame

class PygameGui():

    def __init__(self,monde):
        self.windows = None
        self.monde = monde
    
    def draw(self):
        pass

    def start(self): # start the main loop
        self.__mainLoop()

    def __mainLoop(self): # the main loop
        while True:
            pass

    def click(self,pos): # What to do on a click
        pass

    def key_press(self,key): # what to do on a key press
        pass