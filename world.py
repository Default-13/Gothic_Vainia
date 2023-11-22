import pygame
from settings import tile_size, WIDTH
from tile import Tile
from trap import Trap
from goal import Goal
from player import Player
from game import Game

class World:
    def __init__(self, world_data, screen):
        self.screen = screen
        self.world_data = world_data
        self.setup_world(world_data)
        self.world_shift = 0
        self.current_x = 0
        self.gravity = 0.7
        self.game = Game(self.screen)
