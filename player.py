import math

import pygame
from object import Object

class Character(Object):
    def __init__(self, pos_x, pos_y, facing, HP, size,game):
        super().__init__(pos_x,pos_y,size,game)
        self.facing = facing
        self.hasCollision = True
        self._pushForce = 0.5
        self.HP = HP
        self.speed = 2.5
        self.size = size
    def _collideMethod(self,collider):
        collidedWith = self.checkCollide(collider)
        if collidedWith:
            x2, y2 = collidedWith.rect.centerx - self.rect.centerx, collidedWith.rect.centery - self.rect.centery
            distance = math.sqrt(x2 * x2 + y2 * y2)
            if distance > 0:
                x2, y2 = x2 / distance, y2 / distance
            self.pos_x -= x2 * collidedWith._pushForce * self.speed
            self.pos_y -= y2 * collidedWith._pushForce * self.speed
class Player(Character):
    def __init__(self,pos_x, pos_y, facing, HP, size, game):
        super().__init__(pos_x, pos_y, facing, HP, size, game)
    def update(self):
        x, y = pygame.mouse.get_pos()
        self.rotation = self.getLookAngle(x, y) + 90

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