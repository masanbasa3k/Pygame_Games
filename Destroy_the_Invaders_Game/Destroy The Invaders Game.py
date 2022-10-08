#Advenced calculator
import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 750, 850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Light in the Space")
file_dir = 'C:/pythonProjectFile/assets/pngs'

def loadImage(spr):
    return pygame.image.load(os.path.join(f"{file_dir}/{spr}"))

##IMAGES
#Ships
Player_Ship = loadImage("spr_playerShip.png")   
Enemy_Ship1 = loadImage("spr_enemyShip1.png")
Enemy_Ship2 = loadImage("spr_enemyShip2.png")
Enemy_Ship3 = loadImage("spr_enemyShip3.png")

#Lazer
Lazer = loadImage("spr_lazer.png")

#Background
BG = pygame.transform.scale((loadImage("spr_background.png")), (WIDTH, HEIGHT))#scale the bg

class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.lazer_img = None
        self.lazers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.ship_img = Player_Ship
        self.lazer_img = Lazer
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_healt = health


def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player = Player(300, 650)
    player_vel = 5

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))


        player.draw(WIN)


        pygame.display.update()

    while run:
        clock.tick(FPS) 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: #Left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + 80 < WIDTH: #Right
            player.x += player_vel
        if keys[pygame.K_w] and player.y + player_vel > HEIGHT/2: #Right
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + 100 < HEIGHT: #Right
            player.y += player_vel

        redraw_window()
main()