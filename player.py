import pygame
from object import Object

class Character(Object):
    def __init__(self, pos_x, pos_y, facing, HP, size,game):
        super().__init__(pos_x,pos_y,size,game)
        self.facing = facing
        self.HP = HP
        self.size = size

class Player(Character):
    def __init__(self,pos_x, pos_y, facing, HP, size, game):
        super().__init__(pos_x, pos_y, facing, HP, size, game)
        self.speed = 5

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.rotation = self.getLookAngle(x, y) + 90
        self.pos_x += self.game.input.MoveDirection[0]*self.speed
        self.pos_y += self.game.input.MoveDirection[1]*self.speed
        super().update()