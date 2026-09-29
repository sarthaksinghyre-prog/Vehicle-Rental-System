class Vehicle:
    def __init__(self, vehicle_id, name, vehicle_type, price):
        self.vehicle_id = vehicle_id
        self.name = name
        self.vehicle_type = vehicle_type
        self.price = float(price)
        self.available = True

    def to_dict(self):
        return {
            "vehicle_id": self.vehicle_id,
            "name": self.name,
            "vehicle_type": self.vehicle_type,
            "price": self.price,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        v = cls(data["vehicle_id"], data["name"], data["vehicle_type"], data["price"])
        v.available = data.get("available", True)
        return v
