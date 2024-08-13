"""
Task 1: Vehicle Registration System

- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

- Code Example: Provide a basic structure for the Vehicle class without methods.

    class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
            
- Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a demonstration script showing the creation of Vehicle objects and updating their owners.
"""

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_details(self):
        print(f"Registration Number: {self.registration_number}, Type: {self.type}, Owner: {self.owner}")

vehicles = {}

def display_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_details()

def create_vehicle(reg_num, type, owner):
    vehicles[reg_num] = Vehicle(reg_num, type, owner)

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Updated owner for vehicle {reg_num}.")
    else:
        print("Vehicle not found.")


create_vehicle('ABC-123', 'Truck', 'Mary')
create_vehicle('DEF-456', 'Sedan', 'Kevin')
display_vehicles()

update_vehicle_owner('ABC-123', 'Taylor')
display_vehicles()