import pygame

#import levels
import test_level
import test_level2

#import players
from entities import player

#helper functions
def draw_health_bar(screen, health, x, y, flip):
    hp_surface = pygame.Surface((310,32))

    pygame.draw.rect(hp_surface, (0, 0, 0), (0, 0, 310, 300))

    ratio = health / 100
    hp_width = int(310 * ratio)

    pygame.draw.rect(hp_surface, (255, 28, 0), (0, 0, hp_width, 30))



    if flip == True:
        hp_surface = pygame.transform.flip(hp_surface, True, False)
    
    screen.blit(hp_surface, (x, y))



class Game:
    def __init__(self, player_data, screen):
        self.screen = screen
        self.level = player_data["level"]
        self.player_data = player_data

            #define variables
        self.p1Health = player_data["p1_character"][1]
        self.p2Health = player_data["p2_character"][1]

    def load_level(self):
        if self.level == "test_level":
            test_level.load_test_level(self.screen, self.player_data)
            #print("test_level_loaded")

        if self.level == "test_level2":
            test_level2.load_test_level2(self.screen, self.player_data)
            #print("test_level_loaded")

    def load_ui(self):
        font40 = pygame.font.Font('assets/fonts/font.ttf', 40)

        #load ui
        draw_health_bar(self.screen, self.p1Health, 106, 53, False)
        draw_health_bar(self.screen, self.p2Health, 608, 53, True)

        icon_outline = pygame.image.load("assets/images/icon_outline.png")
        icon_outline_rect = pygame.transform.scale(icon_outline, (80,80))
        icon_outline_rect_p2 = pygame.transform.flip(icon_outline_rect, True, False)
        self.screen.blit(icon_outline_rect, (20, 20))
        self.screen.blit(icon_outline_rect_p2, (924, 20))

        hp_outline = pygame.image.load("assets/images/hp_outline.png")
        hp_outline_rect = pygame.transform.scale(hp_outline, (325,53))
        hp_outline_rect_p2 = pygame.transform.flip(hp_outline_rect, True, False)
        self.screen.blit(hp_outline_rect, (94, 32))
        self.screen.blit(hp_outline_rect_p2, (605, 32))

        #display player icons
        t = pygame.image.load("assets/images/character selection/tess icon.png").convert_alpha()
        tr = pygame.transform.scale(t,(70,70))
        s = pygame.image.load("assets/images/character selection/sammie icon.png").convert_alpha()
        sr = pygame.transform.scale(s,(70,70))
        m = pygame.image.load("assets/images/character selection/maggie icon.png").convert_alpha()
        mr = pygame.transform.scale(m,(70,70))
        b = pygame.image.load("assets/images/character selection/brain icon.png").convert_alpha()
        br = pygame.transform.scale(b,(70,70))
        a = pygame.image.load("assets/images/character selection/amanda icon.png").convert_alpha()
        ar = pygame.transform.scale(a,(70,70))
        e = pygame.image.load("assets/images/character selection/bridger icon.png").convert_alpha()
        er = pygame.transform.scale(e,(70,70))
        mb = pygame.image.load("assets/images/character selection/mb icon.png").convert_alpha()
        mbr = pygame.transform.scale(mb,(70,70))

        if self.player_data["p1_character"][0] == "Tess":
            self.screen.blit(tr, (22, 22))
        if self.player_data["p1_character"][0] == "Sammie":
            self.screen.blit(sr, (22, 22))
        if self.player_data["p1_character"][0] == "Maggie":
            self.screen.blit(mr, (22, 2))
        if self.player_data["p1_character"][0] == "Br ian":
            self.screen.blit(br, (22, 22))
        if self.player_data["p1_character"][0] == "Amanda":
            self.screen.blit(ar, (22, 22))
        if self.player_data["p1_character"][0] == "Bridger":
            self.screen.blit(er, (22, 22))
        if self.player_data["p1_character"][0] == "Missionary Boyfrined":
            self.screen.blit(mbr, (22, 2))
            

        t2 = pygame.image.load("assets/images/character selection/tess icon.png").convert_alpha()
        t2r = pygame.transform.scale(t2,(70,70))
        s2 = pygame.image.load("assets/images/character selection/sammie icon.png").convert_alpha()
        s2r = pygame.transform.scale(s2,(70,70))
        m2 = pygame.image.load("assets/images/character selection/maggie icon.png").convert_alpha()
        m2r = pygame.transform.scale(m2,(70,70))
        b2 = pygame.image.load("assets/images/character selection/brain icon.png").convert_alpha()
        b2r = pygame.transform.scale(b2,(70,70))
        a2 = pygame.image.load("assets/images/character selection/amanda icon.png").convert_alpha()
        a2r = pygame.transform.scale(a2,(70,70))
        e2 = pygame.image.load("assets/images/character selection/bridger icon.png").convert_alpha()
        e2r = pygame.transform.scale(e2,(70,70))
        mb2 = pygame.image.load("assets/images/character selection/mb icon.png").convert_alpha()
        mb2r = pygame.transform.scale(mb2,(70,70))

        if self.player_data["p2_character"][0] == "Tess":
            t2r = pygame.transform.flip(t2r, True, False)
            self.screen.blit(t2r, (930, 22))
        if self.player_data["p2_character"][0] == "Sammie":
            s2r = pygame.transform.flip(s2r, True, False)
            self.screen.blit(s2r, (930, 22))
        if self.player_data["p2_character"][0] == "Maggie":
            m2r = pygame.transform.flip(m2r, True, False)
            self.screen.blit(m2r, (930, 2))
        if self.player_data["p2_character"][0] == "Brian":
            b2r = pygame.transform.flip(b2r, True, False)
            self.screen.blit(b2r, (930, 22))
        if self.player_data["p2_character"][0] == "Amanda":
            a2r = pygame.transform.flip(a2r, True, False)
            self.screen.blit(a2r, (930, 22))
        if self.player_data["p2_character"][0] == "Bridger":
            e2r = pygame.transform.flip(e2r, True, False)
            self.screen.blit(e2r, (930, 22))
        if self.player_data["p2_character"][0] == "Missionary Boyfrined":
            mb2r = pygame.transform.flip(mb2r, True, False)
            self.screen.blit(mb2r, (930, 2))



                #player tag
        p1_character = font40.render("TESS", True, (255, 255, 255))
        p1_character_rect = p1_character.get_rect()
        p1_character_rect.center = (150, 30)
        self.screen.blit(p1_character, p1_character_rect)
        
        p1 = font40.render("Player 1", True, (255, 0, 0))
        p1_rect = p1.get_rect()
        p1_rect.center = (73, 120)
        self.screen.blit(p1, p1_rect)

        p2 = font40.render("Player 2", True, (0, 0, 255))
        p2_rect = p2.get_rect()
        p2_rect.center = (950, 120)
        self.screen.blit(p2, p2_rect)
        


