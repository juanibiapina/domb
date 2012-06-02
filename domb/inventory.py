class Inventory(object):

    def __init__(self, capacity=10):
        self.items = []
        self.capacity = capacity

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __iter__(self):
        return iter(self.items)
