from pygame import draw
from pygame.locals import Color
from vec2d import Vec2d


class InventoryView(object):
    SLOT_SIZE = 32
    SELECTED_ITEM_COLOR = Color("white")
    SLOT_BORDER_COLOR = Color("#4D2C12")
    SLOT_BACKGROUND_COLOR = Color("#AE5E21")

    def __init__(self, inventory):
        self.pos = Vec2d(1, 1)
        self.display = False
        self.inventory = inventory
        self.active = False
        self.current_item = 0

    def draw(self, screen):
        if not self.display:
            return

        for slot, item in self.inventory.slots_and_items():
            self._draw_slot(screen, slot)
            if item:
                item.draw(screen, self.pos + Vec2d(slot, 0))

    def next_item(self):
        self.inventory.next_slot()

    def previous_item(self):
        self.inventory.previous_slot()

    def toggle(self):
        self.display = not self.display
        self.active = not self.active

    def is_active(self):
        return self.active

    def _draw_slot(self, screen, slot):
        self._draw_slot_background(screen, slot)
        if self.inventory.is_selected(slot):
            self._draw_selection_cursor(screen, slot)
        else:
            self._draw_slot_border(screen, slot)

    def _draw_slot_border(self, screen, slot):
        draw.rect(screen, self.SLOT_BORDER_COLOR, self._slot_rect(slot), 1)

    def _draw_selection_cursor(self, screen, slot):
        draw.rect(screen, self.SELECTED_ITEM_COLOR, self._slot_rect(slot), 1)

    def _draw_slot_background(self, screen, slot):
        draw.rect(screen, self.SLOT_BACKGROUND_COLOR, self._slot_rect(slot))

    def _slot_rect(self, slot):
        pos = (self.pos * self.SLOT_SIZE) + Vec2d(slot * self.SLOT_SIZE, 0)
        return (pos.x, pos.y, self.SLOT_SIZE, self.SLOT_SIZE)
