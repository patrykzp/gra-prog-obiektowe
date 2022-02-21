import pygame
import random
import player

class NPC(player.Character):
   def __init__(self,pos_x, pos_y, facing, HP, size,game):
       super().__init__(pos_x, pos_y, facing, HP, size,game)
       self.setImage(pygame.image.load("krowa.png"))
       self.timer = 0
       self.direction = (0,0)
   def state(self):
       pass

   def update(self):
       if self.timer >= 120:
           self.direction = (random.randint(-1, 1),random.randint(-1, 1))
           self.rotation = self.getLookAngle(self.rect.centerx+self.direction[0],self.rect.centery+self.direction[1])+180
           self.timer = 0
       self.pos_x += self.direction[0]*1
       self.pos_y += self.direction[1]*1
       super().update()
       self.timer += 1


   def rest(self):
       pass

   def run(self):
       pass
