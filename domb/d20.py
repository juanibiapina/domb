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
    attack = origin.calculate_attack()
    ac = target.calculate_ac()

    if attack >= ac:  # hit!
        if attack == 20:
            critical_confirmation = origin.calculate_attack()
            critical = 2 if (critical_confirmation >= ac) else 1
            damage = resolve_damage(origin, target, critical)
            logger.info('%s attacked %s - attack: %d (critical: %d) / ac: %d / damage (x%d): %d', origin.get_name(), target.get_name(), attack, critical_confirmation, ac, critical, damage)
        else:
            damage = resolve_damage(origin, target)
            logger.info('%s attacked %s - attack: %d / ac: %d / damage: %d', origin.get_name(), target.get_name(), attack, ac, damage)
    else:  # no hit
        logger.info('%s attacked %s - attack: %d / ac: %d / miss', origin.get_name(), target.get_name(), attack, ac)
