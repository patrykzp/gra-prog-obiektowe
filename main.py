# tu bedzie gra
import pygame
import npc
import player
import random

class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,size,game):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.size = size
        self.game = game
        self.setImage(pygame.image.load("Player.png"))
        game.Objects.add(self)
    def setImage(self,image):
        self.image = image
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
    def update(self): # updateowanie pozycji modelu zeby byla taka sama jak pozycja obiektu
        self.rect.center = (self.pos_x-self.game.camera[0],self.pos_y-self.game.camera[1])
class Game:
    input = None
    Objects = pygame.sprite.Group()
    camera=(0,0)
    screen = None
    @staticmethod
    def newFrame():
        Input.playerInput()
        for object in Game.Objects:
            object.update()
        Game.Objects.draw(Game.screen)

class Input:
    MoveDirection = (0,0)
    @staticmethod
    def playerInput():

        x = int(pygame.key.get_pressed()[pygame.K_d])-int(pygame.key.get_pressed()[pygame.K_a])
        y = pygame.key.get_pressed()[pygame.K_s]-pygame.key.get_pressed()[pygame.K_w]
        Input.MoveDirection = (x,y)


if __name__ == "__main__":
    pygame.init()
    size = (1200, 750)
    Game.screen = pygame.display.set_mode(size)
    pygame.display.set_caption("gra")
    gameOn = True
    background = Object(-700,-500,(640*15,1024*15),Game)
    background.setImage(pygame.image.load("trawa.png"))
    for i in range(10):
        npc.NPC(random.randint(-1000,1000),random.randint(-1000,1000),5,5,(100,50),Game)
    plr = player.Player(25,25,5,5,(50,50),Game)
    clock = pygame.time.Clock()
    Game.input = Input
    while gameOn:
        Game.camera = (plr.pos_x-size[0]/2, plr.pos_y-size[1]/2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Wyjscie z gry
                gameOn = False
        Game.screen.fill((75,190,70))
        Game.newFrame()
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()