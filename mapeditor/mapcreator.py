from pygame import draw
from pygame.locals import Color
from pygame.locals import KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_r, K_x, K_a

from domb.area import Area
from domb.area import Spot
from domb.entity import Entity
from domb.vec2d import Vec2d


class MapCreator(object):
    def __init__(self, tile_picker):
        self.data = {}
        self.selected = Vec2d(10, 10)
        self.tile_picker = tile_picker

    def draw_selection_box(self, surface):
        box_pos = self.selected * 32
        draw.rect(surface, Color("white"), (box_pos.x, box_pos.y, 32, 32), 1)

    def draw(self, surface):
        if self.tile_picker.active:
            return
        map = Area(self.data)
        map.draw(surface)
        self.draw_selection_box(surface)

    def replace_tile(self):
        self.data[self.selected] = Spot(Entity(self.tile_picker.get_current_tile()))

    def add_tile(self):
        if self.selected in self.data:
            spot = self.data[self.selected]
        else:
            spot = Spot()
            self.data[self.selected] = spot
        spot.add_entity(Entity(self.tile_picker.get_current_tile()))

    def delete_tile(self):
        del self.data[self.selected]

    def handle_input(self, ev):
        if ev.type == KEYUP:
            # selection
            if ev.key == K_DOWN:
                self.selected = self.selected + Vec2d(0, 1)
            if ev.key == K_UP:
                self.selected = self.selected + Vec2d(0, -1)
            if ev.key == K_LEFT:
                self.selected = self.selected + Vec2d(-1, 0)
            if ev.key == K_RIGHT:
                self.selected = self.selected + Vec2d(1, 0)

            # replace tile
            if ev.key == K_r:
                self.replace_tile()

            # add tile
            if ev.key == K_a:
                self.add_tile()

            # delete tile
            if ev.key == K_x:
                self.delete_tile()

            return True
        return False
