import pygame
from yaml import load
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


class Tile(object):
    def __init__(self, tile_set, index):
        self.tile_set = tile_set
        self.index = index

    def draw(self, surface, pos):
        self.tile_set.blit_tile(surface, self.index, pos)


class TileSetManager(object):
    def __init__(self, spec_file):
        self.files = {}
        self.tiles = {}
        specs = load(open(spec_file, 'r'))
        for file in specs["files"]:
            self.files[file] = TileSet(file)
        for name, tile_def in specs["tiles"].iteritems():
            self.tiles[name] = Tile(self.files[tile_def["file"]], (tile_def["x"], tile_def["y"]))

    def get(self, name):
        return self.tiles[name]
