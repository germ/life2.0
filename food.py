import math
import random
import pygame

FOOD_START      = 20
FOOD_MIN        = 10
FOOD_RAD_MIN    = 5
FOOD_MIN_SUPPLY = 20
FOOD_WIDTH      = 3

class Food():
    def __init__(self, screen):
        #init class vars
        self.screen = screen
        self.ss     = screen.get_size()

        self.x      = random.randint(0, self.ss[0])
        self.y      = random.randint(0, self.ss[1])
        self.store  = random.randint(FOOD_MIN_SUPPLY, FOOD_MIN_SUPPLY*2)

    def draw(self):
        rad     = FOOD_RAD_MIN + self.store*0.2
        color   = pygame.color.Color(0, 255, 0)

        pygame.draw.circle(self.screen, color, (self.x, self.y) , int(rad), FOOD_WIDTH)
    
    def take(self):
        #Food removal code
        if self.store >= 1:
            self.store -= 1
            return 1
        else:
            return 0

    def debug(self):
        print "DEBUG"
        print "X: %d, Y: %d, Store: %d" % (self.x, self.y, self.store)

class FoodControl():
    def __init__(self, screen):
        self.foods      = []
        self.screen     = screen
        for i in range(0, FOOD_START):
            self.foods.append(Food(screen))
    
    def draw(self):
        for i in self.foods: 
            i.draw()

    def update(self):
        #Remove exhausted food stores
        if len(self.foods) > 0:
            new = []
            for i in self.foods:
                if i.store >= 1:
                    new.append(i)

            self.foods = new

        #Spawn new ones if necessary
        if len(self.foods) < FOOD_MIN:
            for i in range(0, FOOD_MIN - len(self.foods)):
                self.foods.append(Food(self.screen))

    def debug(self):
        for i in self.foods:
            i.debug()
