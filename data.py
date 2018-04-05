class DataManager(object):

    def __init__(self):
        self.max_energy = 10000
        self.max_storage = 10000
        self.energy = 0
        self.storage = 0
        self.money = 10000
        self.price = 100

    def get_value(self, resource):
        return self.__dict__[resource]

    def set_value(self, resource, value):
        self.__dict__[resource] = value

    def add_value(self, resource, value):
        self.__dict__[resource] += value

    def get_object_value(self, obj, var, value):
        return obj.__dict__[var].value

    def update_data(self, build_manager):
        for _ in build_manager.spheres:
            if self.energy < self.max_energy:
                self.energy += 1
