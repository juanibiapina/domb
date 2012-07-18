from mock import Mock
from domb.view.camera import Camera
from domb.vec2d import Vec2d


def test_camera_transformation():
    screen = Mock(name="screen")
    screen.get_width.return_value = 12
    screen.get_height.return_value = 8

    camera = Camera(screen)
    camera.position = Vec2d(1, 1)

    assert camera.translate(Vec2d(2, 0), tile_size=2) == Vec2d(6, 3)
    assert camera.translate(Vec2d(0, 0), tile_size=2) == Vec2d(4, 3)


def test_camera_change_position_when_start_following():
    character = Mock(name="character")
    character.pos = Vec2d(2, 2)

    screen = Mock(name="screen")
    screen.get_width.return_value = 10
    screen.get_height.return_value = 6

    camera = Camera(screen)
    camera.position = Vec2d(1, 1)

    camera.follow(character)

    assert camera.translate(Vec2d(2, 0), tile_size=1) == Vec2d(6, 2)
    assert camera.translate(Vec2d(0, 0), tile_size=1) == Vec2d(4, 2)
