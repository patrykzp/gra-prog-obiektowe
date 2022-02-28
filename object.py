import pygame
import math

class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,size,game):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.size = size
        self.rotation = 0
        self.__oldrot = 0
        self.game = game
        self.setImage(pygame.image.load("Player.png"))
        game.Objects.add(self)
    def getLookAngle(self,pos_x,pos_y):
        rel_x, rel_y = pos_x-self.rect.centerx, pos_y-self.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        return int(angle)
    def setImage(self,image):
        self.__ogimg = image
        self.__ogimg = pygame.transform.scale(self.__ogimg, self.size)
        self.image = self.__ogimg
        self.rect = self.image.get_rect()
    def update(self): # updateowanie pozycji modelu zeby byla taka sama jak pozycja obiektu
        self.rect.center = (self.pos_x-self.game.camera[0],self.pos_y-self.game.camera[1])
        self.rotation=self.rotation%360
        if self.__oldrot-self.rotation!=0:
            self.image = pygame.transform.rotate(self.__ogimg, self.rotation)
            x, y = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)
        self.__oldrot = self.rotation