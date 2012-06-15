class Entity(object):
    tile = None
    walkable = True

    def __init__(self, tile=None):
        if tile:
            self.tile = tile

    def draw(self, screen, pos, camera):
        if self.tile:
            self.tile.draw(screen, pos, camera)

    def is_walkable(self):
        return self.walkable
