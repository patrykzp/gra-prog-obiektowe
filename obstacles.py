import pygame
from object import Object

class Obstacle(Object):
   def __init__(self,pos_x, pos_y,size,game):
       super().__init__(pos_x, pos_y, size,game)
       self.hasCollision = True
       self.setImage(pygame.image.load("Rock_Pile.png"))

class InteractiveObstacle(Obstacle):
    def __init__(self,pos_x,pos_y,size,game,HP):
        super().__init__(pos_x,pos_y,size,game)
        self.HP = HP
        self.setImage(pygame.image.load("IronOre.png"))

    def takeDamage(self,damage):
        self.game.player.iron+=1
        self.HP -= damage
        if (self.HP <= 0):
            self.kill()

class InteractiveObstacle2(Obstacle):
    def __init__(self,pos_x,pos_y,size,game,HP):
        super().__init__(pos_x,pos_y,size,game)
        self.HP = HP
        self.setImage(pygame.image.load("tree.png"))

    def takeDamage(self, damage):
        self.game.player.wood += 1
        self.HP -= damage
        if (self.HP <= 0):
            self.kill()

class InteractiveObstacle3(Obstacle):
    def __init__(self,pos_x,pos_y,size,game,HP):
        super().__init__(pos_x,pos_y,size,game)
        self.HP = HP
        self.setImage(pygame.image.load("THEROCK.png"))

    def takeDamage(self, damage):
        self.game.player.stone += 1
        self.HP -= damage
        if (self.HP <= 0):
            self.kill()