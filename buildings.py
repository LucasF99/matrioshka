class Sphere(object):

    def __init__(self):
        pass
    
class BuildingManager(object):

    def __init__(self):
        self.spheres = []

    def add(self, build_type, build):
        self.__dict__[build_type].append(build)
