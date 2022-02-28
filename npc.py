import pygame
import random
import player

class NPC(player.Character):
   def __init__(self,pos_x, pos_y, HP, size,game):
       super().__init__(pos_x, pos_y, HP, size,game)
       self.setImage(pygame.image.load("krowa.png"))
       self.timer = 0
       self.collisionBox = pygame.rect.Rect(0, 0, self.size[0]/2,self.size[1]/2)
       self.direction = (0,0)
   def state(self):
       pass

   def update(self):
       if self.timer >= 120:
           if random.randint(0, 1) == 1:
               self.direction = (random.randint(-1, 1),random.randint(-1, 1))
               self.rotation = self.getLookAngle(self.rect.centerx+self.direction[0],self.rect.centery+self.direction[1])+180
           else:
               self.direction = (0,0)
           self.timer = 0
       self.pos_x += self.direction[0]*1
       self.pos_y += self.direction[1]*1

       collider = pygame.rect.Rect(self.rect.centerx, self.rect.centery, self.size[0] / 1.5 + abs(self.direction[0]),
                                   self.size[0] / 1.5 + abs(self.direction[1]))
       collider.center = (self.rect.centerx + self.direction[0] * 4,
                          self.rect.centery + self.direction[1] * 4)
       # pygame.draw.rect(self.game.screen, (155, 0, 0), collider, 5)
       self._collideMethod(collider)

       super().update()
       self.timer += 1


   def rest(self):
       pass

   def run(self):
       pass
