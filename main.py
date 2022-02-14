# tu bedzie gra
import pygame

class Object:
    def __init__(self,x,y,size):
        self.pos_x = x
        self.pos_y = y
        self.size = size
        self.model = pygame.rect.Rect(x,y,size[0],size[1])
        Game.Objects.append(self)
    def update(self): # updateowanie pozycji modelu zeby byla taka sama jak pozycja obiektu
        self.model.x = self.pos_x
        self.model.y = self.pos_y
        self.model.size = self.size
    def render(self):
        self.update()
        pygame.draw.rect(Game.screen,(0,0,0), self.model) #wyswietlanie obiektu na ekranie

class Game:
    Objects = []
    screen = None
    @staticmethod
    def newFrame():
        for object in Game.Objects:
            object.render()


if __name__ == "__main__":
    pygame.init()
    size = (700, 500)
    Game.screen = pygame.display.set_mode(size)
    pygame.display.set_caption("gra")
    gameOn = True

    clock = pygame.time.Clock()
    obj1 = Object(10, 10, (250, 250))
    obj2 = Object(300, 100, (50, 50))
    while gameOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Wyjscie z gry
                gameOn = False
        Game.screen.fill((155,155,155))
        Game.newFrame()
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()

