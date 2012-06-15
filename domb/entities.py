from domb.entity import Entity
import domb.tiles as t


class Door(Entity):
    tile = t.DOOR
    walkable = True


class DungeonFloor(Entity):
    tile = t.FLOOR
    walkable = True


class Wall(Entity):
    tile = t.WALL
    walkable = False
