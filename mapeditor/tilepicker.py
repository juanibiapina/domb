from pygame import draw
from pygame.locals import Color
from pygame.locals import KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_a, K_s, K_w, K_d

from domb.tileset import TileSet
from domb.tileset import Tile
from domb.vec2d import Vec2d


class TilePicker(object):
    tileset = TileSet("images/tileset.png")
    offset = Vec2d(0, 0)
    current_selected = Vec2d(0, 0)
    active = False

    def toggle(self):
        self.active = not self.active

    def draw(self, surface):
        if not self.active:
            return

        iwidth, iheight = self.tileset.get_size()
        tile_size = self.tileset.get_tile_size()
        width = iwidth / tile_size
        height = iheight / tile_size
        for w in range(width):
            for h in range(height):
                self.tileset.blit_tile(surface, Vec2d(w, h), Vec2d(w, h) + self.offset)

        box_pos = (self.current_selected + self.offset) * tile_size
        draw.rect(surface, Color("white"), (box_pos.x, box_pos.y, tile_size, tile_size), 1)

    def get_current_tile(self):
        pos = self.current_selected
        return Tile(pos.x, pos.y, self.tileset)

    def handle_input(self, ev):
        if not self.active:
            return False

        if ev.type == KEYUP:

            # movement
            if ev.key == K_s:
                self.offset += Vec2d(0, -1)
            if ev.key == K_w:
                self.offset += Vec2d(0, 1)
            if ev.key == K_a:
                self.offset += Vec2d(1, 0)
            if ev.key == K_d:
                self.offset += Vec2d(-1, 0)

            # selection
            if ev.key == K_DOWN:
                self.current_selected += Vec2d(0, 1)
            if ev.key == K_UP:
                self.current_selected += Vec2d(0, -1)
            if ev.key == K_LEFT:
                self.current_selected += Vec2d(-1, 0)
            if ev.key == K_RIGHT:
                self.current_selected += Vec2d(1, 0)
            return True
        return False
