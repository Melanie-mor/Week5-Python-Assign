# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

# Subclasses with polymorphic move()
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each will call its own version of move()