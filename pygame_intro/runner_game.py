import pygame
from sys import exit

# ___CREATE SCORE


def display_score():
    current_time = pygame.time.get_ticks()
    print(current_time)


# ___CREATE GAME


pygame.init()

# SET
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
box_color = '#c0e8ec'
game_active = True

# TXT
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_color = (64, 64, 64)

# BG
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# SCORE
# score_surf = text_font.render('My game', False, text_color)
# score_rect = score_surf.get_rect(center=(400, 50))


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
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.bottom >= 300:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if player_rect.bottom >= 300:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    if game_active:
        # bg
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))

        # bg score
        # pygame.draw.rect(screen, box_color, score_rect)
        # pygame.draw.rect(screen, box_color, score_rect, 10)
        # screen.blit(score_surf, score_rect)
        display_score()

        # snail
        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800

        screen.blit(snail_surf, (snail_rect))

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, (player_rect))

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Red')

    # run
    pygame.display.update()
    clock.tick(60)
