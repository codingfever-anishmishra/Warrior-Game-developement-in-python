from random import randrange
from settings import*
import pygame
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.player_img
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT-20
        self.rect.left = 10
        Gun(self.game,self.rect.right-8,self.rect.centery+5)
        
class Gun(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.gun_img
        self.rect = self.image.get_rect()
        self.pos = vec(x,y)
        self.vel = vec(0,0)
        self.rot = 0
        self.rot_speed = 0
        self.down = False
        self.aiming = False
        
    def aim(self):
        if not self.game.launched:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.aiming = True
                if self.down == False:
                    self.rot_speed = 50
                if self.down == True:
                    self.rot_speed = -50
                    
                if self.rot > 75:
                    self.down = True
                if self.rot < -20:
                    self.down = False
            #if not key[pygame.K_SPACE]:
                #self.rot_speed = 0
                #if self.aiming == True:
                    #self.game.launched = True
                    #Bullet(self.game,self.pos,self.rot)
                    #self.aiming = False
                    #self.rot = 0
                    #self.down = False
                    
    def update(self):
        self.aim()
        self.rot = (self.rot + self.rot_speed * self.game.dt)
        self.image = pygame.transform.rotate(self.game.gun_img,self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

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
