from mock import Mock

from domb.character.ac import AC

character = Mock(name='character')

character.dex.get_modifier.return_value = 0
character.natural_armor = 0
character.size.get_modifier.return_value = 0


def test_base_value():
    ac = AC(character)
    assert ac.get_value() == 10


def test_uses_modifiers():
    character.dex.get_modifier.return_value = 2
    character.natural_armor = 3
    character.size.get_modifier.return_value = 3
    ac = AC(character)
    assert ac.get_value() == 18
