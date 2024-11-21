import pygame
from pygame.locals import *
from map import Map


class Level():
    def __init__(self, game, map_filename):
        self.game = game
        self.map = Map(self.game, map_filename)
        self.map.load_map()

    def update(self):
        pass

    def draw(self):
        self.map.draw_map()

class Level0(Level):
    def __init__(self, game):
        self.startx, self.starty = 100, 496
        super().__init__(game, "./assets/map_level/map0.csv")

    def update(self):
        super().update()

    def draw(self):
        super().draw()
