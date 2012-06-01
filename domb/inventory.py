from vec2d import Vec2d
from pygame import draw
from pygame.locals import Color


class Inventory(object):
    SLOT_SIZE = 32

    def __init__(self):
        self.display = False
        self.pos = Vec2d(50, 50)
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def draw(self, screen):
        if not self.display:
            return

        for i in range(len(self)):
            self._draw_slot(i, screen)

    def toggle(self):
        self.display = not self.display

    def _draw_slot(self, i, screen):
        slot_pos = self.pos + Vec2d(i * self.SLOT_SIZE, 0)
        draw.rect(screen, Color("#AE5E21"),
                  (slot_pos.x, slot_pos.y, self.SLOT_SIZE, self.SLOT_SIZE))
        draw.rect(screen, Color("#4D2C12"),
                  (slot_pos.x, slot_pos.y, self.SLOT_SIZE, self.SLOT_SIZE), 1)

    def __len__(self):
        return len(self.items)
