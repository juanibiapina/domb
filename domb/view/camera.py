from domb.vec2d import Vec2d

class Camera(object):

  def __init__(self):
    self._offset = Vec2d(0,0)


  def offset(self, offset_by):
    self._offset += offset_by

  def translate(self, position):
    return self._offset + position
