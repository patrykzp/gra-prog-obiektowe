import pygame
import random
import player

class NPC(player.Character):
   def __init__(self,pos_x, pos_y, facing, HP, size):
       super().__init__(pos_x, pos_y, facing, HP, size)
       pos_x = random.randint(50, 650)
       pos_y = random.randint(50, 450)

   def state(self):
       pass

   def move(self):
       pass

   def rest(self):
       pass

   def run(self):
       pass