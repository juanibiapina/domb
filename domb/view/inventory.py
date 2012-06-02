from pygame import draw
from pygame.locals import Color
from vec2d import Vec2d
from itertools import izip_longest


class InventoryView(object):
    SLOT_SIZE = 32
    SLOTS = 5

    def __init__(self, inventory):
        self.pos = Vec2d(1, 1)
        self.display = False
        self.inventory = inventory
        self.active = False

    def draw(self, screen):
        if not self.display:
            return

        for slot, item in self._slots_and_items():
            self._draw_slot(slot, screen)
            if item:
                item.draw(screen, self.pos + Vec2d(slot, 0))

    def toggle(self):
        self.display = not self.display
        self.active = not self.active

    def _draw_slot(self, i, screen):
        slot_pos = (self.pos * self.SLOT_SIZE) + Vec2d(i * self.SLOT_SIZE, 0)
        draw.rect(screen, Color("#AE5E21"),
                  (slot_pos.x, slot_pos.y, self.SLOT_SIZE, self.SLOT_SIZE))
        draw.rect(screen, Color("#4D2C12"),
                  (slot_pos.x, slot_pos.y, self.SLOT_SIZE, self.SLOT_SIZE), 1)

    def _slots_and_items(self):
        slots = self.inventory.capacity
        return izip_longest(range(slots), self.inventory)

    def __len__(self):
        return len(self.items)

    def is_active(self):
        return self.active
