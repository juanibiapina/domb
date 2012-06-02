from d20 import roll, resolve_attack
from inventory import Inventory
import logging

logger = logging.getLogger('console')


class Character(object):
    hit_dice = None
    blood_tile = None
    tile = None
    ai = None
    hp = 1
    name = "Monster"

    def __init__(self, area):
        if self.hit_dice:
            self.hp = self.hit_dice.roll()
        self.area = area
        self.pos = area.get_random_position()
        self.area.add_character(self)
        self.inventory = Inventory()

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
        return roll(3)  # unarmed strike

    def calculate_attack(self):
        return roll(20)  # base attack, no modifiers

    def calculate_ac(self):
        return 10  # base ac, no modifiers

    def is_incapacitated(self):
        return self.hp <= 0

    def damage(self, damage):
        self.hp -= damage

    def attack_pos(self, pos):
        if not self.is_incapacitated():
            target = self.area.get_character_at(pos)
            if target:
                resolve_attack(self, target)

    def attack(self, direction):
        if not self.is_incapacitated():
            target = self.area.get_character_at(self.pos + direction)
            if target:
                resolve_attack(self, target)

    def pick_up_item(self):
        item = self.area.pick_up_item(self.pos)
        if item:
            logger.info(self.get_name() + " picked up a " + item)
            self.inventory.add_item(item)

    def get_items(self):
        return self.inventory
