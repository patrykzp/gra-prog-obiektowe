import pygame
from object import Object

class Obstacle(Object):
   def __init__(self,pos_x, pos_y,size,game):
       super().__init__(pos_x, pos_y, size,game)
       self.hasCollision = True
       self.setImage(pygame.image.load("Rock_Pile.png"))

class InteractiveObstacle(Obstacle):
    def __init__(self,pos_x,pos_y,size,game,HP):
        super().__init__(pos_x,pos_y,size,game)
        self.HP = HP
        self.setImage(pygame.image.load("IronOre.png"))

    def takeDMG(self):
        pass