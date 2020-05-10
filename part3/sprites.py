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

class Enemy(pygame.sprite.Sprite):
    def __init__(self,game,platform):
        self.groups = game.all_sprites,game.enemy_group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.enemy_img[0]
        self.rect = self.image.get_rect()
        #self.hit_rect_body = pygame.Rect(0,0,int(self.rect.width*0.3),self.rect.height*0.6)
        #self.hit_rect_head = pygame.Rect(0,0,self.rect.width*0.2,self.rect.height*0.3)
        self.pos = vec(platform.rect.right-20,platform.rect.top+10)
        self.i = 0 # to change image of enemy
    def update(self):
        self.image = self.game.enemy_img[self.i]
        self.rect = self.image.get_rect()
        self.rect.right = self.pos.x
        self.rect.bottom = self.pos.y
        #self.hit_rect_body.right = self.rect.right-30
        #self.hit_rect_body.bottom = self.rect.bottom
        #self.hit_rect_head.right = self.rect.right-50
        #self.hit_rect_head.y = self.rect.top+10
        self.i +=1
        if self.i>= len(self.game.enemy_img)-1:
            self.i = 0
        self.mask = pygame.mask.from_surface(self.image)
