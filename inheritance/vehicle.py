class vehicle:
    def __init__(vehicletype):
        print(vehicletype)

class car(vehicle):
    def __init__(self):
        vehicle.__init__("car")

print(issubclass(car,vehicle))
        
        