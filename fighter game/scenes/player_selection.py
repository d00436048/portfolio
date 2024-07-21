import copy
import pygame
from characters import character_list

icon_height = 450


class PlayerSelect:
    def __init__(self, player_data, game_stats, screen):
        self.screen = screen

        player_data["p1_character"] = copy.deepcopy(character_list[player_data["p1_tally"]])
        player_data["p2_character"] = copy.deepcopy(character_list[player_data["p2_tally"]])

    def show_character_choices(self, player_data):
        font20 =  pygame.font.Font('assets/fonts/font.ttf', 20)
        font32 = pygame.font.Font('assets/fonts/font.ttf', 32)
        font40 =  pygame.font.Font('assets/fonts/font.ttf', 40)
        font64 = pygame.font.Font('assets/fonts/font.ttf', player_data["font_increment"])
        font64_Static = pygame.font.Font('assets/fonts/font.ttf', 64)

        #background
        background = pygame.image.load("assets/images/character selection/background.png").convert_alpha()
        self.screen.blit(background, (0, 0))
        f = font64_Static.render("Select Character", True, (255, 255, 255))
        fr = f.get_rect()
        fr.center = (512, 50)
        self.screen.blit(f, fr)
        if player_data["p1_selected"] == False or player_data["p2_selected"] == False:
            vs_font = font64.render("VS", True, (255, 255, 255))
            vs_font_rect = vs_font.get_rect()
            vs_font_rect.center = (512, 300)
            self.screen.blit(vs_font, vs_font_rect)
            circle = pygame.image.load("assets/images/character selection/circle.png").convert_alpha()
            self.screen.blit(circle, (512 - 50, 250))
        
        #player icon boxes
        pygame.draw.rect(self.screen, (255, 255, 255), (1024/2 - 340, icon_height, 80, 80))
        pygame.draw.rect(self.screen, (255, 255, 255), (1024/2 - 240, icon_height, 80, 80))
        pygame.draw.rect(self.screen, (255, 255, 255), (1024/2 - 140, icon_height, 80, 80))
        pygame.draw.rect(self.screen, (255, 255, 255), (1024/2 - 40, icon_height, 80, 80))
        pygame.draw.rect(self.screen, (255, 255, 255), (1024/2 + 60, icon_height, 80, 80))
        pygame.draw.rect(self.screen, (255, 255, 255), (1024/2 + 160, icon_height, 80, 80))
        pygame.draw.rect(self.screen, (255, 255, 255), (1024/2 + 260, icon_height, 80, 80))

        #display player icons
        t = pygame.image.load("assets/images/character selection/tess icon.png").convert_alpha()
        tr = pygame.transform.scale(t,(75,75))
        s = pygame.image.load("assets/images/character selection/sammie icon.png").convert_alpha()
        sr = pygame.transform.scale(s,(75,75))
        m = pygame.image.load("assets/images/character selection/maggie icon.png").convert_alpha()
        mr = pygame.transform.scale(m,(75,75))
        b = pygame.image.load("assets/images/character selection/brain icon.png").convert_alpha()
        br = pygame.transform.scale(b,(75,75))
        a = pygame.image.load("assets/images/character selection/amanda icon.png").convert_alpha()
        ar = pygame.transform.scale(a,(75,75))
        e = pygame.image.load("assets/images/character selection/bridger icon.png").convert_alpha()
        er = pygame.transform.scale(e,(75,75))
        mb = pygame.image.load("assets/images/character selection/mb icon.png").convert_alpha()
        mbr = pygame.transform.scale(mb,(75,75))
        self.screen.blit(tr, (1024/2 - 340, icon_height))
        self.screen.blit(sr, (1024/2 - 240, icon_height))
        self.screen.blit(mr, (1024/2 - 140, icon_height))
        self.screen.blit(br, (1024/2 - 40, icon_height))
        self.screen.blit(ar, (1024/2 + 60, icon_height))
        self.screen.blit(er, (1024/2 + 160, icon_height))
        self.screen.blit(mbr, (1024/2 + 260, icon_height))

        #player icon selected
        select_box = pygame.Surface((80,80))
        select_box.set_alpha(200)
        select_box.fill((50, 50, 50))

        if player_data["p1_selected"] and player_data["p1_character"][0] == "Tess":
            self.screen.blit(select_box, (1024/2 - 340, icon_height))
        elif player_data["p1_selected"] and player_data["p1_character"][0] == "Sammie":
            self.screen.blit(select_box, (1024/2 - 240, icon_height))
        elif player_data["p1_selected"] and player_data["p1_character"][0] == "Maggie":
            self.screen.blit(select_box, (1024/2 - 140, icon_height))
        elif player_data["p1_selected"] and player_data["p1_character"][0] == "Brian":
            self.screen.blit(select_box, (1024/2 - 40, icon_height))
        elif player_data["p1_selected"] and player_data["p1_character"][0] == "Amanda":
            self.screen.blit(select_box, (1024/2 + 60, icon_height))
        elif player_data["p1_selected"] and player_data["p1_character"][0] == "Bridger":
            self.screen.blit(select_box, (1024/2 + 160, icon_height))
        elif player_data["p1_selected"] and player_data["p1_character"][0] == "Missionary Boyfriend":
            self.screen.blit(select_box, (1024/2 + 260, icon_height))

        if player_data["p2_selected"] and player_data["p2_character"][0] == "Tess":
            self.screen.blit(select_box, (1024/2 - 340, icon_height))
        elif player_data["p2_selected"] and player_data["p2_character"][0] == "Sammie":
            self.screen.blit(select_box, (1024/2 - 240, icon_height))
        elif player_data["p2_selected"] and player_data["p2_character"][0] == "Maggie":
            self.screen.blit(select_box, (1024/2 - 140, icon_height))
        elif player_data["p2_selected"] and player_data["p2_character"][0] == "Brian":
            self.screen.blit(select_box, (1024/2 - 40, icon_height))
        elif player_data["p2_selected"] and player_data["p2_character"][0] == "Amanda":
            self.screen.blit(select_box, (1024/2 + 60, icon_height))
        elif player_data["p2_selected"] and player_data["p2_character"][0] == "Bridger":
            self.screen.blit(select_box, (1024/2 + 160, icon_height))
        elif player_data["p2_selected"] and player_data["p2_character"][0] == "Missionary Boyfriend":
            self.screen.blit(select_box, (1024/2 + 260, icon_height))

        #character scene change tag
        if player_data["p1_selected"] == True and player_data["p2_selected"] == True:
            ready_font = font64.render("READY", True, (255, 0, 0))
            ready_font_rect = ready_font.get_rect()
            ready_font_rect.center = (512, 250)
            ready_button_font = font64.render("press spacebar", True, (255, 0, 0))
            ready_button_font_rect = ready_button_font.get_rect()
            ready_button_font_rect.center = (512, 300)
            self.screen.blit(ready_font, ready_font_rect)
            self.screen.blit(ready_button_font, ready_button_font_rect)




        #player tag
        character1_tag_font = font40.render("Player 1", True, (255, 0, 0))
        character1_tag_rect = character1_tag_font.get_rect()
        character1_tag_rect.center = (225,100)
        character2_tag_font = font40.render("Player 2", True, (0, 0, 255))
        character2_tag_rect = character2_tag_font.get_rect()
        character2_tag_rect.center = (799,100)
        self.screen.blit(character1_tag_font, character1_tag_rect)
        self.screen.blit(character2_tag_font, character2_tag_rect)

        #player character choice
        character1_render = font32.render(player_data["p1_character"][0], True, (255,255,255))
        character1_redner_rect = character1_render.get_rect()
        character1_redner_rect.center = (225,135)
        character2_render = font32.render(player_data["p2_character"][0], True, (255,255,255))
        character2_redner_rect = character2_render.get_rect()
        character2_redner_rect.center = (799,135)
        self.screen.blit(character1_render, character1_redner_rect)
        self.screen.blit(character2_render, character2_redner_rect)

        #stats
        character1_stats_sp = font20.render("Speed: " + player_data["p1_character"][2], True, (255, 255, 255))
        character1_stats_sp_rect = character1_stats_sp.get_rect()
        character1_stats_sp_rect.center = (345,225)
        character1_stats_s = font20.render("Strength: " + player_data["p1_character"][3], True, (255, 255, 255))
        character1_stats_s_rect = character1_stats_s.get_rect()
        character1_stats_s_rect.center = (357,250)
        character1_stats_d = font20.render("Defense: " + player_data["p1_character"][4], True, (255, 255, 255))
        character1_stats_d_rect = character1_stats_d.get_rect()
        character1_stats_d_rect.center = (353,275)
        self.screen.blit(character1_stats_sp, character1_stats_sp_rect)
        self.screen.blit(character1_stats_s, character1_stats_s_rect)
        self.screen.blit(character1_stats_d, character1_stats_d_rect)

        character2_stats_sp = font20.render("Speed: " + player_data["p2_character"][2], True, (255, 255, 255))
        character2_stats_sp_rect = character2_stats_sp.get_rect()
        character2_stats_sp_rect.center = (675 ,225)
        character2_stats_s = font20.render("Strength: " + player_data["p2_character"][3], True, (255, 255, 255))
        character2_stats_s_rect = character2_stats_s.get_rect()
        character2_stats_s_rect.center = (687,250)
        character2_stats_d = font20.render("Defense: " + player_data["p2_character"][4], True, (255, 255, 255))
        character2_stats_d_rect = character2_stats_d.get_rect()
        character2_stats_d_rect.center = (683,275)
        self.screen.blit(character2_stats_sp, character2_stats_sp_rect)
        self.screen.blit(character2_stats_s, character2_stats_s_rect)
        self.screen.blit(character2_stats_d, character2_stats_d_rect)


        #selection boxes
        rsb = pygame.image.load("assets/images/character selection/red_icon_select.png").convert_alpha()
        bsb = pygame.image.load("assets/images/character selection/blue_icon_select.png").convert_alpha()
        if player_data["p1_character"][0] == "Tess":
            self.screen.blit(rsb, (1024/2 - 342, icon_height-2))
        elif player_data["p1_character"][0] == "Sammie":
            self.screen.blit(rsb, (1024/2 - 242, icon_height-2))
        elif player_data["p1_character"][0] == "Maggie":
            self.screen.blit(rsb, (1024/2 - 142, icon_height-2))
        elif player_data["p1_character"][0] == "Brian":
            self.screen.blit(rsb, (1024/2 - 42, icon_height-2))
        elif player_data["p1_character"][0] == "Amanda":
            self.screen.blit(rsb, (1024/2 + 58, icon_height-2))
        elif player_data["p1_character"][0] == "Bridger":
            self.screen.blit(rsb, (1024/2 + 158, icon_height-2))
        elif player_data["p1_character"][0] == "Missionary Boyfriend":
            self.screen.blit(rsb, (1024/2 + 258, icon_height-2))
        
        if player_data["p2_character"][0] == "Tess":
            self.screen.blit(bsb, (1024/2 - 342, icon_height-2))
        elif player_data["p2_character"][0] == "Sammie":
            self.screen.blit(bsb, (1024/2 - 242, icon_height-2))
        elif player_data["p2_character"][0] == "Maggie":
            self.screen.blit(bsb, (1024/2 - 142, icon_height-2))
        elif player_data["p2_character"][0] == "Brian":
            self.screen.blit(bsb, (1024/2 - 42, icon_height-2))
        elif player_data["p2_character"][0] == "Amanda":
            self.screen.blit(bsb, (1024/2 + 58, icon_height-2))
        elif player_data["p2_character"][0] == "Bridger":
            self.screen.blit(bsb, (1024/2 + 158, icon_height-2))
        elif player_data["p2_character"][0] == "Missionary Boyfriend":
            self.screen.blit(bsb, (1024/2 + 258, icon_height-2))

        #show character sprites
        if player_data["p1_character"][0] == "Tess":
            ts = pygame.image.load("assets/images/character selection/tess sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            self.screen.blit(tsr, (190, 200))
        elif player_data["p1_character"][0] == "Sammie":
            ts = pygame.image.load("assets/images/character selection/sammie sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            self.screen.blit(tsr, (190, 200))
        elif player_data["p1_character"][0] == "Maggie":
            ts = pygame.image.load("assets/images/character selection/maggie sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            self.screen.blit(tsr, (190, 200))
        elif player_data["p1_character"][0] == "Brian":
            ts = pygame.image.load("assets/images/character selection/brian sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            self.screen.blit(tsr, (190, 200))
        elif player_data["p1_character"][0] == "Amanda":
            ts = pygame.image.load("assets/images/character selection/amanda sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            self.screen.blit(tsr, (190, 200))
        elif player_data["p1_character"][0] == "Bridger":
            ts = pygame.image.load("assets/images/character selection/bridger sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            self.screen.blit(tsr, (190, 200))
        elif player_data["p1_character"][0] == "Missionary Boyfriend":
            ts = pygame.image.load("assets/images/character selection/mb sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            self.screen.blit(tsr, (190, 200))
        
        if player_data["p2_character"][0] == "Tess":
            ts = pygame.image.load("assets/images/character selection/tess sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            tsr = pygame.transform.flip(tsr, True, False) 
            self.screen.blit(tsr, (764, 200))
        elif player_data["p2_character"][0] == "Sammie":
            ts = pygame.image.load("assets/images/character selection/sammie sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            tsr = pygame.transform.flip(tsr, True, False) 
            self.screen.blit(tsr, (764, 200))
        elif player_data["p2_character"][0] == "Maggie":
            ts = pygame.image.load("assets/images/character selection/maggie sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            tsr = pygame.transform.flip(tsr, True, False) 
            self.screen.blit(tsr, (764, 200))
        elif player_data["p2_character"][0] == "Brian":
            ts = pygame.image.load("assets/images/character selection/brian sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            tsr = pygame.transform.flip(tsr, True, False) 
            self.screen.blit(tsr, (764, 200))
        elif player_data["p2_character"][0] == "Amanda":
            ts = pygame.image.load("assets/images/character selection/amanda sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            tsr = pygame.transform.flip(tsr, True, False) 
            self.screen.blit(tsr, (764, 200))
        elif player_data["p2_character"][0] == "Bridger":
            ts = pygame.image.load("assets/images/character selection/bridger sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            tsr = pygame.transform.flip(tsr, True, False) 
            self.screen.blit(tsr, (764, 200))
        elif player_data["p2_character"][0] == "Missionary Boyfriend":
            ts = pygame.image.load("assets/images/character selection/mb sprite.png").convert_alpha()
            tsr = pygame.transform.scale(ts,(80,150))
            tsr = pygame.transform.flip(tsr, True, False) 
            self.screen.blit(tsr, (764, 200))


    def character_selection(self, player_data):
        #def sound effects
        cursor_move = pygame.mixer.Sound("assets/music/soundfx/character select/cursor_move.wav")
        character_selected = pygame.mixer.Sound("assets/music/soundfx/character select/character_select.wav")

        key = pygame.key.get_pressed()

        if player_data["p1_selected"] == False:
            if key[pygame.K_d]:
                if player_data["p1_tally"] < 6:
                    player_data["p1_tally_d"] += .1
                    if player_data["p1_tally_d"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["p1_tally"] +=1
                        player_data["p1_tally_d"] = 0
                elif player_data["p1_tally"] == 6:
                    player_data["p1_tally_d"] += .1
                    if player_data["p1_tally_d"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["p1_tally"] = 0
                        player_data["p1_tally_d"] = 0

                player_data["p1_character"] = character_list[player_data["p1_tally"]]
                self.show_character_choices(player_data)

            if key[pygame.K_a]:
                if player_data["p1_tally"] > 0:
                    player_data["p1_tally_a"] += .1
                    if player_data["p1_tally_a"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["p1_tally"] -=1
                        player_data["p1_tally_a"] = 0
                elif player_data["p1_tally"] == 0:
                    player_data["p1_tally_a"] += .1
                    if player_data["p1_tally_a"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["p1_tally"] = 6
                        player_data["p1_tally_a"] = 0

                player_data["p1_character"] = character_list[player_data["p1_tally"]]
                self.show_character_choices(player_data)
        
        if player_data["p2_selected"] == False:
            if key[pygame.K_l]:
                if player_data["p2_tally"] < 6:
                    player_data["p2_tally_l"] += .1
                    if player_data["p2_tally_l"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["p2_tally"] +=1
                        player_data["p2_tally_l"] = 0
                elif player_data["p2_tally"] == 6:
                    player_data["p2_tally_l"] += .1
                    if player_data["p2_tally_l"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["p2_tally"] = 0
                        player_data["p2_tally_l"] = 0

                player_data["p2_character"] = character_list[player_data["p2_tally"]]
                self.show_character_choices(player_data)

            if key[pygame.K_j]:
                if player_data["p2_tally"] > 0:
                    player_data["p2_tally_j"] += .1
                    if player_data["p2_tally_j"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["p2_tally"] -=1
                        player_data["p2_tally_j"] = 0
                elif player_data["p2_tally"] == 0:
                    player_data["p2_tally_j"] += .1
                    if player_data["p2_tally_j"] >= .4:
                        pygame.mixer.Sound.play(cursor_move)
                        player_data["p2_tally"] = 6
                        player_data["p2_tally_j"] = 0

                player_data["p2_character"] = character_list[player_data["p2_tally"]]
                self.show_character_choices(player_data)

        if key[pygame.K_q]:
            if player_data["p1_selected"] == False:
                player_data["p1_selected"] = True
                pygame.mixer.Sound.play(character_selected)
            else:
                player_data["p1_selected"] = False

        if key[pygame.K_p]:
            if player_data["p2_selected"] == False:
                player_data["p2_selected"] = True
                pygame.mixer.Sound.play(character_selected)
            else:
                player_data["p2_selected"] = False