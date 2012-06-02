from entity import Entity
import tiles


class Potion(Entity):
    name = "Potion"

    def __init__(self):
        super(Potion, self).__init__(tiles.POTION, walkable=True)

    def get_name(self):
        return self.name
