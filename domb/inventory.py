from itertools import izip_longest


class Inventory(object):

    def __init__(self, capacity=10):
        self.items = []
        self.capacity = capacity
        self.current_slot = 0

    def add_item(self, item):
        self.items.append(item)

    def next_slot(self):
        self.current_slot = (self.current_slot + 1) % self.capacity

    def previous_slot(self):
        self.current_slot = (self.current_slot - 1) % self.capacity

    def is_selected(self, slot):
        return self.current_slot == slot

    def slots_and_items(self):
        slots = self.capacity
        return izip_longest(range(slots), self)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __iter__(self):
        return iter(self.items)
