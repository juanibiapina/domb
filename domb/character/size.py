class Size(object):
    size_modifier = 0

    def get_ac_modifier(self):
        return self.size_modifier


class Fine(Size):
    size_modifier = 8


class Diminutive(Size):
    size_modifier = 4


class Tiny(Size):
    size_modifier = 2


class Small(Size):
    size_modifier = 1


class Medium(Size):
    size_modifier = 0


class Large(Size):
    size_modifier = -1


class Huge(Size):
    size_modifier = -2


class Gargantuan(Size):
    size_modifier = -4


class Colossal(Size):
    size_modifier = -8
