import pygame

class Stats:
    def __init__(self, screen):
        self.screen = screen
    
    
    def load_assets(self):
        font40 = pygame.font.Font('assets/fonts/font.ttf', 40)
        font64 = pygame.font.Font('assets/fonts/font.ttf', 64)

        f = font64.render("Stats", True, (255, 255, 255))
        fr = f.get_rect()
        fr.center = (512, 50)
        self.screen.blit(f, fr)
        
        background = pygame.image.load("assets/images/bckgnd.png").convert_alpha()
        self.screen.blit(background, (0, 0))