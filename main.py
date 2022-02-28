# tu bedzie gra
import pygame
import math
import npc
import obstacles
from object import Object
import player
import random

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
        if (abs(x)==1 and abs(y)==1): x,y = x/1.5,y/1.5
        Input.MoveDirection = (x,y)


if __name__ == "__main__":
    pygame.init()
    size = (1200, 750)
    Game.screen = pygame.display.set_mode(size)
    pygame.display.set_caption("gra")
    gameOn = True

    background = Object(-700,-500,(640*15,640*15),Game)
    background.setImage(pygame.image.load("TrawaBg.jpg"))
    for i in range(100):
        npc.NPC(random.randint(-2500,2500),random.randint(-2500,2500),5,5,(150,75),Game)
    for i in range(100):
        obstacles.Obstacle(random.randint(-2500, 2500), random.randint(-2500, 2500), (150, 150), Game)

    plr = player.Player(25,25,5,5,(90,90),Game)
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