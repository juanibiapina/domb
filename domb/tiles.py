from tileset import TileSet, Tile

BASE_SET = TileSet("images/tileset.png")
BLOOD_SET = TileSet("images/blood.png")

WOLF = Tile(6, 1, BASE_SET)
GROUND = Tile(9, 31, BASE_SET)
HOLE = Tile(13, 32, BASE_SET)
COW = Tile(5, 4, BASE_SET)
HUNTER = Tile(18, 16, BASE_SET)
CAT = Tile(28, 1, BASE_SET)
DOG = Tile(1, 1, BASE_SET)
CHEST = Tile(30, 16, BASE_SET)
BLOOD = Tile(1, 1, BLOOD_SET)
