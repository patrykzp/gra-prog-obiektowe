import pygame


class Character:
    def __init__(self, pos_x, pos_y, facing, HP, size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.facing = facing
        self.HP = HP
        self.size = size
        pygme.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Player.png")
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.size, self.facing)

class Player(Character):
    def __init__(self,pos_x, pos_y, facing, HP, size):
        super().__init__(pos_x, pos_y, facing, HP, size)
        pygme.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Player.png")
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.size, self.facing)