# Import libraries
import pygame, sys
from settings import *
from world import World

# Init pygame library
pygame.init()

# Create the screen object
# the size determind by the constant WIDTH andHEIGHT
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Gothic_Vainia")

# Gothic_Vainia class uses __init__() method initializes
# various attributes and loads then scales background image 
# from a given file path 
class Gothic_Vainia:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.player_event = False
        self.bg_img = pygame.image.load('assets/gothicvania-cemetery-files/PNG/Environment/background.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (width, height))
# the main() method is where the game loop is located. this
# creates and instance called World as a class and passes
# the world_map and screen as parameters. This will run 
# indefinitely until the game is closed.
    def main(self):
        world =World(world_map, self.screen)
        while True:
            self.screen.blit(self.bg_img, (0,0))
            for event in pygame.event():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_LEFT:
                        self.player_event == "left"
                    if event.key ==pygame.K_RIGHT:
                        self.player_event == "right"
                    if event.key ==pygame.K_SPACE:
                        self.player_event == "space"
                elif event.type == pygame.KEYUP:
                    self.player_event = False
                
            world.update(self.player_event)
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    play = Gothic_Vainia(screen, WIDTH, HEIGHT)
    play.main()

                    