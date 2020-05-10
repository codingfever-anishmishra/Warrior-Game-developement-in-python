from random import randrange
from settings import*
import pygame
vec = pygame.math.Vector2

class Platform(pygame.sprite.Sprite):
    def __init__(self,game):
        self.groups = game.all_sprites,game.platform
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.platform_img
        self.rect = self.image.get_rect()
        x = randrange(int(WIDTH*0.4), int(WIDTH-self.rect.width),50)
        y = randrange(int(10+self.rect.height), int(HEIGHT-self.rect.height-50),50)
        self.pos = vec(x,y)
        self.rect.topleft = self.pos
        self.mask = pygame.mask.from_surface(self.image)
