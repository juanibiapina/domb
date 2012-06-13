class DungeonView(object):

  def __init__(self, area):
    self.area = area

  def draw(self, screen, camera):
      for pos, spot in self.area._data.iteritems():
          spot.draw(screen, pos, camera)
      for character in self.area.characters:
          character.draw(screen, camera)

