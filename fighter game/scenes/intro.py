import pygame

class Intro:
    def __init__(self, screen, fontIncrement):
        self.screen = screen
        self.fontIncrement = fontIncrement

    def load_assets(self):
        font40 = pygame.font.Font('assets/fonts/font.ttf', self.fontIncrement)
        font20 = pygame.font.Font('assets/fonts/font.ttf', 20)

        title = pygame.image.load("assets/images/title/title.png")
        titler = pygame.transform.scale(title,(1024//1.5,437//1.5))
        self.screen.blit(titler, (180, 80))

        f = font40.render("press spacebar", True, (255, 255, 255))
        fr = f.get_rect()
        fr.center = (512, 450)
        self.screen.blit(f, fr)

        r = font20.render("fillers", True, (255, 255, 255))
        rr = r.get_rect()
        rr.center = (512, 550)
        self.screen.blit(r, rr)

        background = pygame.image.load("assets/images/bckgnd.png").convert_alpha()
        self.screen.blit(background, (0, 0))

