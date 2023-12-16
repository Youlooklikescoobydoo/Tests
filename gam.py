import pygame
from pygame.locals import *

display = pygame.display.set_mode((300,300))

fps = pygame.time.Clock()

green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)
white = (0,0,0)
black = (255,255,255)

display.fill(white)

pygame.display.set_caption("Gam")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load()
        self.rect = self.image.get.rect()
        self.rect.center = (random.randint(40, screenwidth-40),0)

    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.move_ip(-5,0)
        if self.rect.right < screenwidth:
            if pressed_keys[K_RIGHT]:
                self.move_ip(5,0)
        
        def draw(self, surface):
            surface.blit(self.image, self.rect)
            
P1 = Player()
EN = Enemy()

screenwidth = 500
screenheight = 600

pygame.init()

while True:
    pass
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    
    P1.update()
    EN.move()
    
    display.fill(white)
    P1.draw(display)
    EN.draw(display)

    pygame.display.update()
    fps.tick(60)