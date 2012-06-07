from itertools import izip_longest


class Inventory(object):

    def __init__(self, capacity=10):
        self.items = []
        self.capacity = capacity
        self.current_slot = 0

    def add_item(self, item):
        inv_item = filter(lambda x: x[0].get_name() == item.get_name(), self.items)
        if inv_item:
            self.items[self.items.index(inv_item[0])] = (item, inv_item[0][1] + 1)
        else:
            self.items.append((item, 1))

    def remove_current(self):
        item, quantity = self.items[self.current_slot]
        if quantity == 0:
            del self.items[self.current_slot]
        else:
            self.items[self.current_slot] = item, quantity - 1

    def next_slot(self):
        self.current_slot = (self.current_slot + 1) % self.capacity

    def previous_slot(self):
        self.current_slot = (self.current_slot - 1) % self.capacity

    def is_selected(self, slot):
        return self.current_slot == slot

    def current_item(self):
        return self.items[self.current_slot][0]

    def slots_and_items(self):
        slots = self.capacity
        return izip_longest(range(slots), self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]
