from domb.dice import roll


class HP(object):
    def __init__(self, character):
        self.number_of_dice = character.hit_dice_number
        self.sides = character.hit_dice_value
        self.con = character.con
        self.max = 0
        self.roll()
        self.current_value = self.max

    def roll(self):
        self.max += roll(self.number_of_dice, self.sides, self.con.get_modifier())

    def damage(self, damage):
        self.current_value -= damage
