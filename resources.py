class ResourceManager(object):

    def __init__(self):
        self.max_energy = 100
        self.max_storage = 100
        self.energy = 0
        self.storage = 0

    def get_resource(self, resource):
        return self.__dict__[resource]

    def set_resource(self, resource, value):
        self.__dict__[resource] = value

    def add_resource(self, resource, value):
        self.__dict__[resource] += value

    def update_resources(self, build_manager):
        for _ in build_manager.spheres:
            if self.energy < self.max_energy:
                self.energy += 1
