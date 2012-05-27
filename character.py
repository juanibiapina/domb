from d20 import roll, resolve_attack
from tileset import TileSet

BLOOD_TILE_INDEX = (1, 1)


class Character(object):
    def __init__(self, tile_index, area):
        self.tile_index = tile_index
        self.area = area
        self.pos = area.get_random_position()
        self.area.add_character(self, self.pos)
        self.ai = None
        self.hp = 2  # cat hp
        self.blood_tile_set = TileSet("blood.png")

    def draw(self, surface, tile_set):
        tile_set.blit_tile(surface, self.tile_index, self.pos)
        if self.is_incapacitated():
            self.blood_tile_set.blit_tile(surface, BLOOD_TILE_INDEX, self.pos)
            pass

    def move(self, dx, dy):
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (self.area.walkable(new_pos_x, new_pos_y)):
            self.area.update_character_position(self.pos, (new_pos_x, new_pos_y))
            self.pos = new_pos_x, new_pos_y

    def set_ai(self, ai):
        self.ai = ai

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

    def attack(self, direction):
        target = self.area.get_character_at((self.pos[0] + direction[0], self.pos[1] + direction[1]))
        if target:
            resolve_attack(self, target)
