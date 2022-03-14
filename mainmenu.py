import UI
import pygame
import os
import random

class Menu:
    def __init__(self,game):
        self.game = game
        self.centerwidth, self.centerheight= game.screen.get_size()
        self.centerwidth = self.centerwidth/2
        self.centerheight = self.centerheight/2
        self.start()
    def start(self):
        font = pygame.font.Font(os.path.abspath("8BITWONDER.TTF"),50)
        font2 = pygame.font.Font(os.path.abspath("8BITWONDER.TTF"),45)
        UI.Button(self.centerwidth,self.centerheight-100,(350,100),self.game).onClick = self.pressed
        UI.Text(self.centerwidth, self.centerheight-100, self.game, "GRAJ",font=font2,textColor=pygame.color.Color("black"))

        UI.Text(self.centerwidth,self.centerheight-200,self.game,"GRA SURVIVAL",font=font,textColor=pygame.color.Color("white"))

        UI.Button(self.centerwidth, self.centerheight+25, (350, 100), self.game).onClick = self.pressedAuthors
        UI.Text(self.centerwidth, self.centerheight+25, self.game, "AUTORZY", font=font2,
                textColor=pygame.color.Color("black"))
        UI.Button(self.centerwidth, self.centerheight + 150, (350, 100), self.game).onClick = self.pressedTutorial
        UI.Text(self.centerwidth, self.centerheight + 150, self.game, "JAK GRAC", font=font2,
                textColor=pygame.color.Color("black"))


    def clearScene(self):
        self.game.Objects.empty()
        self.game.UI.empty()

    def pressed(self):
        self.clearScene()
        self.game.gameStart()
    def pressedAuthors(self):
        self.clearScene()
        Authors(self.game)
    def pressedTutorial(self):
        self.clearScene()
        Tutorial(self.game)

class Authors(Menu):
    def start(self):
        font = pygame.font.Font(os.path.abspath("COMIC.TTF"), 25)
        font2 = pygame.font.Font(os.path.abspath("COMIC.TTF"), 35)
        UI.Text(self.centerwidth, self.centerheight-25, self.game, "Autorzy gry:", font=font2,
                textColor=pygame.color.Color("white"))
        UI.Text(self.centerwidth, self.centerheight+25, self.game, "Bartosz Szylkowski, Radoslaw Kaliszuk, Patryk Zajkowski, Patryk Mantaj", font=font,
                textColor=pygame.color.Color("white"))

        UI.Button(self.centerwidth, self.centerheight + 125, (350, 100), self.game).onClick = self.goBack
        UI.Text(self.centerwidth, self.centerheight + 125, self.game,
                "WROC", font=pygame.font.Font(os.path.abspath("8BITWONDER.TTF"),45),
                textColor=pygame.color.Color("black"))
    def goBack(self):
        self.clearScene()
        Menu(self.game)
class Tutorial(Authors):
    def start(self):
        font = pygame.font.Font(os.path.abspath("COMIC.TTF"), 25)
        font2 = pygame.font.Font(os.path.abspath("COMIC.TTF"), 35)

        UI.Text(self.centerwidth, self.centerheight - 250, self.game, "Jak grac?", font=font2,
                textColor=pygame.color.Color("white"))
        UI.Text(self.centerwidth, self.centerheight-150, self.game,
                "WSAD - Poruszanie sie", font=font,
                textColor=pygame.color.Color("white"))
        UI.Text(self.centerwidth, self.centerheight-100, self.game,
                "Lewy przycisk myszy - Uderzanie/Interakcja", font=font,
                textColor=pygame.color.Color("white"))
        UI.Text(self.centerwidth, self.centerheight-50, self.game,
                "Celem gry jest przetrwanie i zebranie jak najwiecej materialow", font=font,
                textColor=pygame.color.Color("white"))
        UI.Text(self.centerwidth, self.centerheight, self.game,
                "Cala gre glod spada, jezeli spadnie do zera gracz zaczyna tracic zdrowie", font=font,
                textColor=pygame.color.Color("white"))
        UI.Text(self.centerwidth, self.centerheight+50, self.game,
                "By zaspokoic glod, nalezy zabic krowe lub uderzyc jablon", font=font,
                textColor=pygame.color.Color("white"))


        UI.Button(self.centerwidth, self.centerheight + 150, (350, 100), self.game).onClick = self.goBack
        UI.Text(self.centerwidth, self.centerheight + 150, self.game,
                "WROC", font=pygame.font.Font(os.path.abspath("8BITWONDER.TTF"), 45),
                textColor=pygame.color.Color("black"))
        a = UI.UIObject(150,600,(300,300),self.game)
        a.setImage(pygame.image.load("krowa.png"))
        if random.randint(0,10)==0:
            a.setImage(pygame.image.load("damian.png"))
        a.update()
class DeathScreen(Menu):
    def start(self):
        self.clearScene()
        font = pygame.font.Font(os.path.abspath("8BITWONDER.TTF"),50)
        font2 = pygame.font.Font(os.path.abspath("8BITWONDER.TTF"),45)
        UI.Button(self.centerwidth,self.centerheight,(300,100),self.game).onClick = self.pressed
        UI.Text(self.centerwidth, self.centerheight, self.game, "POWROT",font=font2,textColor=pygame.color.Color("black"))

        UI.Text(self.centerwidth,self.centerheight-100,self.game,"NIE ZYJESZ",font=font,textColor=pygame.color.Color("white"))
    def pressed(self):
        self.clearScene()
        Menu(self.game)