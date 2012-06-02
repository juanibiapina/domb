from domb.inventory import Inventory

inv = Inventory(capacity=3)


def test_add_items():
    inv.add_item("item 1")
    inv.add_item("item 2")
    assert len(inv) == 2


def test_indexable():
    inv.add_item("item 1")
    assert inv[0] == "item 1"


def test_selection():
    inv.next_slot()
    assert inv.is_selected(1)
