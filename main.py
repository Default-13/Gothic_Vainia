# Simple pygame program

# Import the pygame library
import pygame

# Import pygames.locals for convenience 
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Init pygame library
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# the size determind by the constant SCREEN_WIDTH and SCREEN HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Variable to keep the game running
running = True

# Main loop
while running:
    # Look at every event in the game
    for event in pygame.event.get():
        # Did the user hit the key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            # Did the user click the window close button?
        elif event.type == QUIT:
            running == False

# Fill the screen with white
screen.fill((255, 255, 255))

# Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50, 50))

# Give the surface a color to seperate from the background
surf.fill((0,0,0))
rect = surf.get_rect()

# This line says "Draw surf onto the screen at the center"
screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
pygame.display.flip()