import pygame
import random
import time
pygame.font.init()

WIDTH = 600
HEIGHT = 700

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge This!")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

FONT = pygame.font.SysFont("comicsans",30)

ITEM_W, ITEM_H = 10, 10
ITEM_SPD = 5

def draw(player, elapsed_time, items):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f"{round(elapsed_time)}",1,"white")
    WIN.blit(time_text,(10, 10))

    pygame.draw.rect(WIN,"green",player)

    for item in items:
        pygame.draw.rect(WIN,"white",item)

    pygame.display.update()

player_spd = 5

def main():
    run = True
    hit = False
    player = pygame.Rect(200, HEIGHT - 70, 40, 60)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    item_add_increment = 2000
    item_count = 0

    items = []

    while run:
        item_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if item_count > item_add_increment:
            for _ in range(random.randint(3,7)):
                item_x = random.randint(10, WIDTH - ITEM_W)
                item = pygame.Rect(item_x, -ITEM_H, ITEM_W, ITEM_H)
                items.append(item)

            item_add_increment = max(200, item_add_increment - 50)
            item_count = 0

        # quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (player.x - player_spd >= 10):
            player.x -= player_spd
        if keys[pygame.K_RIGHT] and (player.x + player_spd + player.width <= WIDTH-10):
            player.x += player_spd

        for item in items[:]:
            item.y += ITEM_SPD
            if item.y > HEIGHT:
                items.remove(item)
            elif (item.y + item.height >= player.y) and (item.colliderect(player)):
                items.remove(item)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()  
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, items)
    pygame.quit()

if __name__ == "__main__":
    main()