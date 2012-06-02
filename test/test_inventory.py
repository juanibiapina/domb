from domb.inventory import Inventory

inv = Inventory()


def test_add_items():
    inv.add_item("item 1")
    inv.add_item("item 2")
    assert len(inv) == 2


def test_indexable():
    inv.add_item("item 1")
    assert inv[0] == "item 1"
