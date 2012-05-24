GROUND_TILE = (9, 31)

class GameMap(object):
    def __init__(self, data, tile_set):
        self._data = data
        self._tile_set = tile_set

    def draw(self, screen):
        for pos, tile in self._data.iteritems():
            self._tile_set.blit_tile(screen, tile, pos)

    def walkable(self, x, y):
        return (x, y) in self._data.keys()

def generate_map(tile_set):
    return GameMap(generate_square(10, GROUND_TILE), tile_set)

def generate_square(size, tile):
    square = {}
    for i in xrange(size):
      for j in xrange(size):
        square[(i,j)] = tile
    return square
