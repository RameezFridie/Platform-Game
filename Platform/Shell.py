# Shell of a game like a tempelate
import pygame
import random
from Platform.settings import *

# Initialise pygame window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()

# Sprites Groups
all_sprites = pygame.sprite.Group()

running = True
# Game loop
while running:
    # Keep running at 30fps
    clock.tick(fps)
    # Process
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False

    # Updates
    all_sprites.update()
    # Render
    screen.fill(blue)
    all_sprites.draw(screen)
    # after drawing 
    pygame.display.flip()

pygame.quit()