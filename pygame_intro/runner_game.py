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
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')

text_surface = test_font.render('My game', False, 'Black')

# Enemy
snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600


# RUN
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw all our elements
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_x_pos += -4
    if snail_x_pos < -100:
        snail_x_pos = 850

    screen.blit(snail_surface, (snail_x_pos, 250))

    # Update everything

    pygame.display.update()
    clock.tick(60)
