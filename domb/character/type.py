class Type(object):
    hit_dice_sides = 8
    base_attack = 3.0 / 4.0


class Animal(Type):
    hit_dice_sides = 8
    base_attack = 3.0 / 4.0


class Fighter(Type):
    hit_dice_sides = 10
    base_attack = 1.0
