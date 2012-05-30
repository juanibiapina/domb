from d20 import roll, resolve_attack


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

    def get_name(self):
        return self.name

    def draw(self, surface):
        self.tile.draw(surface, self.pos)
        if self.is_incapacitated():
            self.blood_tile.draw(surface, self.pos)

    def move(self, dx, dy):
        if not self.is_incapacitated():
            new_pos_x = self.pos[0] + dx
            new_pos_y = self.pos[1] + dy
            if (self.area.walkable(new_pos_x, new_pos_y)):
                self.pos = new_pos_x, new_pos_y

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
            target = self.area.get_character_at((self.pos[0] + direction[0], self.pos[1] + direction[1]))
            if target:
                resolve_attack(self, target)
