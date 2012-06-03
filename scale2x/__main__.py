import sys
from pygame.transform import scale2x
import pygame.image as image
import pygame
import os.path as p


def main():
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.init()
    input_image_name = sys.argv[1]
    result = scale2x(image.load(input_image_name).convert_alpha())
    path, name = p.split(input_image_name)
    old_name, ext = p.splitext(name)
    new_name = old_name + "2x" + ext
    new_path = p.join(path, new_name)
    image.save(result, new_path)


if __name__ == "__main__":
    main()
