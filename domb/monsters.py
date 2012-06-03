from character.character import Character
import tiles
blood_tile = tiles.BLOOD


class Cat(Character):
    name = "Cat"
    hit_dice_number = 0.5
    hit_dice_value = 8
    attributes = "Str 3, Dex 15, Con 10, Int 2, Wis 12, Cha 7"
    tile = tiles.CAT
    blood_tile = blood_tile


class Dog(Character):
    name = "Dog"
    hit_dice_number = 1
    hit_dice_value = 8
    attributes = "Str 13, Dex 17, Con 15, Int 3, Wis 12, Cha 6"
    natural_armor = 1
    tile = tiles.DOG
    blood_tile = blood_tile


class Wolf(Character):
    name = "Wolf"
    hit_dice_number = 2
    hit_dice_value = 8
    attributes = "Str 13, Dex 15, Con 15, Int 2, Wis 12, Cha 6"
    natural_armor = 2
    tile = tiles.WOLF
    blood_tile = blood_tile


class Cow(Character):
    name = "Cow"
    hit_dice_number = 3
    hit_dice_value = 8
    attributes = "Str 13, Dex 15, Con 15, Int 2, Wis 12, Cha 6"
    tile = tiles.COW
    blood_tile = blood_tile
