import logging

from domb.item.item import Item
import tiles


logger = logging.getLogger('console')


class Potion(Item):
    name = "Potion"
    tile = tiles.POTION

    def use(self, character):
        hp = character.hp.restore(5)
        logger.info("%s used %s: %d hp regenerated", character.name, self.name, hp)
        return True
