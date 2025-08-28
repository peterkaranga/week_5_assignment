class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing "

for v in [Car(), Plane(), Boat()]:
    print(v.move())
