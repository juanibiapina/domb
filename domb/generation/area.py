from random import choice, randint, random

from domb.directions import N, S, E, W
from vec2d import Vec2d
from entity import Entity
import domb.tiles as tiles
from domb.area import Spot
from domb.area import Area


class AreaGenerator(object):
    def __init__(self, parameters):
        self.parameters = parameters
        self.data = {}

    def build(self):
        p = self.parameters

        # initial room
        space = self.create_space(Vec2d(10, 10), E, p.initial_room_width, p.initial_room_height)
        self.data.update(space)

        # other rooms
        i = 0
        while i < p.number_of_rooms - 1:
            created = self.sprout_space(p.room_width, p.room_height)
            if p.force_number:
                if created:
                    i += 1
            else:
                i += 1

        return self.get_area()

    def sprout_space(self, width, height):
        pos, dir = self.random_wall()
        if dir:
            space = self.create_space(pos, dir, width, height)
            return self.merge_space(pos, space)
        else:
            return False

    def merge_space(self, apos, space):
        for pos, name in space.iteritems():
            if pos in self.data and self.data[pos] != "wall":
                return False
        self.data.update(space)
        if random() <= self.parameters.door_probability:
            self.data[apos] = "door"
        else:
            self.data[apos] = "floor"
        return True

    def valid_dir(self, pos):
        valid_dirs = []
        for dir in self.parameters.directions:
            if (pos + dir) not in self.data:  # direction has nothing
                dir1, dir2 = self.cross(dir)
                if (pos + dir1) in self.data and self.data[pos + dir1] == "wall":  # has wall on one side
                    if (pos + dir2) in self.data and self.data[pos + dir2] == "wall":  # has wall on the other side
                        if (pos - dir) not in self.data or self.data[pos - dir] != "wall":
                            valid_dirs.append(dir)

        if len(valid_dirs) == 0:
            return None
        else:
            return choice(valid_dirs)

    def random_wall(self):
        pos = choice([pos for pos, name in self.data.iteritems() if name == "wall"])
        dir = self.valid_dir(pos)
        return pos, dir

    def create_space(self, pos, dir, width, length):
        data = {}
        dir1, dir2 = self.cross(dir)

        # First wall
        data[pos] = "wall"
        for w in range(1, width + 2):
            data[(pos + (dir1 * w))] = "wall"
            data[(pos + (dir2 * w))] = "wall"

        # contents of room + border walls
        for i in range(1, length + 1):
            # border
            data[(pos + (dir1 * (width + 1))) + (i * dir)] = "wall"

            # floor
            data[pos + (i * dir)] = "floor"
            for w in range(1, width + 1):
                data[pos + (i * dir) + (dir1 * w)] = "floor"
                data[pos + (i * dir) + (dir2 * w)] = "floor"

            # other border
            data[(pos + (dir2 * (width + 1))) + (i * dir)] = "wall"

        # last wall
        data[pos + ((length + 1) * dir)] = "wall"
        for w in range(1,  width + 2):
            data[(pos + (dir1 * w)) + ((length + 1) * dir)] = "wall"
            data[(pos + (dir2 * w)) + ((length + 1) * dir)] = "wall"

        return data

    def cross(self, dir):
        x = dir.x
        y = dir.y
        dir1 = Vec2d(1 if x == 0 else 0, 1 if y == 0 else 0)
        dir2 = Vec2d(-1 if x == 0 else 0, -1 if y == 0 else 0)
        return dir1, dir2

    def get_area(self):
        result = {}
        for pos, name in self.data.iteritems():
            result[pos] = self.tile_for(name)
        return Area(result)

    def tile_for(self, name):
        if name == "floor":
            return Spot(Entity(tiles.GROUND, walkable=True))
        if name == "wall":
            return Spot(Entity(tiles.WALL, walkable=False))
        if name == "door":
            return Spot(Entity(tiles.DOOR, walkable=True))


class Parameters(object):
    initial_room_width = 0
    initial_room_height = 1
    door_probability = 1
    number_of_rooms = 1
    force_number = True
    room_width = 0
    room_height = 1
    directions = [N, S, E, W]


class Corridors(Parameters):
    initial_room_width = 0
    initial_room_height = 1
    door_probability = 0
    number_of_rooms = 100


class SquareRooms(Parameters):
    initial_room_width = 3
    initial_room_height = 7
    number_of_rooms = 5
    room_width = 3
    room_height = 7


class KindaRandom(Parameters):
    number_of_rooms = 10
    door_probability = 0.8

    @property
    def room_width(self):
        return randint(1, 3)

    @property
    def room_height(self):
        return randint(2, 6)


class Horizontal(Parameters):
    number_of_rooms = 10
    room_height = 3
    directions = [N]

    @property
    def room_width(self):
        return randint(3, 6)


def generate_dungeon(tiles):
    corridors = AreaGenerator(Corridors()).build()
    square_rooms = AreaGenerator(SquareRooms()).build()
    kinda_random = AreaGenerator(KindaRandom()).build()
    horizontal = AreaGenerator(Horizontal()).build()
    return kinda_random
