import pygame
from object import Object

class Obstacle(Object):
   def __init__(self,pos_x, pos_y,size,game):
       super().__init__(pos_x, pos_y, size,game)
       self.hasCollision = True
       self.setImage(pygame.image.load("Rock_Pile.png"))
