class Galaxy(object):
    def __init__(self, systems):
        self.systems = systems

class System(object):
    def __init__(self, star, planets, index):
        self.star = star
        self.planets = planets
        self.index = index
        self.bodies = self.star + self.planets

    def get_index(self):
        return self.index

class Body(object):
    def __init__(self, image, index, type):
        self.index = index
        self.image = image
        self.type = type

    def get_index(self):
        return self.index

    def get_image(self):
        return self.image

class Star(Body):
    def __init__(self, image, index):
        self.index = index
        self.image = image
        self.type = "star"

class Planet(Body):
    def __init__(self, image, index):
        self.index = index # this is the index in the bodies array, not planets
        self.image = image
        self.type = "planet"
