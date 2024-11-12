class vehicle:
    def __init__(self, name, max_speed, milage):
        self.name= name
        self.max_speed= max_speed
        self.milage= milage
class bus(vehicle):
    pass
school_bus= bus("Volvo", 80, 12)
print(school_bus.name, school_bus.max_speed, school_bus.milage)