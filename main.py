# tu bedzie gra
import pygame
import math
import UI
import npc
import obstacles
from object import Object
import player
import random

class Game:
    input = None
    Objects = pygame.sprite.Group()
    UI = pygame.sprite.Group()
    camera=(0,0)
    player = None
    worldBounds = {
        "x": (-3000,3000),
        "y": (-4000,4000)
    }
    screen = None
    @staticmethod
    def newFrame():
        Input.playerInput()
        for object in Game.Objects:
            object.update()
        Game.Objects.draw(Game.screen)
        for uiobject in Game.UI:
            uiobject.update()
        Game.UI.draw(Game.screen)

    @staticmethod
    def getRandomPos():
        theta = random.uniform(0., 2 * math.pi)
        radius = 5000
        d = radius*math.sqrt(random.uniform(0,1))
        x = d * math.cos(theta)
        y = d * math.sin(theta)
        return x,y

    @staticmethod
    def genTerrain():
        for i in range(50):
            posx,posy = Game.getRandomPos()

            npc.NPC(posx, posy, 75, (300, 150), Game)
        for i in range(50):
            posx, posy = Game.getRandomPos()
            obstacles.Obstacle(posx, posy, (150, 150), Game)
        for i in range(50):
            posx, posy = Game.getRandomPos()
            obstacles.InteractiveObstacle\
                (posx, posy, (150, 150), Game,HP=100)
        for i in range(50):
            posx, posy = Game.getRandomPos()
            obstacles.InteractiveObstacle2\
                (posx, posy, (300, 300), Game,HP=100)


class Input:
    MoveDirection = (0,0)
    sprinting = True
    mouseDown = False
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
    pygame.display.set_caption("gra survival")
    gameOn = True

    # ustawianie tła

    background = Object(0,0,(640*15,640*15),Game)
    background.setImage(pygame.image.load("TrawaBg.jpg"))

    # generowanie elementów terenu

    Game.genTerrain()

    # tworzenie gracza i jego elementów UI

    UI.Button(100,500,(100,100),Game)

    def onClick():
        plr.speed += 1

    UI.Button(100, 620, (100, 100), Game).onClick = onClick

    plr = player.Player(0,0,(90,90),Game,player.UiSet(
        foodText=UI.Text(100, 50, Game, "Siema",textColor=pygame.Color("yellow")),
        hpText=UI.Text(100,100,Game,"e",textColor=pygame.Color("red")),
        ironText=UI.Text(100,150,Game,"e",textColor=pygame.Color("black")),
        stoneText=UI.Text(100, 200, Game, "e", textColor=pygame.Color("gray")),
        woodText=UI.Text(100, 250, Game, "e", textColor=pygame.Color("brown")),
    ))

    Game.player = plr
    clock = pygame.time.Clock()
    Game.input = Input

    # petla gry

    while gameOn:
        # ustawianie pozycji kamery i limiotwanie jej

        Game.camera = (
            min(max(plr.pos_x-size[0]/2,Game.worldBounds["x"][0]),Game.worldBounds["x"][1]),
            min(max(plr.pos_y-size[1]/2,Game.worldBounds["y"][0]),Game.worldBounds["y"][1])
        )

        Input.mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                Input.mouseDown = True
            if event.type == pygame.QUIT:  # Wyjscie z gry
                gameOn = False
        Game.screen.fill((75,190,70))
        Game.newFrame()

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()