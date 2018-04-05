class Galaxy(object):
    def __init__(self, systems):
        self.systems = systems

class System(object):
    def __init__(self, star, planets, index):
        self.star = star
        self.planets = planets
        self.index = index
        self.bodies = self.star + self.planets
        self.population = 0
        for i in self.planets:
            self.population += i.get_population()

    def get_index(self):
        return self.index

    def get_population(self):
        return self.population

    def update_population(self):
        self.population = 0
        for i in self.planets:
            self.population += i.get_population()

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
        self.system = None

    def set_system(self, system):
        self.system = system

class Planet(Body):
    def __init__(self, image, index):
        self.index = index # this is the index in the bodies array, not planets
        self.image = image
        self.type = "planet"
        self.population = 1000000

    def set_system(self, system):
        self.system = system

    def get_population(self):
        return self.population

    def add_population(self, value):
        self.population = self.population + value
