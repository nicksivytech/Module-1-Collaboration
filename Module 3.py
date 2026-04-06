#Nick Kintigh
#April 6th 2026
# Assignment: Module 3 Lab - Case Study: Lists, Functions, and Classes

# Vehicle superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Automobile inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # prints out the car info
    def display_info(self):
        print("\nHere is your car:")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# stores car as the vehicle type
vehicle_type = "car"

# asks the user for their car info
print("Enter your car information below:")
year = input("Year: ")
make = input("Make: ")
model = input("Model: ")
doors = input("Number of doors (2 or 4): ")
roof = input("Type of roof (solid or sun roof): ")

# creates the car object and displays it
my_car = Automobile(vehicle_type, year, make, model, doors, roof)
my_car.display_info()