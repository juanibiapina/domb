from mock import Mock
from domb.area import DungeonBuilder, Entity
from domb.view.dungeon import DungeonView
from domb.vec2d import Vec2d

screen = Mock(name="screen")
fake_tile = Mock(name="tile")

wolf = Mock(name="wolf")
wolf.is_incapacitated.return_value = False
wolf.pos = Vec2d(2, 2)

builder = DungeonBuilder()
builder.add_rectangle(1, 1, 4, 4, Entity(fake_tile, walkable=True))

area = builder.get_dungeon()
area.add_character(wolf)


def test_not_walkable_where_theres_a_character():
    assert not area.walkable(wolf.pos)


def test_walkable_over_dead_monster():
    wolf.is_incapacitated.return_value = True
    assert area.walkable(wolf.pos)


def test_draw_characters():
    camera = Mock(name = "Camera")
    DungeonView(area).draw(screen, camera)
    wolf.draw.assert_called_with(screen, camera)


def test_run_character_turns():
    area.run_turn()
    wolf.run_turn.assert_called()


def test_get_character_at():
    assert area.get_character_at((2, 2)) == wolf


def test_can_hold_items():
    pos = (1, 1)
    area.add_item("item", pos)
    assert area.pick_up_item(pos) == "item"
    assert area.pick_up_item(pos) == None
