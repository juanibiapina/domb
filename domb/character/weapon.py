import logging

from domb.dice import Dice
from domb.item import Item


logger = logging.getLogger('console')


class Weapon(Item):
    damage_dice = Dice("1d2")
    name = "Unarmed"
    tile = None

    def get_damage(self):
        return self.damage_dice.roll()

    def use(self, character):
        character.weapon = self
        logger.info("%s equiped %s", character.get_name(), self.name)
        return False
