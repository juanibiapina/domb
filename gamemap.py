import random

GROUND_TILE = (9, 31)
HOLE_TILE = (13, 32)


class GameMap(object):
    def __init__(self, data, obstacles, tile_set):
        self._data = data
        self._obstacles = obstacles
        self._tile_set = tile_set

    def draw(self, screen):
        for pos, tile in self._data.iteritems():
            self._tile_set.blit_tile(screen, tile, pos)
        for pos, tile in self._obstacles.iteritems():
            self._tile_set.blit_tile(screen, tile, pos)

    def walkable(self, x, y):
        return (x, y) in self._data.keys() and (x, y) not in self._obstacles.keys()


def generate_map(tile_set):
    return GameMap(generate_rectangle(15, 10, GROUND_TILE), generate_obstacles(15, 10), tile_set)


def generate_rectangle(width, height, tile):
    rect = {}
    for i in xrange(width):
        for j in xrange(height):
            rect[(i, j)] = tile
    return rect


def generate_obstacles(width, height):
    obstacles = {}
    for i in xrange(width):
        for j in xrange(height):
            if(random.randint(0, 10) < 2):
                obstacles[(i, j)] = HOLE_TILE
    return obstacles
