from random import randint
import re


class Dice(object):
    DICE_REGEXP = re.compile("([0-9]+|1/2)d([0-9]+)")

    def __init__(self, description):
        base_dice, modifiers = self._split_description(description)
        self._parse_dice(base_dice)
        self._calculate_modifiers(modifiers)

    def roll(self):
        dice_roll = sum(randint(1, self.sides) for i in range(self.num_dices))
        return int(dice_roll * self.multiplier) + self.modifier

    def _split_description(self, description):
        description_components = description.split("+")
        return description_components[0], description_components[1:]

    def _parse_dice(self, dice_description):
        m = self.DICE_REGEXP.search(dice_description)

        num_dices = m.group(1)
        if num_dices == "1/2":
            self.num_dices = 1
            self.multiplier = 0.5
        else:
            self.num_dices = int(num_dices)
            self.multiplier = 1

        self.sides = int(m.group(2))

    def _calculate_modifiers(self, modifiers):
        self.modifier = sum(int(i) for i in modifiers)


def roll(number, sides, modifier_per_dice):
    return sum(randint(1, sides) + modifier_per_dice for i in range(number))
