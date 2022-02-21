import pygame
import main

class Character(main.Object):
    def __init__(self, pos_x, pos_y, facing, HP, size):
        super().__init__(pos_x,pos_y,size)
        self.facing = facing
        self.HP = HP
        self.size = size

class Player(Character):
    def __init__(self,pos_x, pos_y, facing, HP, size):
        super().__init__(pos_x, pos_y, facing, HP, size)