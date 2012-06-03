from domb.dice import roll


class HP(object):
    def __init__(self, character):
        self.hit_dice = character.hit_dice
        self.sides = character.type.hit_dice_sides
        self.con = character.con
        self.max = 0
        self.roll()
        self.current_value = self.max

    def roll(self):
        self.max += roll(self.hit_dice, self.sides, self.con.get_modifier())

    def damage(self, damage):
        self.current_value -= damage
