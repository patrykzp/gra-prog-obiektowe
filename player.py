import math
from dataclasses import dataclass
import UI
import pygame

import mainmenu
from object import Object


@dataclass
class UiSet:
    foodBar : UI.Bar
    healthBar : UI.Bar
    foodText : UI.Text
    hpText : UI.Text
    ironText : UI.Text
    woodText : UI.Text
    stoneText : UI.Text
    def update(self,player):
        self.ironText.changeText("zelazo: {:d}".format(player.iron))
        self.woodText.changeText("drewno: {:d}".format(player.wood))
        self.stoneText.changeText("kamien: {:d}".format(player.stone))
        self.foodBar.progress = player.food/100
        self.healthBar.progress = player.HP / 100

class Character(Object):
    def __init__(self, pos_x, pos_y, HP, size,game):
        super().__init__(pos_x,pos_y,size,game)
        self.hasCollision = True
        self._pushForce = 0.5
        self.HP = HP
        self.speed = 5.5
        self.size = size

    def death(self):
        self.kill()
    def takeDamage(self, damage):
        self.HP -= damage
        if (self.HP <= 0):
            self.death()
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
    def __init__(self,pos_x, pos_y, size, game,uiset : UiSet):
        super().__init__(pos_x, pos_y,100, size, game)
        self.cooldown = 0
        self._uiset = uiset

        self.wood = 0
        self.stone = 0
        self.iron = 0

        self.food = 100
        self.__extrarot = 0
        self.setImage(pygame.image.load("Player.png"))

    def mouseClick(self):
        x, y = pygame.mouse.get_pos()

        collider = pygame.rect.Rect(self.rect.centerx, self.rect.centery, 50,50)
        dx, dy = self.getFacingToVector(x,y)

        collider.center = (self.rect.centerx+dx*70,self.rect.centery+dy*70)
        pygame.draw.rect(self.game.screen, (155, 0, 0), collider, 5)
        obj = self._collideMethod(collider)
        if (hasattr(obj,"takeDamage")):
            obj.takeDamage(25)
            dx, dy = obj.getFacingToVector(self.rect.centerx, self.rect.centery)
            obj._offset = (-dx * 10, -dy * 10)


    def update(self):
        # rotacja i klikanie
        self.cooldown -= 1
        self.food = max(self.food-0.02,0)
        if self.food <= 0:
            self.HP -= 0.01
        if self.HP <= 0:
            mainmenu.DeathScreen(self.game)
            return
        self._uiset.update(self)

        self.__extrarot = max(self.__extrarot-2, 0)
        if self.cooldown <= 0 and self.game.input.mouseDown:
            self.__extrarot = 25
            self.mouseClick()
            self.cooldown = 20
        x, y = pygame.mouse.get_pos()
        self.rotation = self.getLookAngle(x, y) + 90 + self.__extrarot

        # movement

        x, y = self.game.input.MoveDirection[0]*self.speed, self.game.input.MoveDirection[1]*self.speed

        bounds = self.game.worldBounds

        self.pos_x += x
        self.pos_y += y

        # zeby gracz nie wychodzil poza mape
        if bounds['x'][0] > self.pos_x:
            self.pos_x += 1*self.speed
        if bounds['x'][1] < self.pos_x-1200:
            self.pos_x -= 1*self.speed
        if bounds['y'][0] > self.pos_y:
            self.pos_y += 1*self.speed
        if bounds['y'][1] < self.pos_y-750:
            self.pos_y -= 1*self.speed

        # kolizje

        collider = pygame.rect.Rect(self.rect.centerx, self.rect.centery, self.size[0]/1.5 + abs(x),
                                    self.size[1]/1.5 + abs(y))
        collider.center = (self.rect.centerx + self.game.input.MoveDirection[0]*4,
                           self.rect.centery + self.game.input.MoveDirection[1]*4)
        pygame.draw.rect(self.game.screen,(155,0,0),collider,5)
        self._collideMethod(collider)
        super().update()