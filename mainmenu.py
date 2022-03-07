import UI
class Menu:
    def __init__(self,game):
        self.game = game
        self.centerwidth, self.centerheight= game.screen.get_size()
        self.centerwidth = self.centerwidth/2
        self.centerheight = self.centerheight/2
        self.start()
    def start(self):
        UI.Button(self.centerwidth,self.centerheight,(200,100),self.game).onClick = self.pressed
        UI.Text(self.centerwidth, self.centerheight, self.game, "GRAJ")
        UI.Text(self.centerwidth,self.centerheight-100,self.game,"GRA SURVIVAL")
    def pressed(self):
        self.game.Objects.empty()
        self.game.UI.empty()
        self.game.gameStart()