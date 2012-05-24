import random

GROUND_TILE = (9, 31)
HOLE_TILE = (13, 32)


class Spot(object):
    def __init__(self, tile_index):
        self.tile_index = tile_index

    def draw(self, screen, tileset, pos):
        tileset.blit_tile(screen, self.tile_index, pos)


class World(object):
    def __init__(self, data, obstacles, tile_set):
        self._data = data
        self._obstacles = obstacles
        self._tile_set = tile_set

    def draw(self, screen):
        for pos, spot in self._data.iteritems():
            spot.draw(screen, self._tile_set, pos)
        for pos, spot in self._obstacles.iteritems():
            spot.draw(screen, self._tile_set, pos)

    def walkable(self, x, y):
        return (x, y) in self._data.keys() and (x, y) not in self._obstacles.keys()


def generate_world(tile_set):
    return World(generate_rectangle(20, 15, GROUND_TILE), generate_obstacles(20, 15), tile_set)


def generate_rectangle(width, height, tile):
    rect = {}
    for i in xrange(width):
        for j in xrange(height):
            rect[(i, j)] = Spot(tile)
    return rect


def generate_obstacles(width, height):
    obstacles = {}
    for i in xrange(width):
        for j in xrange(height):
            if(random.randint(0, 10) < 2):
                obstacles[(i, j)] = Spot(HOLE_TILE)
    return obstacles
