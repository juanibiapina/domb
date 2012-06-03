from domb.dice import Dice


class Attribute(object):
    dice = Dice("3d6")

    def __init__(self, value=0):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def roll(self):
        self.value = self.dice.roll()

    def get_value(self):
        return self.value

    def get_modifier(self):
        return (self.value - 10) / 2
