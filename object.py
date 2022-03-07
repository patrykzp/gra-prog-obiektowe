import pygame
import math

def nm(a):
    return (a > 0 and 1) or (a < 0 and -1) or 0

class Renderable(pygame.sprite.Sprite):
    def __init__(self, x, y, size, game):
        self.pos_x = x
        self.pos_y = y
        self.game = game
        self.rect = None
        self.size = size
        pygame.sprite.Sprite.__init__(self)
        sf = pygame.surface.Surface(size)
        sf.fill((255, 255, 255))
        self.setImage(sf)

    def setImage(self, image):
        self._ogimg = image
        self._ogimg = pygame.transform.scale(self._ogimg, self.size)
        self.image = self._ogimg

        oldrect = self.rect
        self.rect = self.image.get_rect()
        self.rect.center = (oldrect and oldrect.center) or (0,0)
    def update(self):
        self.rect.center = (self.pos_x,self.pos_y)

class Object(Renderable):
    def __init__(self,x,y,size,game):
        super().__init__(x,y,size,game)
        self.hasCollision = False
        self._offset = (0,0)
        self._pushForce = 1
        self.collisionBox = pygame.rect.Rect(0, 0, self.size[0]/1.5,self.size[1]/1.5)
        self.rotation = 0
        self.__oldrot = 0
        game.Objects.add(self)
    def _allowCollisionWith(self, objCollided):
        return self.hasCollision

    def checkCollide(self,collider):
        p = None
        for obj in self.game.Objects:
            if obj is self: continue
            if obj.collisionBox.colliderect(collider) and obj._allowCollisionWith(self):
                p = obj
                break
            p = None
        return p
    def getFacingToVector(self,x,y):
        dx, dy = x - self.rect.centerx, y - self.rect.centery
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        return dx, dy
    def getLookAngle(self,pos_x,pos_y):
        rel_x, rel_y = pos_x-self.rect.centerx, pos_y-self.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        return int(angle)
    def update(self): # updateowanie pozycji modelu zeby byla taka sama jak pozycja obiektu

        self.rect.center = (self.pos_x+self._offset[0]-self.game.camera[0],
                            self.pos_y+self._offset[1]-self.game.camera[1])
        self.rotation=self.rotation%360
        if self.__oldrot-self.rotation!=0:
            self.image = pygame.transform.rotate(self._ogimg, self.rotation)
            x, y = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)
        self.__oldrot = self.rotation
        x,y = self._offset[0]-nm(self._offset[0]),self._offset[1]-nm(self._offset[1])
        self._offset = (x,y)
        self.collisionBox.center = self.rect.center