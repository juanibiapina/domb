from domb.dice import attack_roll


class Attack(object):
    def __init__(self, character):
        self.str = character.str
        self.size = character.size
        self.attack_base = int(character.type.base_attack * character.hp.hit_dice)

    def roll(self):
        dice = attack_roll()
        return (dice == 20, dice + self.attack_base + self.str.get_modifier() + self.size.get_modifier())
