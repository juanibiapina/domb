COW_TILE = (5, 4)
HUNTER_TILE = (18, 16)


class Cow(object):
    def __init__(self, dungeon):
        self.dungeon = dungeon
        self.pos = (0, 0)

    def draw(self, surface, tile_set):
        tile_set.blit_tile(surface, COW_TILE, self.pos)

    def move(self, dx, dy):
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (self.dungeon.walkable(new_pos_x, new_pos_y)):
            self.pos = new_pos_x, new_pos_y


class Hunter(object):
    def __init__(self, dungeon):
        self.dungeon = dungeon
        self.pos = (7, 7)

    def draw(self, surface, tile_set):
        tile_set.blit_tile(surface, HUNTER_TILE, self.pos)

    def move(self, dx, dy):
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (self.dungeon.walkable(new_pos_x, new_pos_y)):
            self.pos = new_pos_x, new_pos_y
