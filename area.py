from random import randint

GROUND_TILE = (9, 31)
HOLE_TILE = (13, 32)


class Entity(object):
    def __init__(self, tile_index, **attributes):
        self.tile_index = tile_index
        self.attributes = attributes

    def draw(self, screen, tile_set, pos):
        tile_set.blit_tile(screen, self.tile_index, pos)

    def get_attribute(self, attribute):
        return self.attributes.get(attribute, None)


class Spot(object):
    def __init__(self, *entities):
        self.entities = list(entities)

    def draw(self, screen, tile_set, pos):
        for entity in self.entities:
            entity.draw(screen, tile_set, pos)

    def add_entity(self, entity):
        self.entities.append(entity)

    def is_walkable(self):
        return reduce(lambda a, b: a and b, [entity.get_attribute('walkable') for entity in self.entities])


class Area(object):
    def __init__(self, data):
        self._data = data

    def draw(self, screen, tile_set):
        for pos, spot in self._data.iteritems():
            spot.draw(screen, tile_set, pos)

    def walkable(self, x, y):
        if (x, y) in self._data:
            return self._data[(x, y)].is_walkable()
        else:
            return False


class DungeonBuilder(object):
    def __init__(self):
        self.data = {}

    def add_rectangle(self, posx, posy, width, height, entity):
        for i in xrange(width):
            for j in xrange(height):
                coord = (posx + i, posy + j)
                if coord in self.data:
                    self.data[coord].add_entity(entity)
                else:
                    self.data[coord] = Spot(entity)

    def add_obstacles(self):
        for spot in self.data.values():
            if randint(0, 10) < 1:
                spot.add_entity(Entity(HOLE_TILE))

    def get_dungeon(self):
        return Area(self.data)


def generate_dungeon():
    builder = DungeonBuilder()
    builder.add_rectangle(0, 0, 20, 15, Entity(GROUND_TILE, walkable=True))
    builder.add_obstacles()
    return builder.get_dungeon()
