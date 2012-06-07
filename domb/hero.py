from character.character import Character
from character.size import Medium
from character.xp import XP
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
        self.xp = XP(self.hit_dice)

    def resolve_damage(self, damage):
        super(Hero, self).resolve_damage(damage)
        if self.is_incapacitated():
            raise HeroIsDead()

    def resolve_xp(self, target):
        if target.is_incapacitated():
            self.xp.increase(target.get_cr())

    def get_xp(self):
        return self.xp.xp
