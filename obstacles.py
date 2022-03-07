import pygame
from object import Object

class Obstacle(Object):
   def __init__(self,pos_x, pos_y,size,game):
       super().__init__(pos_x, pos_y, size,game)
       self.hasCollision = True
       self.setImage(pygame.image.load("Rock_Pile.png"))

class IronOre(Obstacle):
    def __init__(self,pos_x,pos_y,size,game,HP):
        super().__init__(pos_x,pos_y,size,game)
        self.HP = HP
        self.setImage(pygame.image.load("IronOre.png"))

    def takeDamage(self,damage):
        self.game.player.iron+=1
        self.HP -= damage
        if (self.HP <= 0):
            self.kill()

class Tree(Obstacle):
    def __init__(self,pos_x,pos_y,size,game,HP):
        super().__init__(pos_x,pos_y,size,game)
        self.HP = HP
        self.setImage(pygame.image.load("tree.png"))

    def takeDamage(self, damage):
        self.game.player.wood += 2
        self.HP -= damage
        if (self.HP <= 0):
            self.kill()

class MineableRock(Obstacle):
    def __init__(self,pos_x,pos_y,size,game,HP):
        super().__init__(pos_x,pos_y,size,game)
        self.HP = HP
        self.images = [pygame.image.load("Rock_Pile.png"),pygame.image.load("Rock_Pile2.png")]

        self.setImage(self.images[0])
    def takeDamage(self, damage):
        self.game.player.stone += 2
        self.HP -= damage

        if (self.HP <= 50):
            self.setImage(self.images[1])
        if (self.HP <= 0):
            self.kill()

class AppleTree(Obstacle):
    def __init__(self,pos_x,pos_y,size,game,HP):
        super().__init__(pos_x,pos_y,size,game)
        self.HP = HP
        self.setImage(pygame.image.load("apple_tree.png"))

    def takeDamage(self, damage):
        self.game.player.food = min(self.game.player.food+50,100)
        self.game.player.wood += 1
        self.HP -= damage
        if (self.HP <= 0):
            self.kill()