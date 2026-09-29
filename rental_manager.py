class RentalManager:
    def __init__(self, vehicle_manager):
        self.vehicle_manager = vehicle_manager

    def calculate_bill(self, vehicle, days):
        amount = vehicle.price * days

        if days >= 7:
            discount = amount * 0.10
        elif days >= 3:
            discount = amount * 0.05
        else:
            discount = 0

        return amount, discount, amount - discount

    def rent_vehicle(self, vehicle_id, customer, phone, days):
        vehicle = self.vehicle_manager.find_vehicle(vehicle_id)

        if vehicle is None:
            return False, "Vehicle not found.", None
        if not vehicle.available:
            return False, "Vehicle is already rented.", None
        if not customer.strip() or not phone.strip():
            return False, "Customer name and phone are required.", None
        if days < 1:
            return False, "Number of days must be at least 1.", None

        amount, discount, total = self.calculate_bill(vehicle, days)
        vehicle.available = False
        self.vehicle_manager.save()

        bill = {
            "customer": customer.strip(),
            "phone": phone.strip(),
            "vehicle": vehicle.name,
            "vehicle_id": vehicle.vehicle_id,
            "days": days,
            "price_per_day": vehicle.price,
            "amount": amount,
            "discount": discount,
            "total": total
        }
        return True, "Rental completed successfully.", bill

    def return_vehicle(self, vehicle_id):
        vehicle = self.vehicle_manager.find_vehicle(vehicle_id)
        if vehicle is None:
            return False, "Vehicle not found."
        if vehicle.available:
            return False, "Vehicle is already available."

        vehicle.available = True
        self.vehicle_manager.save()
        return True, vehicle.name + " returned successfully."
