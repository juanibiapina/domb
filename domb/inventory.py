class Inventory(object):

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]
