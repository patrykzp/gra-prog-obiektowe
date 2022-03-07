import UI
import pygame
import os

class Menu:
    def __init__(self,game):
        self.game = game
        self.centerwidth, self.centerheight= game.screen.get_size()
        self.centerwidth = self.centerwidth/2
        self.centerheight = self.centerheight/2
        self.start()
    def start(self):
        font = pygame.font.Font(os.path.abspath("8BITWONDER.TTF"),50)
        UI.Button(self.centerwidth,self.centerheight,(200,100),self.game).onClick = self.pressed
        UI.Text(self.centerwidth, self.centerheight, self.game, "GRAJ",font=font)
        UI.Text(self.centerwidth,self.centerheight-100,self.game,"GRA SURVIVAL",font=font)
    def pressed(self):
        self.game.Objects.empty()
        self.game.UI.empty()
        self.game.gameStart()