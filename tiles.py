class TileMap(object):
    def __init__(self, map, tile_w, tile_h):
        self.map = map
        self.tile_w = tile_w
        self.tile_h = tile_h

    def get_tile_w(self):
        return self.tile_w

    def get_tile_h(self):
        return self.tile_h


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
#
