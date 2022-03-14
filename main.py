#!/usr/bin/env python3
# tu bedzie gra
import pygame
import math
import UI
import mainmenu
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
        player = Game.player
        if hasattr(player,"pos_x"):
            Game.camera = (
                min(max(player.pos_x - size[0] / 2, Game.worldBounds["x"][0]), Game.worldBounds["x"][1]),
                min(max(player.pos_y - size[1] / 2, Game.worldBounds["y"][0]), Game.worldBounds["y"][1])
            )

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
            posx, posy = Game.getRandomPos()

            npc.NPC(posx, posy, 75, (100, 100), Game)
        for i in range(50):
            posx, posy = Game.getRandomPos()
            obstacles.IronOre \
                (posx, posy, (150, 150), Game, HP=125)
        for i in range(50):
            posx, posy = Game.getRandomPos()
            obstacles.Tree \
                (posx, posy, (200, 200), Game, HP=100)
        for i in range(75):
            posx, posy = Game.getRandomPos()
            obstacles.MineableRock \
                (posx, posy, (200, 200), Game, HP=150)
        for i in range(50):
            posx, posy = Game.getRandomPos()
            obstacles.AppleTree \
                (posx, posy, (175, 175), Game, HP=75)

        for i in range(25):
            posx, posy = Game.getRandomPos()
            npc.aggroNPC(posx, posy, 150, (100, 100), Game)
    @staticmethod
    def gameStart():
        # ustawianie tła

        background = Object(0, 0, (640 * 15, 640 * 15), Game)
        background.setImage(pygame.image.load("TrawaBg.jpg"))

        # generowanie elementów terenu

        Game.genTerrain()

        # tworzenie gracza i jego elementów UI

        plr = player.Player(0, 0, (90, 90), Game, player.UiSet(
            foodBar=UI.Bar(100,50,(150,35),Game,(255, 178, 102)),
            healthBar=UI.Bar(100, 100, (150, 35), Game, (255, 51, 51)),
            foodText=UI.Text(100, 50, Game, "glod"),
            hpText=UI.Text(100, 100, Game, "zycie"),
            ironText=UI.Text(100, 150, Game, "e"),
            stoneText=UI.Text(100, 200, Game, "e"),
            woodText=UI.Text(100, 250, Game, "e"),
        ))

        Game.player = plr

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

    clock = pygame.time.Clock()
    Game.input = Input
    mainmenu.Menu(Game)

    # petla gry

    while gameOn:
        Input.mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                Input.mouseDown = True
            if event.type == pygame.QUIT:  # Wyjscie z gry
                gameOn = False
        Game.screen.fill((50,50,50))
        Game.newFrame()
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()