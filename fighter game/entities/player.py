import pygame

class Player():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.rect = pygame.Rect((x, y, 80, 150))
        self.vel_y = 0
        self.jump = False
        self.double_jump = False
        self.attacking = False
        self.attack_type = 0
        self.face_foward = True


    def update_player(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

    def attack(self, target, player_data):
        self.attacking = True
        atttacking_rect = pygame.Rect((self.rect.centerx if self.face_foward else (self.rect.left - self.rect.width/2)), self.rect.y, self.rect.width, self.rect.height)
        
        if atttacking_rect.colliderect(target.rect):
            #print("player 1 hit player 2")
            player_data["p2_character"][1] -= 10
        pygame.draw.rect(self.screen, (0, 0, 255), atttacking_rect)

    def move(self, target, player_data):

        #print("move called")
        SPEED = 10
        DF = 2
        dx = 0
        dy = 0


        #get keypresses
        key = pygame.key.get_pressed()

        #is attacking
        if self.attacking == False:

            #movement keypresses
            if key[pygame.K_a]:
                self.face_foward = False
                dx = -SPEED
            if key[pygame.K_d]:
                self.face_foward = True
                dx = SPEED
            #jump
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            elif key[pygame.K_w] and self.jump == True and self.double_jump == False and self.rect.bottom < 300:
                self.vel_y = -20
                self.double_jump = True

            #apply DF
            self.vel_y += DF
            dy += self.vel_y

            #update player position
            if self.rect.left + dx <= 0:
                SPEED = 0
            elif self.rect.right + dx >= 1024:
                SPEED = 0
            else:
                self.rect.x += dx

            #y pos
            if self.rect.bottom + dy > 490:
                self.vel_y = 0
                dy = 490 - self.rect.bottom
                self.jump = False
                self.double_jump = False
            
            self.rect.y += dy

            #attacks
            if key[pygame.K_e]:
                self.attack_type = 1
                self.attack(target, player_data)
