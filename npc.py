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
       self.run = False


   def update(self):

       if self.timer >= 120:
           if self.run:
               dx, dy = self.getFacingToVector(self.game.player.rect.centerx, self.game.player.rect.centery)
               self.direction = (-dx*4, -dy*4)
               self.run = False
           else:
               if random.randint(0, 1) == 1:
                   self.direction = (random.randint(-1, 1),random.randint(-1, 1))
               else:
                   self.direction = (0,0)
           self.timer = 0
       if self.direction != (0,0):
            self.rotation = self.getLookAngle(self.rect.centerx + self.direction[0],
                                         self.rect.centery + self.direction[1]) + 90
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

   def takeDamage(self, damage):
        super().takeDamage(damage)
        self.run = True
        self.timer = 2000

   def death(self):
       self.game.player.food = min(self.game.player.food+50,100)
       super().death()

class aggroNPC(NPC):

    def __init__(self,pos_x,pos_y,HP,size,game):
        super().__init__(pos_x,pos_y,HP,size,game)
        self.setImage(pygame.image.load("THEROCK.png"))

    def update(self):
        plr = self.game.player
        vec = pygame.math.Vector2
        dist = (vec(self.pos_x,self.pos_y)-vec(plr.pos_x,plr.pos_y)).length()
        super(player.Character,self).update()
        if (dist<= 50):
            self.game.player.HP -= 0.5
        elif (dist <= 500):
            dx, dy = self.getFacingToVector(self.game.player.rect.centerx, self.game.player.rect.centery)
            self.direction = (dx * 3, dy * 3)
        else:
            self.direction = (0,0)
            return
        if self.direction != (0, 0):
            self.rotation = self.getLookAngle(self.rect.centerx + self.direction[0],
                                              self.rect.centery + self.direction[1]) + 90
        self.pos_x += self.direction[0] * 1
        self.pos_y += self.direction[1] * 1

    def death(self):
        self.game.player.HP = min(self.game.player.HP+15,100)
        super().death()