from main import Game

class Object:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        Game.Objects.append(self)
    def render(self):
