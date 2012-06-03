from character.character import Character
import tiles
from dice import Dice

blood_tile = tiles.BLOOD


class Cat(Character):
    name = "Cat"
    hit_dice = Dice("1/2d8+2")
    attributes = "Str 3, Dex 15, Con 10, Int 2, Wis 12, Cha 7"
    tile = tiles.CAT
    blood_tile = blood_tile


class Dog(Character):
    name = "Dog"
    hit_dice = Dice("1d8+2")
    attributes = "Str 13, Dex 17, Con 15, Int 3, Wis 12, Cha 6"
    tile = tiles.DOG
    blood_tile = blood_tile


class Wolf(Character):
    name = "Wolf"
    hit_dice = Dice("2d8+4")
    attributes = "Str 13, Dex 15, Con 15, Int 2, Wis 12, Cha 6"
    tile = tiles.WOLF
    blood_tile = blood_tile


class Cow(Character):
    hp = 50
    name = "Cow"
    tile = tiles.COW
    blood_tile = blood_tile
