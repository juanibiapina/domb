import logging

from domb.d20 import resolve_attack
from domb.inventory import Inventory

from domb.character.attribute import Attribute
from domb.character.hp import HP
from domb.character.ac import AC
from domb.character.attack import Attack
from domb.character.damage import Damage
from domb.character.size import Medium
from domb.character.type import Type

from domb.item.naturalweapons import Unarmed


logger = logging.getLogger('console')


class Character(object):
    hit_dice = 1
    blood_tile = None
    tile = None
    ai = None
    hp = None
    ac = None
    cr = None
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
    weapon = Unarmed()

    def __init__(self, area):
        self.area = area
        self.pos = area.get_random_position()
        self.area.add_character(self)
        self.inventory = Inventory()
        self.set_attributes(self.attributes)
        self.hp = HP(self)
        self.ac = AC(self)
        self.attack = Attack(self)
        self.damage = Damage(self)

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

    def get_attack(self):
        return self.attack

    def get_ac(self):
        return self.ac

    def get_cr(self):
        return self.cr

    def get_damage(self):
        return self.damage

    def get_weapon(self):
        return self.weapon

    def get_hp(self):
        return self.hp

    def is_incapacitated(self):
        return self.hp.current_value <= 0

    def resolve_damage(self, damage):
        self.hp.damage(damage)

    def do_attack_pos(self, pos):
        if not self.is_incapacitated():
            target = self.area.get_character_at(pos)
            if target:
                resolve_attack(self, target)
                self.resolve_xp(target)

    def do_attack(self, direction):
        self.do_attack_pos(self.pos + direction)

    def pick_up_item(self):
        item = self.area.pick_up_item(self.pos)
        if item:
            logger.info(self.get_name() + " picked up a " + item.get_name())
            self.inventory.add_item(item)

    def get_items(self):
        return self.inventory

    def has_feat(self, feat):
        return feat in self.feats

    def use_current_item(self):
        item = self.inventory.current_item()
        if item.use(self):
            self.inventory.remove_current()

    def resolve_xp(self, target):
        pass
