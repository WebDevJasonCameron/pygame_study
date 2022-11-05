import pygame
from sys import exit

pygame.init()

# SET
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
box_color = '#c0e8ec'

# TXT
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_color = (64, 64, 64)

# BG
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# SCORE
score_surf = text_font.render('My game', False, text_color)
score_rect = score_surf.get_rect(center=(400, 50))


# Enemy
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))


# Player
player_surf = pygame.image.load(
    'graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

# Physics
player_gravity = 0


# RUN
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')
        if event.type == pygame.KEYUP:
            print('key up')

    # bg
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))

    # bg score
    pygame.draw.rect(screen, box_color, score_rect)
    pygame.draw.rect(screen, box_color, score_rect, 10)
    screen.blit(score_surf, score_rect)

    # snail
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail_surf, (snail_rect))

    # player
    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surf, (player_rect))

    # run
    pygame.display.update()
    clock.tick(60)
