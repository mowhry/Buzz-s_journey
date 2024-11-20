import pygame
from pygame.locals import *

class Map:
    def __init__(self, game, map_filename):
        self.game = game
        self.data = []
        self.map_filename = map_filename
        self.tile_size = 48
        self.tileset_images = {
            "1": pygame.transform.scale(pygame.image.load("./assets/tileset/Tile_02.png").convert_alpha(), (self.tile_size, self.tile_size)),
            "2": pygame.transform.scale(pygame.image.load("./assets/tileset/Tile_08.png").convert_alpha(), (self.tile_size, self.tile_size)),
        }

    def load_map(self):
        with open(self.map_filename, "r") as file:
            self.data = [list(line.strip()) for line in file]

    def draw_map(self):
        for row_index, row in enumerate(self.data):
            for col_index, tile in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                if tile in self.tileset_images:
                    self.game.display.blit(self.tileset_images[tile], (x, y))

