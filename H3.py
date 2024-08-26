'''3. Implement a Parking Lot System
Requirements:
Implement classes for Vehicle, Car, Bike, ParkingSpot, ParkingLot.
Vehicle should be a base class with attributes like license_plate and vehicle_type.
Car and Bike should inherit from Vehicle.
ParkingSpot should have attributes like spot_id, is_available, and vehicle.
ParkingLot should manage multiple parking spots and provide methods to park and retrieve vehicles, and to get the status of the parking lot.
'''
class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Car")

class Bike(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Bike")

class ParkingSpot:
    def __init__(self, spot_id, is_available=True, vehicle=None):
        self.spot_id = spot_id
        self.is_available = is_available
        self.vehicle = vehicle

    def park_vehicle(self, vehicle):
        if self.is_available:
            self.vehicle = vehicle
            self.is_available = False
            print(f"Vehicle {vehicle.license_plate} parked in spot {self.spot_id}.")
        else:
            print(f"Spot {self.spot_id} is already occupied.")

    def remove_vehicle(self):
        if not self.is_available:
            print(f"Vehicle {self.vehicle.license_plate} removed from spot {self.spot_id}.")
            self.vehicle = None
            self.is_available = True
        else:
            print(f"Spot {self.spot_id} is already empty.")

class ParkingLot:
    def __init__(self, num_spots):
        self.spots = [ParkingSpot(spot_id) for spot_id in range(num_spots)]

    def park(self, vehicle):
        for spot in self.spots:
            if spot.is_available:
                spot.park_vehicle(vehicle)
                return
        print("No available spots for parking.")

    def retrieve(self, license_plate):
        for spot in self.spots:
            if spot.vehicle and spot.vehicle.license_plate == license_plate:
                spot.remove_vehicle()
                return
        print(f"Vehicle with license plate {license_plate} not found.")

    def status(self):
        for spot in self.spots:
            if spot.is_available:
                print(f"Spot {spot.spot_id} is available.")
            else:
                print(f"Spot {spot.spot_id} is occupied by vehicle {spot.vehicle.license_plate}.")

# Example usage
parking_lot = ParkingLot(5)

Kushaq = Car(1234)
Creta = Car(4567)
HD = Bike(9101)

parking_lot.park(Kushaq)
parking_lot.park(Creta)
parking_lot.park(HD)

parking_lot.status()

parking_lot.retrieve(1234)
parking_lot.status()
