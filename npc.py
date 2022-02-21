import threading

import pygame
import random
import player

class NPC(player.Character):
   def __init__(self,pos_x, pos_y, facing, HP, size):
       super().__init__(pos_x, pos_y, facing, HP, size)
       self.setImage(pygame.image.load("krowa.png"))
   def state(self):
       pass

   def update(self):
       super().update()
       self.pos_x += random.randint(-1, 2)/100
       self.pos_y += random.randint(-1, 2)/100
       print("a")


   def rest(self):
       pass

   def run(self):
       pass
