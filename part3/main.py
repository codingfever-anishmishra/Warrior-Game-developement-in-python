import pygame
from pygame.locals import*
from os import path
from sprites import*
from settings import*

class Game(pygame.sprite.Sprite):
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Warrior")
        self.fpsclock = pygame.time.Clock()
        self.running = True
        self.load_data()
        
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'img')
        self.platform_img = pygame.image.load(path.join(img_folder,platform_IMG)).convert_alpha()
        self.enemy_img0 = pygame.image.load(path.join(img_folder, 'Idle_000.png')).convert_alpha()
        self.enemy_img1 = pygame.image.load(path.join(img_folder, 'Idle_001.png')).convert_alpha()
        self.enemy_img2 = pygame.image.load(path.join(img_folder, 'Idle_002.png')).convert_alpha()
        self.enemy_img3 = pygame.image.load(path.join(img_folder, 'Idle_003.png')).convert_alpha()
        self.enemy_img4 = pygame.image.load(path.join(img_folder, 'Idle_004.png')).convert_alpha()
        self.enemy_img5 = pygame.image.load(path.join(img_folder, 'Idle_005.png')).convert_alpha()
        self.enemy_img6 = pygame.image.load(path.join(img_folder, 'Idle_006.png')).convert_alpha()
        self.enemy_img7 = pygame.image.load(path.join(img_folder, 'Idle_007.png')).convert_alpha()
        self.enemy_img8 = pygame.image.load(path.join(img_folder, 'Idle_008.png')).convert_alpha()
        self.enemy_img9 = pygame.image.load(path.join(img_folder, 'Idle_009.png')).convert_alpha()
        self.enemy_img = [self.enemy_img0,self.enemy_img1,self.enemy_img2,self.enemy_img3,self.enemy_img4,self.enemy_img5,self.enemy_img6,self.enemy_img7,self.enemy_img8,self.enemy_img9]
    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platform = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.p = Platform(self)
        self.enemy = Enemy(self,self.p)
    
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.fpsclock.tick(60)/1000
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.playing = False
                self.running = False
    
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
    
    def start_screen(self):
        pass
    
    def go_screen(self):
        pass
    
game=Game()
game.start_screen()
while game.running:
    game.new()
    game.run()
    game.go_screen()


