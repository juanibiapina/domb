from domb.entity import Entity


def test_walkable_by_default():
    e = Entity(None)
    assert e.is_walkable() == True


def test_not_walkable():
    e = Entity(None)
    e.walkable = False
    assert e.is_walkable() == False
