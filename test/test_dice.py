import domb
from domb.dice import Dice


def fake_randint(a, b):
    return a + (b / 2)
domb.dice.randint = fake_randint


def test_a_d8_throw():
    dice = Dice("1d8")
    assert dice.roll() == 5


def test_two_d8():
    dice = Dice("2d8")
    assert dice.roll() == 10


def test_two_d8_plus_3():
    dice = Dice("2d8+3")
    assert dice.roll() == 13


def test_half_d8():
    dice = Dice("1/2d8")
    assert dice.roll() == 2
