import pygame
import gameControl

from pygame.locals import *
from pygame import Color, Rect, Surface

#Global vars, to be killed with fire
pygame.init()
color_bg            = Color("#0000FF")    
clock               = pygame.time.Clock()   
screen              = pygame.display.set_mode((0,0))

class Game():
    def __init__(self):
        self.gc     = gameControl.gameControl(screen)

    def draw(self):                
        #Draw the play field
        screen.fill( color_bg )
        self.gc.draw()
        pygame.display.flip()

        #increase the clock
        clock.tick(60)
    
    def loop(self):
        while 1:
            #Check for escape
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    exit()

            #Loop the game logic
            self.draw()

if __name__ == "__main__":
    g = Game()
    g.loop()
