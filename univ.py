import textures

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
    def __init__(self, image, index, type, name):
        self.index = index
        self.image = image
        self.type = type
        self.name = name

    def get_index(self):
        return self.index

    def get_image(self):
        return self.image

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

class Star(Body):
    def __init__(self, image, index, name):
        self.index = index
        self.image = image
        self.type = "star"
        self.system = None
        self.name = name
        self.energy_level = 0

        self.upgrade_img = textures.img[1]

    def set_system(self, system):
        self.system = system

    def get_energy_level(self):
        return self.energy_level

    def set_energy_level(self, value):
        print("set")
        self.energy_value = value

    def add_energy_level(self, value):
        self.energy_level += value

class Planet(Body):
    def __init__(self, image, index, name):
        self.index = index # this is the index in the bodies array, not planets
        self.image = image
        self.type = "planet"
        self.name = name
        self.population = 1000000

    def set_system(self, system):
        self.system = system

    def get_population(self):
        return self.population

    def add_population(self, value):
        self.population = self.population + value
