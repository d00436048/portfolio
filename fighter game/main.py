import pygame
from pygame.locals import *

from scenes import intro
from scenes import title
from scenes import level_selection
from scenes import player_selection
from scenes import results
from scenes import stats
from scenes import cheat_codes

import characters


#constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("caption")
pygame.mixer.init()

#safety imports
from scenes import game
from entities import player
from entities import player2

#initial scene and scenes
sTally = 0
scenes = ["intro", "title", "player_select", "level_select", "game", "results", "stats", "cheat_codes"]
current_scene = scenes[sTally]
player_select_music = pygame.mixer.Sound("assets/music/player_select.mp3")
scene = pygame.mixer.Sound("assets/music/scene.mp3")
#intro data
fontIncrement = 40
fontIncrementBool = False
intro_completed = False

#main menu data
marker_w = 0
marker_s = 0
marker = 0

glove = 420
glove2 = 370
gloveBool = False
gloveBool2 = False

#player select, level select and game data
game_stats = {
    "times_won": [0,0,0,0,0,0,0]
}
 
player_data = {
    "p1_tally" : 0,
    "p2_tally" : 1,
    "P1_character": None,
    "P2_character": None,
    "result" : None,

    #level select
    "level": None,
    "level_tally": 0,     
    "level_tally_d" : 0,
    "level_tally_a" : 0,
    "level_selected" : False,   

    #player_select
    "p1_tally_d" : 0,
    "p1_tally_a" : 0,    
    "p2_tally_j" : 0,
    "p2_tally_l" : 0,
    "p1_selected": False,
    "p2_selected": False,
    "font_increment": 64,
    "font_increment_bool" : False,

    #unlockables
    "escalante_unlocked" : False,
    "quick_quack_unlocked" : False,
    "Bridger_unlocked" : False,
    "Missionary_Boyfriend_unlocked" : False
}

player1 = player.Player(screen, 200, 300)
player2 = player2.Player(screen, 800, 300)

#game loop
running = True
clock = pygame.time.Clock()
FPS = 60

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:

            # handling scene changes
            if event.key == K_SPACE:
                intro_completed = True
                # print(current_scene)
                if sTally == 0:
                    sTally = 1
                    current_scene = scenes[sTally]
                elif sTally == 1:
                    if marker == 0:
                        sTally = 2
                    elif marker == 1:
                        sTally = 6
                    elif marker == 2:
                        sTally = 7
                    current_scene = scenes[sTally]
                elif sTally == 2:
                    if player_data["p1_selected"] == True and player_data["p2_selected"] == True:
                        sTally = 3
                    current_scene = scenes[sTally]
                elif sTally == 3:
                    if player_data["level_selected"] == True:
                        sTally = 4
                        current_scene = scenes[sTally]
                        player_data["level_selected"] = False
                elif sTally == 4:
                    sTally = 5
                    current_scene = scenes[sTally]
                elif sTally == 5 and intro_completed == True:
                    sTally = 1
                    current_scene = scenes[sTally]
                elif sTally == 6:
                    sTally = 1
                    current_scene = scenes[sTally]
                elif sTally == 7:
                    sTally = 1
                    current_scene = scenes[sTally]
                else:
                    sTally = 0
                    current_scene = scenes[sTally]
                    
                pygame.mixer.Sound.play(scene)


            #for level selection testing

            if current_scene == "level_select":
                if event.key == K_q:
                    player_data["level"] = "test_level"
                    # print("test level 1 selected")
                if event.key == K_p:
                    player_data["level"] = "test_level2"
                    # print("test level 2 selected")

    screen.fill((0,0,0))

    #scenes
    if current_scene == "intro":
        if fontIncrement < 40 and fontIncrementBool == True:
            fontIncrement += 1
        elif fontIncrement > 20 and fontIncrementBool == False:
            fontIncrement -= 1
        elif fontIncrement >= 20 and fontIncrementBool == True:
            fontIncrementBool = False
        elif fontIncrement <= 40 and fontIncrementBool == False:
            fontIncrementBool = True
        I = intro.Intro(screen, fontIncrement)
        I.load_assets()
        
    if current_scene == "title":
        if glove < 430 and gloveBool == True:
            glove += 1
        elif glove > 420 and gloveBool == False:
            glove -= 1
        elif glove >= 420 and gloveBool == True:
            gloveBool = False
        elif glove <= 430 and gloveBool == False:
            gloveBool = True
        if glove2 < 380 and gloveBool2 == True:
            glove2 += 1
        elif glove2 > 370 and gloveBool2 == False:
            glove2 -= 1
        elif glove2 >= 370 and gloveBool2 == True:
            gloveBool2 = False
        elif glove2 <= 380 and gloveBool2 == False:
            gloveBool2 = True
        T = title.Title(screen)
        T.load_assets(marker, marker_w, marker_s, glove, glove2)
        marker = T.keyboard_inputs(marker, marker_w, marker_s)[0]
        marker_w = T.keyboard_inputs(marker, marker_w, marker_s)[1]
        marker_s = T.keyboard_inputs(marker, marker_w, marker_s)[2]

    if current_scene == "player_select":
        if player_data["font_increment"] < 80 and player_data["font_increment_bool"] == True:
            player_data["font_increment"] += 1
        elif player_data["font_increment"] > 50 and player_data["font_increment_bool"] == False:
            player_data["font_increment"] -= 1
        elif player_data["font_increment"] >= 80 and player_data["font_increment_bool"] == True:
            player_data["font_increment_bool"] = False
        elif player_data["font_increment"] <= 50 and player_data["font_increment_bool"] == False:
            player_data["font_increment_bool"] = True
        PS = player_selection.PlayerSelect(player_data, game_stats, screen)
        PS.show_character_choices(player_data)
        PS.character_selection(player_data)
 
    if current_scene == "level_select":
        LS = level_selection.LevelSelect(player_data, game_stats, screen)
        LS.load_level_selection(player_data)
        LS.level_selection(player_data)
        player_data["p1_selected"] = False
        player_data["p2_selected"] = False

    if current_scene == "game": 
        #load game
        current_game = game.Game(player_data, screen)
        current_game.load_level()
 
        #game loop
        player1.move(player2, player_data)
        player1.update_player()
        player2.move(player1, player_data)
        player2.update_player()     

        
        #load ui
        current_game.load_ui()
    if current_scene == "stats":
        s = stats.Stats(screen)
        s.load_assets()
    if current_scene == "cheat_codes":
        c = cheat_codes.Cheat_Codes(screen)
        c.load_assets()
    if current_scene == "results":
        if player_data["font_increment"] < 80 and player_data["font_increment_bool"] == True:
            player_data["font_increment"] += 1
        elif player_data["font_increment"] > 50 and player_data["font_increment_bool"] == False:
            player_data["font_increment"] -= 1
        elif player_data["font_increment"] >= 80 and player_data["font_increment_bool"] == True:
            player_data["font_increment_bool"] = False
        elif player_data["font_increment"] <= 50 and player_data["font_increment_bool"] == False:
            player_data["font_increment_bool"] = True
        r = results.Results(screen, player_data)
        r.load_assets()


    pygame.display.flip()   