import os
import pygame

class Map:
    def __init__(self, game, map_filename):
        self.game = game
        self.data = []
        self.map_filename = map_filename
        self.tile_size = 32
        self.tileset_images = {}
        self.default_tile_image = pygame.Surface((self.tile_size, self.tile_size))
        self.default_tile_image.fill((255, 0, 255))  # Couleur magenta pour indiquer une tuile manquante

    def load_map(self):
        with open(self.map_filename, "r") as file:
            self.data = [ [int(val) for val in line.strip().split(',')] for line in file if line.strip() ]

        tile_numbers = set()
        for row in self.data:
            for tile in row:
                if tile >= 0:
                    tile_numbers.add(tile)

        print("Numéros de tuiles uniques dans la carte :", tile_numbers)

        self.tileset_images = {}
        for tile_num in tile_numbers:
            image_tile_num = tile_num + 1
            image_path = f"./assets/tileset/Tile_{image_tile_num}.png"
            if os.path.isfile(image_path):
                try:
                    image = pygame.image.load(image_path).convert_alpha()
                    image = pygame.transform.scale(image, (self.tile_size, self.tile_size))
                    self.tileset_images[tile_num] = image
                except pygame.error as e:
                    print(f"Erreur lors du chargement de l'image pour la tuile {tile_num}: {e}")
                    self.tileset_images[tile_num] = self.default_tile_image
            else:
                print(f"Avertissement : Image de tuile non trouvée pour l'ID {tile_num} au chemin {image_path}")
                self.tileset_images[tile_num] = self.default_tile_image

    def draw_map(self):
        for row_index, row in enumerate(self.data):
            for col_index, tile in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                if tile >= 0:
                    tile_image = self.tileset_images.get(tile, self.default_tile_image)
                    self.game.display.blit(tile_image, (x, y))
