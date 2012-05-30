from random import randint, choice


class Entity(object):
    def __init__(self, tile, **attributes):
        self.tile = tile
        self.attributes = attributes

    def draw(self, screen, pos):
        self.tile.draw(screen, pos)

    def get_attribute(self, attribute):
        return self.attributes.get(attribute, None)


class Spot(object):
    def __init__(self, *entities, **data):
        self.entities = list(entities)
        self.data = data

    def get_room_name(self):
        return self.data.get("room", None)

    def draw(self, screen, pos):
        for entity in self.entities:
            entity.draw(screen, pos)

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

    def draw(self, screen):
        for pos, spot in self._data.iteritems():
            spot.draw(screen, pos)
        for pos, character in self.characters.iteritems():
            character.draw(screen)

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

    def get_room_name(self, pos):
        if pos in self._data:
            return self._data[pos].get_room_name()
        else:
            return None

    def get_character_at(self, pos):
        return self.characters.get(pos, None)

    def update_character_position(self, old, new):
        self.characters[new] = self.characters[old]
        self.characters.pop(old)


class DungeonBuilder(object):
    def __init__(self):
        self.data = {}

    def add_rectangle(self, posx, posy, width, height, entity, **data):
        for i in xrange(width):
            for j in xrange(height):
                coord = (posx + i, posy + j)
                if coord in self.data:
                    self.data[coord].add_entity(entity)
                else:
                    self.data[coord] = Spot(entity, **data)

    def add_obstacles(self, entity):
        for spot in self.data.values():
            if randint(0, 10) < 1:
                spot.add_entity(entity)

    def get_dungeon(self):
        return Area(self.data)


def generate_dungeon(tiles):
    ground_tile = tiles["GROUND"]
    hole_tile = tiles["HOLE"]

    builder = DungeonBuilder()
    # random rooms!
    builder.add_rectangle(2, 2, 4, 6, Entity(ground_tile, walkable=True), room="room 1")
    builder.add_rectangle(8, 2, 6, 3, Entity(ground_tile, walkable=True), room="room 2")
    builder.add_rectangle(7, 6, 12, 6, Entity(ground_tile, walkable=True), room="room 3")

    # obstacles
    builder.add_obstacles(Entity(hole_tile))

    # random corridors
    builder.add_rectangle(6, 3, 2, 1, Entity(ground_tile, walkable=True))
    builder.add_rectangle(10, 5, 1, 1, Entity(ground_tile, walkable=True))

    return builder.get_dungeon()
