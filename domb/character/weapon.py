from domb.dice import Dice


class Weapon(object):
    damage_dice = Dice("1d2")
    name = "Unarmed"

    def get_damage(self):
        return self.damage_dice.roll()

    def get_name(self):
        return self.name
