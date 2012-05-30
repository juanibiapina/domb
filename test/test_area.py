from domb.area import DungeonBuilder, Entity

from mock import Mock

screen = Mock(name="screen")
fake_tile = Mock(name="tile")

wolf = Mock(name="wolf")
wolf.is_incapacitated.return_value = False

builder = DungeonBuilder()
builder.add_rectangle(1,1,4,4, Entity(fake_tile, walkable=True))

area = builder.get_dungeon()
area.add_character(wolf, (2,2))

def test_not_walkable_where_theres_a_character():
    assert not area.walkable(2,2)
    
def test_walkable_over_dead_monster():
    wolf.is_incapacitated.return_value = True
    assert area.walkable(2,2)
            
def test_draw_characters():
    area.draw(screen)
    wolf.draw.assert_called_with(screen)

def test_run_character_turns():
    area.run_turn()
    wolf.run_turn.assert_called()

def test_get_character_at():
    assert area.get_character_at((2,2)) == wolf
