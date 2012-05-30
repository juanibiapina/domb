from character import Character
from tileset import tiles
from dice import Dice

blood_tile = tiles["BLOOD"]


class Cat(Character):
    hit_dice = Dice("1/2d8+2")
    name = "Cat"
    tile = tiles["CAT"]
    blood_tile = blood_tile


class Dog(Character):
    hit_dice = Dice("1d8+2")
    name = "Dog"
    tile = tiles["DOG"]
    blood_tile = blood_tile


class Wolf(Character):
    hit_dice = Dice("2d8+4")
    name = "Wolf"
    tile = tiles["WOLF"]
    blood_tile = blood_tile


class Cow(Character):
    hp = 50
    name = "Cow"
    tile = tiles["COW"]
    blood_tile = blood_tile
