import pygame


class TileSet(object):
    TILE_SIZE = 32

    def __init__(self, file):
        self.tiles_image = pygame.image.load(file)

    def blit_tile(self, target_surface, tile_index, dest):
        x, y = map(lambda coord: coord * self.TILE_SIZE, tile_index)
        transformed_dest = dest * self.TILE_SIZE
        target_surface.blit(self.tiles_image, transformed_dest,
                            (x, y, self.TILE_SIZE, self.TILE_SIZE))

    def get_size(self):
        return self.tiles_image.get_size()

    def get_tile_size(self):
        return self.TILE_SIZE


class Tile(object):
    def __init__(self, x, y, tile_set):
        self.tile_set = tile_set
        self.index = (x, y)

    def draw(self, surface, pos, camera):
        self.tile_set.blit_tile(surface, self.index, camera.translate(pos, self.tile_set.TILE_SIZE))
