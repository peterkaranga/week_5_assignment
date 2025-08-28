class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"{self.name} from {self.origin} uses {self.power}"

class FlyingHero(Superhero):
    def __init__(self, name, power, origin, speed):
        super().__init__(name, power, origin)
        self.speed = speed

    def move(self):
        return f"{self.name} flies at {self.speed} km/h"
