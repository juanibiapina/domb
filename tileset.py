import pygame
from pygame.rect import Rect


class TileSet(object):
    TILE_SIZE = 32

    def __init__(self, file):
        self.tiles_image = pygame.image.load(file)

    def blit_tile(self, target_surface, tile_index, dest):
        x, y = map(lambda coord: coord * self.TILE_SIZE, tile_index)
        transformed_dest = map(lambda coord: coord * self.TILE_SIZE, dest)
        target_surface.blit(self.tiles_image, transformed_dest,
                            Rect(x, y, self.TILE_SIZE, self.TILE_SIZE))
