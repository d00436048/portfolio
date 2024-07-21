import pygame

class Results:
    def __init__(self, screen, player_data):
        self.screen = screen
        self.player_data = player_data
    
    
    def load_assets(self):
        font64 = pygame.font.Font('assets/fonts/font.ttf', 64)
        font160 = pygame.font.Font('assets/fonts/font.ttf', self.player_data["font_increment"]+80)


        f = font64.render("Results", True, (255, 255, 255))
        fr = f.get_rect()
        fr.center = (512, 50)
        self.screen.blit(f, fr)
        
        background = pygame.image.load("assets/images/bckgnd.png").convert_alpha()
        self.screen.blit(background, (0, 0))

        outline = pygame.image.load("assets/images/results/outline.png").convert_alpha()
        self.screen.blit(outline, (412, 150))

        dec1 = pygame.image.load("assets/images/results/dec.png").convert_alpha()
        dec2 = pygame.image.load("assets/images/results/dec.png").convert_alpha()
        dec1r = pygame.transform.scale(dec1, (128, 128))
        dec2r = pygame.transform.scale(dec2, (128,128))
        dec2r = pygame.transform.flip(dec2r, True, False)
        self.screen.blit(dec1r, (357, 235))
        self.screen.blit(dec2r, (530, 235))

        meda = pygame.image.load("assets/images/results/meda.png").convert_alpha()
        meda = pygame.transform.scale(meda, (128, 128))
        self.screen.blit(meda, (440, 400))

        result = font160.render("filler", True, (255, 255, 255))
        result_font = result.get_rect()
        result_font.center = (512, 425)
        self.screen.blit(result, result_font)