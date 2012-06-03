class Size(object):
    modifier = 0

    def get_modifier(self):
        return self.modifier


class Fine(Size):
    modifier = 8


class Diminutive(Size):
    modifier = 4


class Tiny(Size):
    modifier = 2


class Small(Size):
    modifier = 1


class Medium(Size):
    modifier = 0


class Large(Size):
    modifier = -1


class Huge(Size):
    modifier = -2


class Gargantuan(Size):
    modifier = -4


class Colossal(Size):
    modifier = -8
