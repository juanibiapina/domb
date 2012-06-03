import domb
from domb.dice import Dice
from domb.dice import roll, attack_roll


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


def test_roll_1d8():
    assert roll(1, 8, 0) == 5


def test_roll_2d8():
    assert roll(2, 8, 0) == 10


def test_roll_3d8_plus_2():
    assert roll(3, 8, 2) == 21


def test_roll_half_d8():
    assert roll(0.5, 8, 0) == 2


def test_roll_half_d8_plus_3():
    assert roll(0.5, 8, 3) == 5


def test_roll_doesnt_round_to_zero():
    assert roll(0.5, 1, 0, 1) == 1


def test_attack_roll():
    assert attack_roll() == 11
