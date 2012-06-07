import logging

from entity import Entity


logger = logging.getLogger('console')


class Item(Entity):
    name = "Item"
    tile = None

    def __init__(self):
        super(Item, self).__init__(self.tile, walkable=True)

    def get_name(self):
        return self.name

    def is_equipable(self):
        return self.equipable

    def use(self, character):
        logger.info("%s used %s... nothing happens", character.get_name(), self.name)
        return False
