from mock import Mock
from domb.character import Character
from domb.vec2d import Vec2d

area = Mock(name="area")
area.get_random_position.return_value = Vec2d(2, 2)


def test_create_character_in_area():
    char = Character(area)
    assert char.pos == Vec2d(2, 2)


def test_character_move():
    char = Character(area)
    char.move(Vec2d(1, 1))
    assert char.pos == Vec2d(3, 3)


def test_character_fail_to_pick_up_item():
    area.pick_up_item.return_value = None
    char = Character(area)
    char.pick_up_item()
    assert len(char.get_items()) == 0


def test_character_ACTUALLY_pick_up_item():
    area.pick_up_item.return_value = "item"
    char = Character(area)
    char.pick_up_item()
    assert len(char.get_items()) == 1
