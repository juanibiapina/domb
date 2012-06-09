from domb.dice import roll


class HP(object):
    def __init__(self, character):
        self.hit_dice = character.hit_dice
        self.sides = character.type.hit_dice_sides
        self.con = character.con
        self.max = self.sides + self.con.get_modifier()
        if character.has_feat("Toughness"):
            self.max += 3
        self.value = self.max

    def roll(self):
        self.max += roll(self.hit_dice, self.sides, self.con.get_modifier(), 1)

    def damage(self, damage):
        self.value -= damage

    def restore(self, value):
        if self.max - self.value < value:
            restored = self.max - self.value
            self.value = self.max
        else:
            restored = value
            self.value += value
        return restored
