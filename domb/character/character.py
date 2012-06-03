import logging

from domb.d20 import resolve_attack
from domb.inventory import Inventory
from domb.character.attribute import Attribute
from domb.character.hp import HP
from domb.character.ac import AC
from domb.character.attack import Attack
from domb.character.size import Medium
from domb.character.type import Type
from domb.dice import roll


logger = logging.getLogger('console')


class Character(object):
    hit_dice = 1
    blood_tile = None
    tile = None
    ai = None
    hp = None
    ac = None
    name = "Monster"
    attributes = "Str 10, Dex 10, Con 10, Int 10, Wis 10, Cha 10"
    str = Attribute(10)
    dex = Attribute(10)
    con = Attribute(10)
    int = Attribute(10)
    wis = Attribute(10)
    cha = Attribute(10)
    natural_armor = 0
    size = Medium()
    type = Type()
    feats = []

    def __init__(self, area):
        self.area = area
        self.pos = area.get_random_position()
        self.area.add_character(self)
        self.inventory = Inventory()
        self.set_attributes(self.attributes)
        self.hp = HP(self)
        self.ac = AC(self)
        self.attack = Attack(self)

    def set_attributes(self, attributes):
        broken_attrs = attributes.split(",")
        attrs = {}
        for attr in broken_attrs:
            name = attr.strip().split(" ")[0].lower()
            value = Attribute(int(attr.strip().split(" ")[1]))
            attrs[name] = value
        self.str = attrs["str"]
        self.dex = attrs["dex"]
        self.con = attrs["con"]
        self.int = attrs["int"]
        self.wis = attrs["wis"]
        self.cha = attrs["cha"]

    def get_name(self):
        return self.name

    def draw(self, surface):
        self.tile.draw(surface, self.pos)
        if self.is_incapacitated():
            self.blood_tile.draw(surface, self.pos)

    def move(self, delta):
        if not self.is_incapacitated():
            new_pos = self.pos + delta
            if (self.area.walkable(new_pos)):
                self.pos = new_pos

    def set_ai(self, ai):
        self.ai = ai

    def get_room(self):
        return self.area.get_room_name(self.pos)

    def run_turn(self):
        if not self.is_incapacitated():
            if self.ai:
                self.ai.update(self)

    def calculate_damage(self):
        return roll(1, 3, 0)  # unarmed strike

    def get_attack(self):
        return self.attack

    def get_ac(self):
        return self.ac

    def is_incapacitated(self):
        return self.hp.current_value <= 0

    def damage(self, damage):
        self.hp.damage(damage)

    def do_attack_pos(self, pos):
        if not self.is_incapacitated():
            target = self.area.get_character_at(pos)
            if target:
                resolve_attack(self, target)

    def do_attack(self, direction):
        if not self.is_incapacitated():
            target = self.area.get_character_at(self.pos + direction)
            if target:
                resolve_attack(self, target)

    def pick_up_item(self):
        item = self.area.pick_up_item(self.pos)
        if item:
            logger.info(self.get_name() + " picked up a " + item.get_name())
            self.inventory.add_item(item)

    def get_items(self):
        return self.inventory

    def has_feat(self, feat):
        return feat in self.feats
