from domb.vec2d import Vec2d


def test_equality():
    assert Vec2d(1, 1) == Vec2d(1, 1)


def test_hash():
    assert hash(Vec2d(1, 1)) == hash(Vec2d(1, 1))
