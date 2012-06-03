from random import randint
import logging


logger = logging.getLogger('console')


def roll(sides):
    return randint(1, sides)


def resolve_damage(origin, target, critical=1):
    damage = origin.calculate_damage() * critical
    target.damage(damage)
    return damage


def resolve_attack(origin, target):
    # initialize values
    critical, attack = origin.get_attack().roll()
    ac = target.get_ac().get_value()
    confirm_critical = False  # no critical by default

    # do critical calculations
    multiplier = 1
    if critical:
        confirm_critical, new_attack = origin.get_attack().roll()
        if confirm_critical or new_attack >= ac:
            confirm_critical = True
            multiplier = 2

    # check for hit
    if critical or attack >= ac:
        damage = resolve_damage(origin, target, multiplier)
        if confirm_critical:
            logger.info('%s attacked %s - attack: %d / ac: %d / critical: %d / damage (x%d): %d', origin.get_name(), target.get_name(), attack, ac, new_attack, multiplier, damage)
        else:
            logger.info('%s attacked %s - attack: %d / ac: %d / damage: %d', origin.get_name(), target.get_name(), attack, ac, damage)
    else:  # no hit
        logger.info('%s attacked %s - attack: %d / ac: %d / miss', origin.get_name(), target.get_name(), attack, ac)
