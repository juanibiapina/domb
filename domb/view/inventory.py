from pygame import draw
from pygame.locals import Color
from vec2d import Vec2d


class InventoryView(object):
    SLOT_SIZE = 32

    def __init__(self, inventory):
        self.pos = Vec2d(1, 1)
        self.display = False
        self.inventory = inventory

    def draw(self, screen):
        if not self.display:
            return

        for i in range(len(self.inventory)):
            self._draw_slot(i, screen)
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            item.draw(screen, self.pos + Vec2d(i, 0))

    def toggle(self):
        self.display = not self.display

    def _draw_slot(self, i, screen):
        slot_pos = (self.pos * self.SLOT_SIZE) + Vec2d(i * self.SLOT_SIZE, 0)
        draw.rect(screen, Color("#AE5E21"),
                  (slot_pos.x, slot_pos.y, self.SLOT_SIZE, self.SLOT_SIZE))
        draw.rect(screen, Color("#4D2C12"),
                  (slot_pos.x, slot_pos.y, self.SLOT_SIZE, self.SLOT_SIZE), 1)

    def __len__(self):
        return len(self.items)
