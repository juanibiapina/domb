from random import randint
import logging


logger = logging.getLogger('console')


def roll(sides):
    return randint(1, sides)


def resolve_damage(origin, target, critical=1):
    damage = origin.damage
    value = damage.get_value() * critical
    target.resolve_damage(value)
    return damage.get_weapon(), value


def resolve_attack(origin, target):
    # initialize values
    critical, attack = origin.attack.roll()
    ac = target.ac.get_value()
    confirm_critical = False  # no critical by default

    # do critical calculations
    multiplier = 1
    if critical:
        confirm_critical, new_attack = origin.attack.roll()
        if confirm_critical or new_attack >= ac:
            confirm_critical = True
            multiplier = 2

    # check for hit
    if critical or attack >= ac:
        weapon, damage = resolve_damage(origin, target, multiplier)
        if confirm_critical:
            logger.info('%s attacked %s with %s - attack: %d / ac: %d / critical: %d / damage (x%d): %d', origin.name, target.name, weapon.get_name(), attack, ac, new_attack, multiplier, damage)
        else:
            logger.info('%s attacked %s with %s - attack: %d / ac: %d / damage: %d', origin.name, target.name, weapon.get_name(), attack, ac, damage)
    else:  # no hit
        logger.info('%s attacked %s - attack: %d / ac: %d / miss', origin.name, target.name, attack, ac)
