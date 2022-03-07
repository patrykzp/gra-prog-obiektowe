import pygame.font
import os

from object import Renderable

class UIObject(Renderable):
    def __init__(self,pos_x,pos_y,size,game):
        super().__init__(pos_x,pos_y,size,game)
        game.UI.add(self)

class Text(UIObject):
    def __init__(self,pos_x,pos_y,game,text,textColor = None, font=None):
        super().__init__(pos_x,pos_y,(100,100),game)
        self.font = font or pygame.font.Font(os.path.abspath("8BITWONDER.TTF"),30)
        self.textColor = textColor or pygame.Color("black")
        self.changeText(text)
    def changeText(self,text):
        self.text = text
        self.image = self.font.render(self.text,1,self.textColor)
        self.rect = self.image.get_rect()
    def update(self):
        super().update()

class Button(UIObject):

    def __init__(self, pos_x, pos_y, size, game):
        super().__init__(pos_x, pos_y, size, game)

    def onClick(self):
        sf = pygame.surface.Surface(self.size)
        sf.fill((255, 255,0))
        self.setImage(sf)

    def update(self):
        if self.game.input.mouseDown:
            x, y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x, y):
                self.onClick()
        super().update()

