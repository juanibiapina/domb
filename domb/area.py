from random import random, choice
from vec2d import Vec2d
from entity import Entity


class Spot(object):
    def __init__(self, *entities, **data):
        self.entities = list(entities)
        self.data = data
        self.item = None

    def get_room_name(self):
        return self.data.get("room", None)

    def draw(self, screen, pos, camera):
        for entity in self.entities:
            entity.draw(screen, pos, camera)
        if self.item:
            self.item.draw(screen, pos, camera)

    def add_entity(self, entity):
        self.entities.append(entity)

    def is_walkable(self):
        return reduce(lambda a, b: a and b, [entity.get_attribute('walkable') for entity in self.entities])

    def add_item(self, item):
        self.item = item

    def pick_up_item(self):
        item = self.item
        self.item = None
        return item


class Area(object):
    def __init__(self, mapdata):
        self._data = mapdata
        self.characters = []

    def get_random_position(self):
        return Vec2d(choice([pos for pos, spot in self._data.iteritems() if spot.is_walkable()]))

    def get_position_in_room(self, name):
        return Vec2d(choice([pos for pos, spot in self._data.iteritems() if spot.is_walkable() and spot.get_room_name() == name]))

    def draw(self, screen, camera):
        for pos, spot in self._data.iteritems():
            spot.draw(screen, pos, camera)
        for character in self.characters:
            character.draw(screen, camera)

    def walkable(self, pos):
        alive_characters = (ch.pos for ch in self.characters if not ch.is_incapacitated())
        if pos in self._data:
            return pos not in alive_characters and self._data[pos].is_walkable()
        else:
            return False

    def run_turn(self):
        for character in self.characters:
            character.run_turn()

    def add_character(self, character):
        self.characters.append(character)

    def get_room_name(self, pos):
        if pos in self._data:
            return self._data[pos].get_room_name()
        else:
            return None

    def get_character_at(self, pos):
        for character in self.characters:
            if character.pos == pos:
                return character

    def add_item(self, item, pos):
        if pos in self._data:
            self._data[pos].add_item(item)

    def pick_up_item(self, pos):
        if pos in self._data:
            return self._data[pos].pick_up_item()
        else:
            return None


class DungeonBuilder(object):
    def __init__(self):
        self.data = {}

    def add_rectangle(self, posx, posy, width, height, entity, **data):
        for i in xrange(width):
            for j in xrange(height):
                coord = Vec2d(posx + i, posy + j)
                if coord in self.data:
                    self.data[coord].add_entity(entity)
                else:
                    self.data[coord] = Spot(entity, **data)

    def add_obstacles(self, entity, density):
        for spot in self.data.values():
            if random() < density:
                spot.add_entity(entity)

    def get_dungeon(self):
        return Area(self.data)


def generate_dungeon(tiles):
    ground_tile = tiles.GROUND
    hole_tile = tiles.HOLE

    builder = DungeonBuilder()
    # random rooms!
    builder.add_rectangle(2, 2, 4, 6, Entity(ground_tile, walkable=True), room="room 1")
    builder.add_rectangle(8, 2, 6, 3, Entity(ground_tile, walkable=True), room="room 2")
    builder.add_rectangle(7, 6, 12, 6, Entity(ground_tile, walkable=True), room="room 3")

    # obstacles
    builder.add_obstacles(Entity(hole_tile), 0.05)

    # random corridors
    builder.add_rectangle(6, 3, 2, 1, Entity(ground_tile, walkable=True))
    builder.add_rectangle(10, 5, 1, 1, Entity(ground_tile, walkable=True))

    return builder.get_dungeon()
