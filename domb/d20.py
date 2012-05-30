from random import randint
import logging


logger = logging.getLogger('console')


def roll(sides):
    return randint(1, sides)


def resolve_damage(origin, target):
    damage = origin.calculate_damage()
    target.damage(damage)
    return damage


def resolve_attack(origin, target):
    attack = origin.calculate_attack()
    ac = target.calculate_ac()
    if attack >= ac:  # hit!
        damage = resolve_damage(origin, target)
        logger.info('%s attacked %s - attack roll: %d / ac: %d / damage roll: %d', origin.get_name(), target.get_name(), attack, ac, damage)
    else:  # no hit
        logger.info('%s attacked %s - attack roll: %d / ac: %d', origin.get_name(), target.get_name(), attack, ac)
