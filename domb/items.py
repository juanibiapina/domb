import logging

from domb.item import Item
import tiles


logger = logging.getLogger('console')


class Potion(Item):
    name = "Potion"
    tile = tiles.POTION

    def use(self, character):
        hp = character.get_hp().restore(5)
        logger.info("%s used %s: %d hp regenerated", character.get_name(), self.name, hp)
        return True
