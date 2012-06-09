from mock import Mock

import domb.character.attack
from domb.character.attack import Attack


def fake_roll():
    return 10
domb.character.attack.attack_roll = fake_roll

character = Mock(name='character')


def test_uses_modifiers():
    character.has_feat.return_value = False
    character.str.get_modifier.return_value = 2
    character.size.get_modifier.return_value = 3
    character.type.base_attack = 2
    character.hp.hit_dice = 3

    at = Attack(character)
    assert at.roll() == (False, 10 + (2 * 3) + 2 + 3)


def test_weapon_finesse_uses_dex():
    character.has_feat.return_value = True
    character.str.get_modifier.return_value = 2
    character.dex.get_modifier.return_value = 3
    character.size.get_modifier.return_value = 3
    character.type.base_attack = 2
    character.hp.hit_dice = 3

    at = Attack(character)
    assert at.roll() == (False, 10 + (2 * 3) + 3 + 3)
