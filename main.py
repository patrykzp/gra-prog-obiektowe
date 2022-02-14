# tu bedzie gra
import pygame

class Game:
    Objects = []
    @staticmethod
    def newFrame():
        for object in Game.Objects:
            object.render()

