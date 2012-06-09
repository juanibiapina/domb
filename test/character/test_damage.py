from mock import Mock

from domb.character.damage import Damage


character = Mock(name='character')


def test_uses_modifiers():
    character.weapon.get_damage.return_value = 3

    dam = Damage(character)
    assert dam.get_value() == 3


def test_knows_weapon():
    character.weapon = "weapon"

    dam = Damage(character)
    assert dam.get_weapon() == "weapon"
