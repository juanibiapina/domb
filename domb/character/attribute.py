from domb.dice import Dice


class Attribute(object):
    dice = Dice("3d6")
    value = 0

    def roll(self):
        self.value = self.dice.roll()

    def get_value(self):
        return self.value

    def get_modifier(self):
        return (self.value - 10) / 2
