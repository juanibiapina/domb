class Character(object):
    def __init__(self, tile_index, dungeon):
        self.tile_index = tile_index
        self.dungeon = dungeon
        self.pos = (0, 0)

    def draw(self, surface, tile_set):
        tile_set.blit_tile(surface, self.tile_index, self.pos)

    def move(self, dx, dy):
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (self.dungeon.walkable(new_pos_x, new_pos_y)):
            self.pos = new_pos_x, new_pos_y
