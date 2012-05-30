from character import Character
from tileset import TileSetManager

tiles = TileSetManager("resources/tiles.yaml")
blood_tile = tiles.get("BLOOD")

class Cat(Character):
    hp = 2
    tile = tiles.get("CAT")
    blood_tile = blood_tile

class Hunter(Character):
    hp = 6
    tile = tiles.get("HUNTER")
    blood_tile = blood_tile

class Wolf(Character):
    hp = 13
    tile = tiles.get("WOLF")
    blood_tile = blood_tile

class Cow(Character):
    hp = 50
    tile = tiles.get("COW")
    blood_tile = blood_tile
