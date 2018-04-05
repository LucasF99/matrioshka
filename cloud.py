class Cloud(object):
    def __init__(self, worlds):
        self.worlds = worlds
        self.population = 0

    def get_population(self):
        return self.population

    def add_population(self, value):
        self.population = self.population + value

class World(object):
    def __init__(self, tile_map):
        self.tile_map = tile_map

    def set_tile_map(self, tile_map):
        self.tile_map = tile_map

    def get_tile_map(self):
        return self.tile_map
