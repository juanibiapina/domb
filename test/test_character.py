from mock import Mock
from domb.character import Character

area = Mock(name="area")
area.get_random_position.return_value = (2,2)

def test_create_character_in_area():
    char = Character(area)
    assert char.pos == (2, 2)

def test_character_move():
    char = Character(area)
    char.move(1, 1)
    assert char.pos == (3, 3)
