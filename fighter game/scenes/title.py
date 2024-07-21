import pygame

class Title:
    def __init__(self, screen):
        self.screen = screen
    

    def load_assets(self, marker, marker_w, marker_s, glove, glove2):
        
        font40 = pygame.font.Font('assets/fonts/font.ttf', 40)

        title = pygame.image.load("assets/images/title/title.png")
        titler = pygame.transform.scale(title,(1024//1.5,437//1.5))
        self.screen.blit(titler, (180, 80))

        f = font40.render("Fight", True, (255, 255, 255))
        fr = f.get_rect()
        fr.center = (512, 375)
        self.screen.blit(f, fr)

        s = font40.render("Stats", True, (255, 255, 255))
        sr = s.get_rect()
        sr.center = (512, 425)
        self.screen.blit(s, sr)

        t = font40.render("Cheat Codes", True, (255, 255, 255))
        tr = t.get_rect()
        tr.center = (512, 475)
        self.screen.blit(t, tr)

        if marker == 0:
            icon = pygame.image.load("assets/images/main/boxing_glove.png")
            iconr = pygame.transform.scale(icon,(32, 32))
            self.screen.blit(iconr, (glove, 360))
        elif marker == 1:
            icon = pygame.image.load("assets/images/main/boxing_glove.png")
            iconr = pygame.transform.scale(icon,(32, 32))
            self.screen.blit(iconr, (glove, 410))
        elif marker == 2:
            icon = pygame.image.load("assets/images/main/boxing_glove.png")
            iconr = pygame.transform.scale(icon,(32, 32))
            self.screen.blit(iconr, (glove2, 460))
        
        background = pygame.image.load("assets/images/bckgnd.png").convert_alpha()
        self.screen.blit(background, (0, 0))


    def keyboard_inputs(self, marker, marker_w, marker_s):
        cursor_move = pygame.mixer.Sound("assets/music/soundfx/character select/cursor_move.wav")

        key = pygame.key.get_pressed()

        if key[pygame.K_s]:
            if marker < 2:
                marker_w += .1p
                if marker_w >= .4:
                    pygame.mixer.Sound.play(cursor_move)
                    marker +=1
                    marker_w = 0
            elif marker == 2:
                marker_w += .1
                if marker_w >= .4:
                    pygame.mixer.Sound.play(cursor_move)
                    marker = 0
                    marker_w = 0
        
        if key[pygame.K_w]:
            if marker > 0:
                marker_s += .1
                if marker_s >= .4:
                    pygame.mixer.Sound.play(cursor_move)
                    marker -=1
                    marker_s = 0
            elif marker == 0:
                marker_s += .1
                if marker_s >= .4:
                    pygame.mixer.Sound.play(cursor_move)
                    marker = 2
                    marker_s = 0

        return marker, marker_w, marker_s