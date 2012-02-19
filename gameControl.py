import food
import orginism

class gameControl():
    def __init__(self, screen):
        #Create controllers for the food and critters
        self.orgs    = orginism.OrgControl(screen)
        self.food    = food.FoodControl(screen)

    def draw(self):                
        #Update and draw the critters
        self.orgs.update(self.food.foods)
        self.food.update()

        #Draw screen
        self.orgs.draw()
        self.food.draw()

        #Debug!
        """
        self.food.debug()
        self.control.debug()
        """
