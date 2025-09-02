# Polymorphism with Vehicles

class Vehicle:
    def move(self):
        pass  # Placeholder method

class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚤 The boat is sailing on the water.")

# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Same method name, different behavior
