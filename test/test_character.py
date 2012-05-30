from mock import Mock
from domb.character import Character, Vec2d

area = Mock(name="area")
area.get_random_position.return_value = Vec2d(2, 2)

def test_create_character_in_area():
    char = Character(area)
    assert char.pos == Vec2d(2, 2)

def test_character_move():
    char = Character(area)
    char.move(Vec2d(1, 1))
    assert char.pos == Vec2d(3, 3)
