class Cloud(object):
    def __init__(self, worlds):
        self.worlds = worlds

class World(object):
    def __init__(self, tilemap):
        self.tilemap = tilemap

    def set_tilemap(self, tilemap):
        self.tilemap = tilemap

    def get_tilemap(self):
        return self.tilemap()
