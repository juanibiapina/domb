from random import randint


def roll(sides):
    return randint(1, sides)


def resolve_damage(origin, target):
    damage = origin.calculate_damage()
    target.damage(damage)


def resolve_attack(origin, target):
    attack = origin.calculate_attack()
    ac = target.calculate_ac()
    if attack >= ac:
        resolve_damage(origin, target)
