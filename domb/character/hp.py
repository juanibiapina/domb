from domb.dice import roll


class HP(object):
    def __init__(self, character):
        self.hit_dice = character.hit_dice
        self.sides = character.type.hit_dice_sides
        self.con = character.con
        self.max = self.sides + self.con.get_modifier()
        if character.has_feat("Toughness"):
            self.max += 3
        self.current_value = self.max

    def roll(self):
        self.max += roll(self.hit_dice, self.sides, self.con.get_modifier(), 1)

    def damage(self, damage):
        self.current_value -= damage

    def restore(self, value):
        if self.max - self.current_value < value:
            restored = self.max - self.current_value
            self.current_value = self.max
        else:
            restored = value
            self.current_value += value
        return restored
