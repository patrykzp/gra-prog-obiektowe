import pygame
import random
import player

class NPC(player.Character):
   def __init__(self,pos_x, pos_y, facing, HP, size):
       super().__init__(pos_x, pos_y, facing, HP, size)
   def move(self):
       pass

   def rest(self):
       pass

   def run(self):
       pass
