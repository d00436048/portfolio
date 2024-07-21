import pygame

pygame.init()

bg_image = pygame.image.load("assets/images/backgrounds/testBG1.png").convert_alpha()

def load_test_level(screen, player_data):
    #print("load_test_level_called")

    #load background
    load_bg(screen)
    

#helper functions
def load_bg(screen):
    scaled_bg = pygame.transform.scale(bg_image, (1024, 600))
    screen.blit(scaled_bg, (0,0))

# def load_foreground(screen):

