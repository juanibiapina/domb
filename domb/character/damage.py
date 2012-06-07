class Damage(object):
    def __init__(self, character):
        self.character = character

    def get_value(self):
        return self.character.get_weapon().get_damage()

    def get_weapon(self):
        return self.character.get_weapon()
