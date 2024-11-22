# database.py

from vehicle import Vehicle

class Database:
    def __init__(self):
        self.car_spots = {i: None for i in range(1, 51)}  # 50 car spots
        self.bike_spots = {i: None for i in range(1, 21)}  # 20 bike spots

    def park_vehicle(self, vehicle_id, vehicle_type):
        vehicle = Vehicle(vehicle_id, vehicle_type)
        spots = self.car_spots if vehicle_type == "car" else self.bike_spots
        for spot_id, existing_vehicle in spots.items():
            if existing_vehicle is None:  # Spot is empty
                spots[spot_id] = vehicle
                return spot_id
        return None  # No available spot

    def remove_vehicle(self, vehicle_id):
        # Search in car spots
        for spot_id, vehicle in self.car_spots.items():
            if vehicle and vehicle.vehicle_id == vehicle_id:
                self.car_spots[spot_id] = None
                return spot_id, "car"
        # Search in bike spots
        for spot_id, vehicle in self.bike_spots.items():
            if vehicle and vehicle.vehicle_id == vehicle_id:
                self.bike_spots[spot_id] = None
                return spot_id, "bike"
        return None  # Vehicle not found

    def get_all_vehicles(self):
        vehicles = {}
        for spot_id, vehicle in self.car_spots.items():
            if vehicle:
                vehicles[vehicle.vehicle_id] = f"Car Spot {spot_id}"
        for spot_id, vehicle in self.bike_spots.items():
            if vehicle:
                vehicles[vehicle.vehicle_id] = f"Bike Spot {spot_id}"
        return vehicles
