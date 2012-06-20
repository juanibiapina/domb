def place_hero(area, character):
    character.pos = area.get_position_in_room("initial room")
    character.place(area)


def place_monster(area, character):
    character.pos = area.get_random_position()
    character.place(area)


def place_item(area, item):
    area.add_item(item, area.get_random_position())
