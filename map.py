GROUND_TILE = (9, 31)

class Map(object):
    def __init__(self, data, tile_set):
        self._data = data
        self._tile_set = tile_set

    def draw(self, screen):
        for pos, tile in self._data.iteritems():
            self._tile_set.blit_tile(screen, tile, pos)

def generate_map(tile_set):
  return Map(dict(((i, 0), GROUND_TILE) for i in range(10)), tile_set)
