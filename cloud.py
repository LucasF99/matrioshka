class Cloud(object):
    def __init__(self, worlds):
        self.worlds = worlds

class World(object):
    def __init__(self, tile_map):
        self.tile_map = tile_map

    def set_tile_map(self, tile_map):
        self.tile_map = tile_map

    def get_tile_map(self):
        return self.tile_map
