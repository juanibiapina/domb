from random import randint
import re

class Dice(object):
    DICE_REGEXP = re.compile("([0-9]+)d([0-9]+)")
    
    def __init__(self, description):
        base_dice, modifiers = self._split_description(description)
        self._parse_dice(base_dice)
        self._calculate_modifiers(modifiers)
        
    def roll(self):
        dice_roll = sum(randint(1, self.sides) for i in range(self.num_dices))
        return dice_roll + self.modifier

    def _split_description(self, description):
        description_components = description.split("+")
        return description_components[0], description_components[1:]

    def _parse_dice(self, dice_description):
        m = self.DICE_REGEXP.search(dice_description)
        self.num_dices = int(m.group(1))
        self.sides = int(m.group(2))

    def _calculate_modifiers(self, modifiers):
        self.modifier = sum(int(i) for i in modifiers)
