import math

import pygame

import npc
from object import Object

class Character(Object):
    def __init__(self, pos_x, pos_y, HP, size,game):
        super().__init__(pos_x,pos_y,size,game)
        self.hasCollision = True
        self._pushForce = 0.5
        self.HP = HP
        self.speed = 3.5
        self.size = size
    def takeDamage(self, damage):
        self.HP -= damage
        if (self.HP <= 0):
            self.kill()
    def _collideMethod(self,collider):
        collidedWith = self.checkCollide(collider)
        if collidedWith:
            x2, y2 = collidedWith.rect.centerx - self.rect.centerx, collidedWith.rect.centery - self.rect.centery
            distance = math.sqrt(x2 * x2 + y2 * y2)
            if distance > 0:
                x2, y2 = x2 / distance, y2 / distance
            self.pos_x -= x2 * collidedWith._pushForce * self.speed
            self.pos_y -= y2 * collidedWith._pushForce * self.speed
        return collidedWith
class Player(Character):
    def __init__(self,pos_x, pos_y, size, game):
        super().__init__(pos_x, pos_y,100, size, game)
        self.cooldown = 0

        self.__extrarot = 0
    def mouseClick(self):
        x, y = pygame.mouse.get_pos()

        collider = pygame.rect.Rect(self.rect.centerx, self.rect.centery, 50,50)
        dx, dy = x - self.rect.centerx, y - self.rect.centery
        dist = math.hypot(dx, dy)

        dx, dy = dx / dist, dy / dist  # Normalize

        print(dx,dy)
        collider.center = (self.rect.centerx+dx*60,self.rect.centery+dy*60)
        pygame.draw.rect(self.game.screen, (155, 0, 0), collider, 5)
        obj = self._collideMethod(collider)
        if (isinstance(obj,npc.NPC)):
            obj.takeDamage(25)


    def update(self):
        self.cooldown -= 1
        self.__extrarot = max(self.__extrarot-2, 0)
        if self.cooldown <= 0 and self.game.input.mouseDown:
            self.__extrarot = 25
            self.mouseClick()
            self.cooldown = 20
        x, y = pygame.mouse.get_pos()
        self.rotation = self.getLookAngle(x, y) + 90 + self.__extrarot

        x, y = self.game.input.MoveDirection[0]*self.speed, self.game.input.MoveDirection[1]*self.speed

        self.pos_x += x
        self.pos_y += y

        collider = pygame.rect.Rect(self.rect.centerx, self.rect.centery, self.size[0]/1.5 + abs(x),
                                    self.size[1]/1.5 + abs(y))
        collider.center = (self.rect.centerx + self.game.input.MoveDirection[0]*4,
                           self.rect.centery + self.game.input.MoveDirection[1]*4)
        # pygame.draw.rect(self.game.screen,(155,0,0),collider,5)
        self._collideMethod(collider)

        super().update()