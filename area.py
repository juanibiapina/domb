from random import randint, choice

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
    def __init__(self, mapdata):
        self._data = mapdata
        self.characters = {}

    def get_random_position(self):
        return choice(self._data.keys())

    def draw(self, screen, tile_set):
        for pos, spot in self._data.iteritems():
            spot.draw(screen, tile_set, pos)
        for pos, character in self.characters.iteritems():
            character.draw(screen, tile_set)

    def walkable(self, x, y):
        if (x, y) in self._data:
            return (x, y) not in self.characters and self._data[(x, y)].is_walkable()
        else:
            return False

    def run_turn(self):
        for pos, character in self.characters.iteritems():
            character.run_turn()

    def add_character(self, character, pos):
        self.characters[pos] = character

    def remove_character(self, character):
        for pos, c in self.characters.iteritems():
            if c == character:
                self.characters.pop(pos)

    def update_character_position(self, old, new):
        print self.characters
        self.characters[new] = self.characters[old]
        self.characters.pop(old)


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
    # random rooms!
    builder.add_rectangle(2, 2, 4, 6, Entity(GROUND_TILE, walkable=True))
    builder.add_rectangle(8, 2, 6, 3, Entity(GROUND_TILE, walkable=True))
    builder.add_rectangle(7, 6, 12, 6, Entity(GROUND_TILE, walkable=True))

    # obstacles
    builder.add_obstacles()

    # random corridors
    builder.add_rectangle(6, 3, 2, 1, Entity(GROUND_TILE, walkable=True))
    builder.add_rectangle(10, 5, 1, 1, Entity(GROUND_TILE, walkable=True))

    return builder.get_dungeon()
