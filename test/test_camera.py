from domb.view.camera import Camera
from domb.vec2d import Vec2d

def test_camera_transformation():
  camera = Camera()
  camera.offset(Vec2d(1,1))

  assert camera.translate(Vec2d(2,0)) == Vec2d(3,1)
  assert camera.translate(Vec2d(0,0)) == Vec2d(1,1)
