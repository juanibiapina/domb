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
        return (x, y) in self._data.keys()

def generate_map(tile_set):
    return GameMap(generate_square(10, GROUND_TILE), generate_obstacles(10), tile_set)

def generate_square(size, tile):
    square = {}
    for i in xrange(size):
      for j in xrange(size):
        square[(i,j)] = tile
    return square

def generate_obstacles(size):
    obstacles = {}
    for i in xrange(size):
        for j in xrange(size):
            if(random.randint(0,10) < 3):
                obstacles[(i,j)] = HOLE_TILE

    return obstacles 

