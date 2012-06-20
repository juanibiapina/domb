from mock import Mock
from domb.character.character import Character
from domb.vec2d import Vec2d
from domb.character.attribute import Attribute

area = Mock(name="area")

potion = Mock(name="potion")
potion.get_name.return_value = "potion"


def create_char_in_area():
    char = Character()
    char.pos = Vec2d(2, 2)
    char.place(area)
    return char


def test_character_move():
    char = create_char_in_area()

    char.move(Vec2d(1, 1))
    assert char.pos == Vec2d(3, 3)


def test_character_fail_to_pick_up_item():
    area.pick_up_item.return_value = None
    char = create_char_in_area()

    char.pick_up_item()
    assert len(char.get_items()) == 0


def test_character_ACTUALLY_pick_up_item():
    area.pick_up_item.return_value = potion
    char = create_char_in_area()

    char.pick_up_item()
    assert len(char.get_items()) == 1


def test_set_attributes():
    char = create_char_in_area()

    char.set_attributes("Str 3, Dex 15, Con 10, Int 2, Wis 12, Cha 7")
    assert char.str == Attribute(3)
    assert char.dex == Attribute(15)
    assert char.con == Attribute(10)
    assert char.int == Attribute(2)
    assert char.wis == Attribute(12)
    assert char.cha == Attribute(7)
