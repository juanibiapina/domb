from character import Character
from tileset import TileSetManager
from dice import Dice

tiles = TileSetManager("resources/tiles.yaml")
blood_tile = tiles.get("BLOOD")


class Cat(Character):
    hit_dice = Dice("1/2d8+2")
    tile = tiles.get("CAT")
    blood_tile = blood_tile


class Dog(Character):
    hit_dice = Dice("1d8+2")
    tile = tiles.get("DOG")
    blood_tile = blood_tile


class Wolf(Character):
    hit_dice = Dice("2d8+4")
    tile = tiles.get("WOLF")
    blood_tile = blood_tile


class Cow(Character):
    hp = 50
    tile = tiles.get("COW")
    blood_tile = blood_tile
