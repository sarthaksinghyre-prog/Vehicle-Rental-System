import json
import os
from vehicle import Vehicle

FILE_NAME = "vehicles.json"


class DataManager:
    def __init__(self, file_name=FILE_NAME):
        self.file_name = file_name

    def save_vehicles(self, vehicles):
        data = []
        for v in vehicles:
            data.append(v.to_dict())

        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_vehicles(self):
        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [Vehicle.from_dict(x) for x in data]
        except (json.JSONDecodeError, KeyError, TypeError):
            return []

    def create_default_data(self):
        if os.path.exists(self.file_name):
            return

        vehicles = [
            Vehicle("V101", "Maruti Swift", "Car", 1800),
            Vehicle("V102", "Hyundai i20", "Car", 2000),
            Vehicle("V103", "Honda City", "Car", 2800),
            Vehicle("V104", "Royal Enfield", "Bike", 900),
            Vehicle("V105", "Honda Activa", "Scooter", 500)
        ]
        self.save_vehicles(vehicles)
