from random import choice, randint
from domb.directions import N, S, E, W
from vec2d import Vec2d
from entity import Entity
import domb.tiles as tiles
from domb.area import Spot
from domb.area import Area


class AreaGenerator(object):
    data = {}

    def build(self):
        # initial room
        space = self.create_space(Vec2d(10, 10), E, 3, 6)
        self.data.update(space)

        for i in range(20):
            self.sprout_space(randint(2, 6), randint(2, 6))

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
        self.data[apos] = "door"
        return True

    def valid_dir(self, pos):
        dirs = [dir for dir in [N, S, E, W] if (pos + dir) not in self.data]
        if len(dirs) == 0:
            return None
        else:
            return choice(dirs)

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


def generate_dungeon(tiles):
    b = AreaGenerator()
    b.build()
    return b.get_area()
