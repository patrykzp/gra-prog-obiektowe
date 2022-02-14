import pygame

from main import Game

class Object:
    def __init__(self,x,y):
        self.pos_x = x
        self.pos_y = y
        self.rect = pygame.Rect(x,y)
        Game.Objects.append(self)
    def render(self):
        pass