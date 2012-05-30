from random import randint
import logging


logger = logging.getLogger('console')


def roll(sides):
    return randint(1, sides)


def resolve_damage(origin, target, critical):
    damage = origin.calculate_damage() * critical
    target.damage(damage)
    return damage


def resolve_attack(origin, target):
    attack = origin.calculate_attack()
    ac = target.calculate_ac()
    critical = 1

    if attack == 20 and origin.calculate_attack() >= ac:  # critical hit!
        logger.info('Critical HIT!')
        critical = 2

    if attack >= ac:  # hit!
        damage = resolve_damage(origin, target)
        logger.info('%s attacked %s - attack: %d / ac: %d / damage: %d', origin.get_name(), target.get_name(), attack, ac, damage)
    else:  # no hit
        logger.info('%s attacked %s - attack: %d / ac: %d', origin.get_name(), target.get_name(), attack, ac)
