from domb.dice import roll


class HP(object):
    def __init__(self, number_of_dice, sides, con):
        self.number_of_dice = number_of_dice
        self.sides = sides
        self.con = con
        self.max = 0
        self.roll()
        self.current_value = self.max

    def roll(self):
        self.max += roll(self.number_of_dice, self.sides, self.con.get_modifier())

    def damage(self, damage):
        self.current_value -= damage
