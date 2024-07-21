import copy
import pygame
from characters import level_list
class LevelSelect:
    def __init__(self, player_data, game_stats, screen):
        self.screen = screen

        player_data["level"] = copy.deepcopy(level_list[player_data["level_tally"]][0])



    def load_level_selection(self, player_data):
        font20 =  pygame.font.Font('assets/fonts/font.ttf', 20)
        font32 = pygame.font.Font('assets/fonts/font.ttf', 32)
        font40 =  pygame.font.Font('assets/fonts/font.ttf', 40)
        font64 = pygame.font.Font('assets/fonts/font.ttf', 64)


        f = font64.render("Select Level", True, (255, 255, 255))
        fr = f.get_rect()
        fr.center = (512, 50)
        self.screen.blit(f, fr)

        select_box = pygame.Surface((200,200))
        select_box.set_alpha(200)
        select_box.fill((50, 50, 50))

        #level select icon
        rsb = pygame.image.load("assets/images/character selection/red_icon_select.png").convert_alpha()
        rsb = pygame.transform.scale(rsb, (200, 200))
        if player_data["level"] == "backyard":
            font = font64.render("The Backyard", True, (255, 255, 255))
            font_rect = font.get_rect()
            font_rect.center = (225, 300)
            self.screen.blit(font, font_rect)
            self.screen.blit(rsb, (150, 50))
        if player_data["level"] == "garage":
            font = font64.render("The Garage", True, (255, 255, 255))
            font_rect = font.get_rect()
            font_rect.center = (500, 300)
            self.screen.blit(font, font_rect)
            self.screen.blit(rsb, (400, 50))
        if player_data["level"] == "kitchen":
            font = font64.render("The Kitchen", True, (255, 255, 255))
            font_rect = font.get_rect()
            font_rect.center = (775, 300)
            self.screen.blit(font, font_rect)
            self.screen.blit(rsb, (675, 50))
        if player_data["level"] == "backyard2":
            font = font64.render("The Backyard 2", True, (255, 255, 255))
            font_rect = font.get_rect()
            font_rect.center = (250, 550)
            self.screen.blit(font, font_rect)
            self.screen.blit(rsb, (150, 325))
        if player_data["level"] == "escalante":
            font = font64.render("The Escalante", True, (255, 255, 255))
            font_rect = font.get_rect()
            font_rect.center = (500, 550)
            self.screen.blit(font, font_rect)
            self.screen.blit(rsb, (400, 325))
        if player_data["level"] == "quick_quack":
            font = font64.render("Quick Quack Car Wash", True, (255, 255, 255))
            font_rect = font.get_rect()
            font_rect.center = (700, 550)
            self.screen.blit(font, font_rect)
            self.screen.blit(rsb, (675, 325))

        if player_data["level"] == "backyard" and player_data["level_selected"] == True:
            self.screen.blit(select_box, (150, 50))
        if player_data["level"] == "garage" and player_data["level_selected"] == True:
            self.screen.blit(select_box, (400, 50))
        if player_data["level"] == "kitchen" and player_data["level_selected"] == True:
            self.screen.blit(select_box, (675, 50))
        if player_data["level"] == "backyard2" and player_data["level_selected"] == True:
            self.screen.blit(select_box, (150, 325))
        if player_data["level"] == "escalante" and player_data["level_selected"] == True:
            self.screen.blit(select_box, (400, 325))
        if player_data["level"] == "quick_quack" and player_data["level_selected"] == True:
            self.screen.blit(select_box, (675, 325))

    def level_selection(self, player_data):
        #def sound effects
        cursor_move = pygame.mixer.Sound("assets/music/soundfx/character select/cursor_move.wav")
        character_selected = pygame.mixer.Sound("assets/music/soundfx/character select/character_select.wav")

        key = pygame.key.get_pressed()

        if player_data["level_selected"] == False:
            if key[pygame.K_d]:
                if player_data["level_tally"] < 5:
                    player_data["level_tally_d"] += .1
                    if player_data["level_tally_d"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["level_tally"] += 1
                        player_data["level_tally_d"] = 0
                elif player_data["level_tally"] == 5:
                    player_data["level_tally_d"] += .1
                    if player_data["level_tally_d"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["level_tally"] = 0
                        player_data["level_tally_d"] = 0

                level_appended = level_list[player_data["level_tally"]]
                level_appended = level_appended[0]
                player_data["level"] = level_appended
                #self.show_character_choices(player_data)

            if key[pygame.K_a]:
                if player_data["level_tally"] > 0:
                    player_data["level_tally_a"] += .1
                    if player_data["level_tally"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["level_tally"] -= 1
                        player_data["level_tally_a"] = 0
                elif player_data["level_tally"] == 0:
                    player_data["level_tally_a"] += .1
                    if player_data["level_tally_a"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["level_tally"] = 5
                        player_data["level_tally_a"] = 0

                print(player_data["level_tally"])
                print(player_data["level"])
                level_appended = level_list[player_data["level_tally"]]
                level_appended = level_appended[0]
                player_data["level"] = level_appended
                #self.show_character_choices(player_data)

        if key[pygame.K_q]:
            if player_data["level_selected"] == False:
                player_data["level_selected"] = True
                pygame.mixer.Sound.play(character_selected)
            else:
                player_data["level_selected"] = False