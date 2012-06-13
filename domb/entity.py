class Entity(object):
    def __init__(self, tile, **attributes):
        self.tile = tile
        self.attributes = attributes

    def draw(self, screen, pos, camera):
        self.tile.draw(screen, pos, camera)

    def get_attribute(self, attribute):
        return self.attributes.get(attribute, None)
