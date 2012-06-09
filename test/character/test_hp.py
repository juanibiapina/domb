from mock import Mock

import domb.dice
from domb.character.hp import HP


def roll(a, b, c, d):
    return a + b + c + d
domb.character.hp.roll = roll

char_type = Mock(hit_dice_sides=10)
con = Mock()
con.get_modifier.return_value = 1
character = Mock(hit_dice=1, type=char_type, con=con)
character.has_feat.return_value = False


def test_starts_with_full_dice():
    hp = HP(character)
    assert hp.max == 11


def test_starts_with_max_hp():
    hp = HP(character)
    assert hp.value == 11


def test_damage():
    hp = HP(character)
    hp.damage(4)

    assert hp.value == 7


def test_restore():
    hp = HP(character)
    hp.damage(6)
    assert hp.restore(5) == 5
    assert hp.value == 10


def test_restore_to_max():
    hp = HP(character)
    hp.damage(4)
    assert hp.restore(5) == 4
    assert hp.value == 11


def test_roll():
    hp = HP(character)
    hp.roll()
    assert hp.max == 24


def test_toughness():
    character.has_feat.return_value = True
    hp = HP(character)
    assert hp.max == 11 + 3
