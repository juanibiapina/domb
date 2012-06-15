from domb.entity import Entity
import domb.tiles as t


class Door(Entity):
    tile = t.DOOR
    walkable = False

    def __init__(self, closed=True):
        self.closed = closed

    def open(self):
        self.closed = False
        self.walkable = True

    def draw(self, screen, pos, camera):
        if self.closed:
            super(Door, self).draw(screen, pos, camera)


class DungeonFloor(Entity):
    tile = t.FLOOR
    walkable = True


class Wall(Entity):
    tile = t.WALL
    walkable = False
