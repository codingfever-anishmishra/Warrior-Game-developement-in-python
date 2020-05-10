import pygame
from pygame.locals import*
from os import path
from sprites import*
from settings import*

class Game(pygame.sprite.Sprite):
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Warrior")
        self.running = True
        self.load_data()
        
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'img')
        self.platform_img = pygame.image.load(path.join(img_folder,platform_IMG)).convert_alpha()
    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platform = pygame.sprite.Group()
        self.p = Platform(self)
    
    def run(self):
        self.playing = True
        while self.playing:
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

