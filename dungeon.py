import random

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


class Dungeon(object):
    def __init__(self, data, tile_set):
        self._data = data
        self._tile_set = tile_set

    def draw(self, screen):
        for pos, spot in self._data.iteritems():
            spot.draw(screen, self._tile_set, pos)

    def walkable(self, x, y):
        if (x, y) in self._data:
            return self._data[(x, y)].is_walkable()
        else:
            return False


def generate_dungeon(tile_set):
    world_data = generate_rectangle(20, 15, GROUND_TILE)
    obstacles = generate_obstacles(20, 15)
    for tile_index, obstacle in obstacles.items():
        world_data[tile_index].add_entity(obstacle)
    return Dungeon(world_data, tile_set)


def generate_rectangle(width, height, tile):
    rect = {}
    for i in xrange(width):
        for j in xrange(height):
            rect[(i, j)] = Spot(Entity(tile, walkable=True))
    return rect


def generate_obstacles(width, height):
    obstacles = {}
    for i in xrange(width):
        for j in xrange(height):
            if(random.randint(0, 10) < 1):
                obstacles[(i, j)] = Entity(HOLE_TILE)
    return obstacles
