class DataManager(object):

    def __init__(self):
        self.max_energy = 10000
        self.max_storage = 10000
        self.energy = 0
        self.storage = 0

    def get_value(self, resource):
        return self.__dict__[resource]

    def set_value(self, resource, value):
        self.__dict__[resource] = value

    def add_value(self, resource, value):
        self.__dict__[resource] += value

    def update_data(self, build_manager):
        for _ in build_manager.spheres:
            if self.energy < self.max_energy:
                self.energy += 1
