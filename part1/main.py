import pygame
from pygame.locals import*
from settings import*

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Warrior")
        self.running = True
        self.load_data()
    def load_data(self):
        pass
    
    def new(self):
        pass
    
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
        pass
    
    def draw(self):
        self.screen.fill(WHITE)
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


