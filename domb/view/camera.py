from domb.vec2d import Vec2d


class Camera(object):
    def __init__(self, screen):
        self.position = Vec2d(0, 0)
        self.screen = screen
        self._character = None

    def translate(self, position, tile_size=None):
        screen_offset = Vec2d(self.screen.get_width(), self.screen.get_height()) / (2 * tile_size)
        new_pos = self.position + position + screen_offset
        if self._character:
            new_pos -= self._character.pos

        return new_pos

    def follow(self, character):
        self._character = character
