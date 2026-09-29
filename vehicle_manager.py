class VehicleManager:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.vehicles = data_manager.load_vehicles()

    def save(self):
        self.data_manager.save_vehicles(self.vehicles)

    def find_vehicle(self, vehicle_id):
        vehicle_id = vehicle_id.strip().lower()
        for v in self.vehicles:
            if v.vehicle_id.lower() == vehicle_id:
                return v
        return None

    def add_vehicle(self, vehicle):
        if self.find_vehicle(vehicle.vehicle_id):
            return False, "Vehicle ID already exists."
        self.vehicles.append(vehicle)
        self.save()
        return True, "Vehicle added successfully."

    def remove_vehicle(self, vehicle_id):
        v = self.find_vehicle(vehicle_id)
        if v is None:
            return False, "Vehicle not found."
        if not v.available:
            return False, "A rented vehicle cannot be removed."
        self.vehicles.remove(v)
        self.save()
        return True, "Vehicle removed successfully."

    def search(self, text):
        text = text.strip().lower()
        if text == "":
            return self.vehicles

        found = []
        for v in self.vehicles:
            if (text in v.vehicle_id.lower() or
                    text in v.name.lower() or
                    text in v.vehicle_type.lower()):
                found.append(v)
        return found
