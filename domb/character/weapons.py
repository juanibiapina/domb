from domb.character.weapon import Weapon
from domb.dice import Dice
import domb.tiles as tiles


class Longsword(Weapon):
    name = "Longsword"
    damage_dice = Dice("1d8")
    tile = tiles.LONGSWORD
