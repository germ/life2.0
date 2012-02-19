import math
import random
import pygame

ORG_START       = 25
ORG_MIN         = 15
ORG_RAD_MIN     = 1
ORG_FOOD_INCR   = 20
ORG_SPEED       = 3
ORG_BIRTH       = 20
ORG_DISPLACE    = 10
ORG_WIDTH       = 2

class OrgControl():
    def __init__(self, screen):
        #Set class vars, and populate the playfield
        self.orgs       = []
        self.screen     = screen

        for i in range(0, ORG_START):
            self.orgs.append(Orginism(screen))

    def draw(self):
        #Draw every critter
        for i in self.orgs:
            i.draw()

    def update(self, food):
        #Move, birth, bring out the dead, eat
        if len(self.orgs) > 0:
            new = []

            for i in self.orgs:
                #Move/eat
                i.update(food)
                if i.alive:
                    #Birth
                    if i.food > ORG_BIRTH:
                        j = Orginism(self.screen)
                        j.food = i.food/2
                        i.food = j.food

                        new.append(i)
                        new.append(j)
                    else:
                        new.append(i)
             
            #Remove the dead
            self.orgs = new

        #Spawn new critters if population drops below min
        if len(self.orgs) < ORG_MIN:
            for i in range(0, ORG_MIN - len(self.orgs)):
                self.orgs.append(Orginism(self.screen))

    def debug(self):
        for i in self.orgs:
            i.debug()

class Orginism():
    def __init__(self, screen):
        #Set class vars
        self.ss         = screen.get_size()
        self.screen     = screen
        self.color      = pygame.color.Color(255, 0, 0)
        self.x          = random.randint(0, self.ss[0])
        self.y          = random.randint(0, self.ss[1])
        self.food       = random.randint(0, 20)
        self.lastFeed   = 0
        self.alive      = True

    def draw(self):
        rad     = ORG_RAD_MIN + self.food*0.5
        if rad < ORG_WIDTH:
            pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)) , int(rad), int(rad))
        else:
            pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)) , int(rad), ORG_WIDTH)

    def update(self, food):
        #Navigation code
        nearFood    = self.nearestFood(food)

        if nearFood != None:
            near        = [nearFood.x, nearFood.y]
        else:
            #Catch code for no food, will be spawned on next draw
            near        = [random.randint(0, self.ss[0]), random.randint(0, self.ss[1])]

        x           = near[0] - self.x
        y           = near[1] - self.y
        r           = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        ang         = math.atan2(y, x)
        yMov        = math.sin(ang)*ORG_SPEED
        xMov        = math.cos(ang)*ORG_SPEED

        #Code to move directly to food if in range
        if (r < ORG_SPEED):
            self.x = near[0]
            self.y = near[1]
        else:
            self.x += xMov
            self.y += yMov

        #Check for exhaustion/eat food
        #On the food and hungry (Below 1/4 full val)
        if nearFood != None:
            if self.x == near[0] and self.y == near[1] and self.lastFeed < ORG_FOOD_INCR/4:
                self.food += nearFood.take()

        #Death code
        if self.lastFeed <= 0 and self.food == 0:
            self.alive = False

        #Eat food from stores
        if self.lastFeed <= 0:
            self.food       -= 1
            self.lastFeed   += ORG_FOOD_INCR

        self.lastFeed -= 1

    def nearestFood(self, food):
        #Find the nearest food source
        dis = []
        for i in food:
            r = abs(math.sqrt(math.pow(i.x - self.x, 2) + math.pow(i.y - self.y, 2)))
            dis.append([r, i])

        dis = sorted(dis, key=lambda i: i[0])

        if len(dis) > 0:
            return dis[0][1]
        else:
            return None

    def debug(self):
        print "DEBUG"
        print "X: %d, Y: %d, lastFeed: %d, alive: %d, food: %d" % (self.x, self.y, self.lastFeed, self.alive, self.food)
