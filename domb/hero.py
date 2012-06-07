from character.character import Character
from character.size import Medium
from domb.character.type import Fighter
import tiles

blood_tile = tiles.BLOOD


class HeroIsDead(Exception):
    pass


class Hero(Character):
    name = "The Dude"
    hit_dice = 1
    type = Fighter()
    attributes = "Str 15, Dex 13, Con 15, Int 10, Wis 12, Cha 12"
    size = Medium()
    tile = tiles.FIGHTER
    blood_tile = blood_tile

    def __init__(self, area):
        super(Hero, self).__init__(area)
        self.xp = 0

    def add_xp(self, extra_xp):
        self.xp += extra_xp

    def resolve_damage(self, damage):
        super(Hero, self).resolve_damage(damage)
        if self.is_incapacitated():
            raise HeroIsDead()
