from domb.item.weapon import Weapon
from domb.dice import Dice


class Claw(Weapon):
    name = "Claw"
    damage_dice = Dice("1d2")


class Bite(Weapon):
    name = "Bite"
    damage_dice = Dice("1d4")


class Unarmed(Weapon):
    name = "Unarmed Strike"
    damage_dice = Dice("1d3")
