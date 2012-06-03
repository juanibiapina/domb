class AC(object):
    BASE_AC = 10

    def __init__(self, dex, natural_armor):
        self.dex = dex
        self.natural_armor = natural_armor

    def get_value(self):
        return self.BASE_AC + self.dex.get_modifier() + self.natural_armor
