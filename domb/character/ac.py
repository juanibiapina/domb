class AC(object):
    BASE_AC = 10

    def __init__(self, character):
        self.dex = character.dex
        self.natural_armor = character.natural_armor
        self.size = character.size

    def get_value(self):
        return self.BASE_AC + self.dex.get_modifier() + self.natural_armor + self.size.get_modifier()
