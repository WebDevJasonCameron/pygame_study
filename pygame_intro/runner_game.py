import pygame
from sys import exit

pygame.init()

# SET
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# TXT
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# BAK
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

text_surf = test_font.render('My game', False, 'Black')

# Enemy
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

# Player
player_surf = pygame.image.load(
    'graphics/Player/player_walk_1.png').convert_alpha()


# RUN
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw all our elements
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    screen.blit(text_surf, (300, 50))

    snail_x_pos += -4
    if snail_x_pos < -100:
        snail_x_pos = 850

    screen.blit(snail_surf, (snail_x_pos, 250))

    # Update everything

    pygame.display.update()
    clock.tick(60)
