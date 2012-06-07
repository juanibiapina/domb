from domb.dice import Dice
from domb.entity import Entity


class Weapon(Entity):
    damage_dice = Dice("1d2")
    name = "Unarmed"
    tile = None

    def __init__(self):
        super(Weapon, self).__init__(self.tile, walkable=True)

    def get_damage(self):
        return self.damage_dice.roll()

    def get_name(self):
        return self.name
