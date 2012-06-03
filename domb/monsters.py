from character.character import Character
from character.size import Tiny, Small, Medium
from domb.character.type import Animal
import tiles

blood_tile = tiles.BLOOD


class Cat(Character):
    name = "Cat"
    hit_dice = 0.5
    type = Animal()
    attributes = "Str 3, Dex 15, Con 10, Int 2, Wis 12, Cha 7"
    size = Tiny()
    tile = tiles.CAT
    blood_tile = blood_tile


class Dog(Character):
    name = "Dog"
    hit_dice = 1
    type = Animal()
    attributes = "Str 13, Dex 17, Con 15, Int 3, Wis 12, Cha 6"
    natural_armor = 1
    size = Small()
    tile = tiles.DOG
    blood_tile = blood_tile


class Wolf(Character):
    name = "Wolf"
    hit_dice = 2
    type = Animal()
    attributes = "Str 13, Dex 15, Con 15, Int 2, Wis 12, Cha 6"
    natural_armor = 2
    size = Medium()
    tile = tiles.WOLF
    blood_tile = blood_tile


class ConstrictorSnake(Character):
    name = "Constrictor Snake"
    hit_dice = 3
    type = Animal()
    attributes = "Str 17, Dex 17, Con 13, Int 1, Wis 12, Cha 2"
    natural_armor = 2
    size = Medium()
    feats = ['Toughness']
    tile = tiles.SNAKE
    blood_tile = blood_tile


class Cow(Character):
    name = "Cow"
    hit_dice = 3
    type = Animal()
    attributes = "Str 13, Dex 15, Con 15, Int 2, Wis 12, Cha 6"
    size = Medium()
    tile = tiles.COW
    blood_tile = blood_tile
