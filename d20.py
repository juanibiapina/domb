from random import randint

BASE_AC = 10


def roll(sides):
    return randint(1, sides)


def resolve_damage(origin, target):
    damage = roll(3)  # unarmed strike
    target.hp -= damage
    if target.hp <= 0:
        print "incapacitated"


def resolve_attack(origin, target):
    attack = roll(20)
    ac = BASE_AC
    if attack >= ac:
        resolve_damage(origin, target)
    else:
        print "miss"
