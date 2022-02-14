# tu bedzie gra
import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.size = size
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        Game.Objects.add(self)
    def update(self): # updateowanie pozycji modelu zeby byla taka sama jak pozycja obiektu
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

class Game:
    Objects = pygame.sprite.Group()
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

