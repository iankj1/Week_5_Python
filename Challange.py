# Parent class
class Vehicle:
    def move(self):
        # Generic move (will be overridden by child classes)
        print("The vehicle is moving...")

# Child classes overriding move()
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚢 The boat is sailing on the water.")

class Bicycle(Vehicle):
    def move(self):
        print("🚴 The bicycle is pedaling forward.")


# ---- Testing polymorphism ----
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()   # each class has its own version of move()
