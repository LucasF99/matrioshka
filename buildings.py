class Sphere(object):

    def __init__(self):
        self.energy_per_second = 20 # default eps

    def get_energy_per_second(self):
        return self.energy_per_second

class Mine(object):

    def __init__(self):
        pass

class BuildingManager(object):

    def __init__(self):
        self.spheres = []
        self.mines = []

    def add(self, build_type, build):
        self.__dict__[build_type].append(build)
