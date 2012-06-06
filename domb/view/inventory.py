from pygame import draw
from pygame.locals import Color
from vec2d import Vec2d
from pygame.font import SysFont


class InventoryView(object):
    SLOT_SIZE = 32
    SELECTED_ITEM_COLOR = Color("white")
    SLOT_BORDER_COLOR = Color("#4D2C12")
    SLOT_BACKGROUND_COLOR = Color("#AE5E21")
    SLOT_FONT_COLOR = Color("white")

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
                self._draw_item(screen, slot, item)

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
        pos = self._slot_pos(slot)
        return (pos.x, pos.y, self.SLOT_SIZE, self.SLOT_SIZE)

    def _slot_pos(self, slot):
        return (self.pos * self.SLOT_SIZE) + Vec2d(slot * self.SLOT_SIZE, 0)

    def _draw_item(self, screen, slot, item):
        item[0].draw(screen, self.pos + Vec2d(slot, 0))
        self._draw_item_quantity(screen, slot, item[1])

    def _draw_item_quantity(self, screen, slot, quantity):
        quantity_surface = SysFont('Arial', 12, bold=True).render(str(quantity), False, self.SLOT_FONT_COLOR)
        screen.blit(quantity_surface, (self._item_quantity_pos(quantity_surface.get_size(), slot)))

    def _item_quantity_pos(self, surface_size, slot):
        pos = self._slot_pos(slot)
        return (pos.x + self.SLOT_SIZE - surface_size[0] - 1, pos.y + self.SLOT_SIZE - surface_size[1] - 1)
