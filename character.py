from d20 import roll


class Character(object):
    def __init__(self, tile_index, dungeon):
        self.tile_index = tile_index
        self.dungeon = dungeon
        self.pos = dungeon.get_random_position()
        self.dungeon.add_character(self, self.pos)
        self.ai = None
        self.hp = 2  # cat hp

    def draw(self, surface, tile_set):
        tile_set.blit_tile(surface, self.tile_index, self.pos)

    def move(self, dx, dy):
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (self.dungeon.walkable(new_pos_x, new_pos_y)):
            self.dungeon.update_character_position(self.pos, (new_pos_x, new_pos_y))
            self.pos = new_pos_x, new_pos_y

    def set_ai(self, ai):
        self.ai = ai

    def run_turn(self):
        if self.is_incapacitated():
            self.dungeon.remove_character(self)
        else:
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
