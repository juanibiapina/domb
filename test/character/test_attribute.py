from mock import Mock

from domb.character.attribute import Attribute

dice = Mock(name="dice")
dice.roll.return_value = 10

attr = Attribute()
attr.dice = dice


def test_roll():
    attr.roll()
    assert attr.get_value() == 10


def test_positive_modifiers():
    attr.value = 10
    assert attr.get_modifier() == 0

    attr.value = 11
    assert attr.get_modifier() == 0

    attr.value = 12
    assert attr.get_modifier() == 1

    attr.value = 13
    assert attr.get_modifier() == 1

    attr.value = 14
    assert attr.get_modifier() == 2

    attr.value = 20
    assert attr.get_modifier() == 5


def test_negative_modifiers():
    attr.value = 1
    assert attr.get_modifier() == -5

    attr.value = 2
    assert attr.get_modifier() == -4

    attr.value = 3
    assert attr.get_modifier() == -4

    attr.value = 4
    assert attr.get_modifier() == -3

    attr.value = 5
    assert attr.get_modifier() == -3

    attr.value = 9
    assert attr.get_modifier() == -1
