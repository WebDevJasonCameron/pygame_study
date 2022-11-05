import pygame
from sys import exit

pygame.init()

# SET
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# TXT
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# BG
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# SCORE
score_surf = test_font.render('My game', False, 'Black')
score_rect = score_surf.get_rect(center=(400, 50))


# Enemy
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))


# Player
player_surf = pygame.image.load(
    'graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))


# RUN
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))

    screen.blit(score_surf, score_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail_surf, (snail_rect))
    screen.blit(player_surf, (player_rect))

    # COLLIDE

    pygame.display.update()
    clock.tick(60)
