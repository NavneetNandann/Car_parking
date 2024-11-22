# parking_lot.py

class ParkingLot:
    def __init__(self, db):
        self.db = db

    def park_vehicle(self, vehicle_id, vehicle_type):
        return self.db.park_vehicle(vehicle_id, vehicle_type)

    def remove_vehicle(self, vehicle_id):
        return self.db.remove_vehicle(vehicle_id)

    def available_spots(self, vehicle_type):
        spots = self.db.car_spots if vehicle_type == "car" else self.db.bike_spots
        return sum(1 for spot in spots.values() if spot is None)
