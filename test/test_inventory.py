from domb.inventory import Inventory
from mock import Mock

item_a = Mock(name="potion")
item_b = Mock(name="armor")


def test_add_items():
    inv = Inventory(capacity=3)
    inv.add_item(item_a)
    inv.add_item(item_b)
    assert len(inv) == 2


def test_stack_items():
    inv = Inventory(capacity=3)
    inv.add_item(item_a)
    inv.add_item(item_a)
    assert inv[0][1] == 2


def test_indexable():
    inv = Inventory(capacity=3)
    inv.add_item(item_a)
    assert inv[0][0] == item_a


def test_selection():
    inv = Inventory(capacity=3)
    inv.next_slot()
    assert inv.is_selected(1)
