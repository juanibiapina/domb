from random import choice
from domb.directions import N, S, E, W
from vec2d import Vec2d
from entity import Entity
import domb.tiles as tiles
from domb.area import Spot
from domb.area import Area


class AreaGenerator(object):
    data = {}

    def build(self):
        self.create_initial_room()
        pos = self.random_wall()
        dir = self.valid_dir(pos)
        if dir:
            self.create_corridor(pos, dir, 5)

    def valid_dir(self, pos):
        dirs = [dir for dir in [N, S, E, W] if (pos + dir) not in self.data]
        if len(dirs) == 0:
            return None
        else:
            return choice(dirs)

    def random_wall(self):
        return choice([pos for pos, name in self.data.iteritems() if name == "wall"])

    def create_corridor(self, pos, dir, length):
        data = {}
        dir1, dir2 = self.cross(dir)
        for i in range(1, length + 1):
            data[pos + (i * dir)] = "floor"
            data[(pos + dir1) + (i * dir)] = "wall"
            data[(pos + dir2) + (i * dir)] = "wall"

        data[pos + ((length + 1) * dir)] = "wall"
        data[(pos + dir1) + ((length + 1) * dir)] = "wall"
        data[(pos + dir2) + ((length + 1) * dir)] = "wall"

        self.data.update(data)

        self.data[pos] = "door"

    def cross(self, dir):
        x = dir.x
        y = dir.y
        dir1 = (1 if x == 0 else 0, 1 if y == 0 else 0)
        dir2 = (-1 if x == 0 else 0, -1 if y == 0 else 0)
        return dir1, dir2

    def create_initial_room(self):
        self.create_room(10, 10)

    def create_room(self, width, height):
        for i in xrange(width):
            for j in xrange(height):
                coord = Vec2d(i, j)
                if i == 0 or i == (width - 1) or j == 0 or j == (height - 1):
                    self.data[coord] = "wall"
                else:
                    self.data[coord] = "floor"

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
