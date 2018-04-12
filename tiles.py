import os
import pygame

class TileMap(object):
    def __init__(self, map, tile_w, tile_h):
        self.map = map
        self.tile_w = tile_w
        self.tile_h = tile_h
        self.width = len(map)
        self.height = len(map[0])
        self.types = 2

    def get_tile_w(self):
        return self.tile_w

    def get_tile_h(self):
        return self.tile_h

    def get_index(self, pos, cam_pos, cam_zoom, screen_dim):
        i = int((pos[0] - cam_pos[0] + screen_dim[0]/2)/int(self.tile_w*cam_zoom))
        if i > self.width:
            i = None
        j = int((pos[1] - cam_pos[1] + screen_dim[1]/2)/int(self.tile_w*cam_zoom))
        if j > self.width:
            j = None

        return (i, j)

images = []

dir = os.path.dirname(__file__)

images.append(pygame.image.load(os.path.join(dir, "res", "tiles", "tile-green.png"))) # index 0
images.append(pygame.image.load(os.path.join(dir, "res", "tiles", "tile-blue.png"))) # index 1

## TILES
#
#   Multi-Tile Format:
#     ____________________
# y^ |__1_|__2_|__3_|__4_|
#    |__5_|__6_|__7_|__8_|
#    |__9_|_10_|_11_|_12_|
#    |_13_|_14_|_15_|_16_| -> x
#  ---------------------
#
#   0 - green
#   1 - blue
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
