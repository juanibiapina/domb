import domb
from domb.dice import Dice


def fake_randint(a, b):
    return fake_randint.return_value

domb.dice.randint = fake_randint


def test_a_d8_throw():
    fake_randint.return_value = 5
    dice = Dice("1d8")
    assert dice.roll() == 5

    fake_randint.return_value = 3
    assert dice.roll() == 3
