class DataManager(object):

    def __init__(self):
        self.max_energy = 10000
        self.max_storage = 10000
        self.energy = 0
        self.storage = 0
        self.money = 10000
        self.price = 100
        self.clock = 0
        self.tick_time = 500 # time between data updates in milliseconds

    def get_value(self, resource):
        return self.__dict__[resource]

    def set_value(self, resource, value):
        self.__dict__[resource] = value

    def add_value(self, resource, value):
        self.__dict__[resource] += value

    def get_object_value(self, obj, var, value):
        return obj.__dict__[var].value

    def update_data(self, build_manager, time):
        if self.clock >= self.tick_time:
            added_energy = 0
            for i in build_manager.spheres:
                added_energy += i.get_energy_per_second()/(1000/self.tick_time)
            if self.energy < self.max_energy:
                self.energy += added_energy

            self.clock = self.clock - self.tick_time
        self.clock += time
