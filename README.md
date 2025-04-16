# Base class
class Food:
    def __init__(self, name, calories):
        self.name = name
        self.__calories = calories  # Encapsulated attribute

    def get_calories(self):
        return self.__calories

    def set_calories(self, calories):
        if calories > 0:
            self.__calories = calories
        else:
            print("Calories must be positive!")

    def describe(self):
        return f"{self.name} contains {self.__calories} calories."


# Subclass
class FastFood(Food):
    def __init__(self, name, calories, is_spicy, preparation_time):
        super().__init__(name, calories)
        self.is_spicy = is_spicy
        self.preparation_time = preparation_time

    def make_order(self):
        spice_level = "Spicy" if self.is_spicy else "Not Spicy"
        return (f"Order placed: {self.name} ({spice_level}, "
                f"{self.preparation_time} mins to prepare).")

    def describe(self):
        # Overriding describe method
        base_description = super().describe()
        return base_description + f" Preparation time: {self.preparation_time} mins."


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
