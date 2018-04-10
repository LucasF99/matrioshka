import textures
import math

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

    def get_energy_level(self):
        return self.energy_level

    def set_energy_level(self, value):
        self.energy_level = value

    def add_energy_level(self, value):
        self.energy_level += value

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

class Planet(Body):
    def __init__(self, image, index, name):
        self.index = index # this is the index in the bodies array, not planets
        self.image = image
        self.radius = image.get_width()/2
        self.type = "planet"
        self.name = name
        self.population = 1000000
        self.buildings = []
        self.building_coords = []

        for i in range(8):
            self.buildings.append(0)
            self.building_coords.append(None)

        self.building_coords[0] = (math.cos((3/4)*math.pi)/2, math.sin((3/4)*math.pi)/2)
        self.building_coords[1] = (math.cos((1/4)*math.pi)/2, math.sin((1/4)*math.pi)/2)
        self.building_coords[2] = (math.cos((5/4)*math.pi)/2, math.sin((5/4)*math.pi)/2)
        self.building_coords[3] = (math.cos((7/4)*math.pi)/2, math.sin((7/4)*math.pi)/2)
        self.building_coords[4] = (math.cos((3/4)*math.pi)*1.5, math.sin((3/4)*math.pi)*1.5)
        self.building_coords[5] = (math.cos((1/4)*math.pi)*1.5, math.sin((1/4)*math.pi)*1.5)
        self.building_coords[6] = (math.cos((5/4)*math.pi)*1.5, math.sin((5/4)*math.pi)*1.5)
        self.building_coords[7] = (math.cos((7/4)*math.pi)*1.5, math.sin((7/4)*math.pi)*1.5)

    def check_mouse(self, pos, radius): # returns [x, y, buildings array index]
        x = pos[0]
        y = pos[1]

        if math.hypot(x, y) <= radius:
            if y > 0:
                if x < 0:
                    return [math.cos((3/4)*math.pi)*radius/2, math.sin((3/4)*math.pi)*radius/2, 0]
                if x >= 0:
                    return [math.cos((1/4)*math.pi)*radius/2, math.sin((1/4)*math.pi)*radius/2, 1]
            elif y <= 0:
                if x < 0:
                    return [math.cos((5/4)*math.pi)*radius/2, math.sin((5/4)*math.pi)*radius/2, 2]
                if x >= 0:
                    return [math.cos((7/4)*math.pi)*radius/2, math.sin((7/4)*math.pi)*radius/2, 3]
        elif abs(x) <= 1.5*radius and abs(y) <= 1.5*radius:
            if y > 0:
                if x < 0:
                    return [math.cos((3/4)*math.pi)*1.5*radius, math.sin((3/4)*math.pi)*1.5*radius, 4]
                if x >= 0:
                    return [math.cos((1/4)*math.pi)*1.5*radius, math.sin((1/4)*math.pi)*1.5*radius, 5]
            elif y <= 0:
                if x < 0:
                    return [math.cos((5/4)*math.pi)*1.5*radius, math.sin((5/4)*math.pi)*1.5*radius, 6]
                if x >= 0:
                    return [math.cos((7/4)*math.pi)*1.5*radius, math.sin((7/4)*math.pi)*1.5*radius, 7]
        else:
            return [None, None, None]

    def set_system(self, system):
        self.system = system

    def get_population(self):
        return self.population

    def add_population(self, value):
        self.population = self.population + value
