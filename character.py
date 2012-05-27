from d20 import roll


class Character(object):
    def __init__(self, tile_index, dungeon):
        self.tile_index = tile_index
        self.dungeon = dungeon
        self.pos = dungeon.get_random_position()
        self.ai = None
        self.hp = 2  # cat hp

    def draw(self, surface, tile_set):
        tile_set.blit_tile(surface, self.tile_index, self.pos)

    def move(self, dx, dy):
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (self.dungeon.walkable(new_pos_x, new_pos_y)):
            self.pos = new_pos_x, new_pos_y

    def set_ai(self, ai):
        self.ai = ai

    def update(self):
        if self.ai:
            self.ai.update(self)

    def calculate_damage(self):
        return roll(3)  # unarmed strike

    def calculate_attack(self):
        return roll(20)  # base attack, no modifiers

    def calculate_ac(self):
        return 10  # base ac, no modifiers

    def damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print "incapacitated"
