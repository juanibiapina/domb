from domb.dice import roll


class Attack(object):
    def __init__(self, character):
        self.str = character.str
        self.size = character.size
        self.attack_base = int(character.type.base_attack * character.hp.hit_dice)

    def roll(self):
        return roll(1, 20, self.attack_base + self.str.get_modifier() + self.size.get_modifier())
