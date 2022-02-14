import pygame
import random

class NPC(Character):
   def __init__(self,pos_x, pos_y, facing, HP, size):
       super().__init__(pos_x, pos_y, facing, HP, size)
       pygame.sprite.Sprite.__init__(self)
       self.rect = pygame.Rect(self.pos_x, self.pos_y, self.size, self.facing)

   def move(self):
       pass

   def rest(self):
       pass

   def run(self):
       pass
