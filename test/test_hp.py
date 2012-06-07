from domb.character.hp import HP
from mock import Mock

char_type = Mock(hit_dice_sides=10)
con = Mock()
con.get_modifier.return_value = 1
character = Mock(hit_dice=1, type=char_type, con=con)


def test_start_with_max_hp():
    character.has_feat.return_value = False
    hp = HP(character)
    assert hp.max == 11
