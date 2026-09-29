from vehicle import Vehicle
from vehicle_manager import VehicleManager
from rental_manager import RentalManager


class TestData:
    def __init__(self):
        self.saved = []

    def load_vehicles(self):
        return []

    def save_vehicles(self, vehicles):
        self.saved = vehicles


def test_vehicle():
    v = Vehicle("V1", "Test Car", "Car", 1000)
    assert v.vehicle_id == "V1"
    assert v.price == 1000
    assert v.available is True


def test_bill():
    data = TestData()
    vm = VehicleManager(data)
    v = Vehicle("V1", "Test Car", "Car", 1000)
    vm.vehicles.append(v)

    rm = RentalManager(vm)
    amount, discount, total = rm.calculate_bill(v, 3)
    assert amount == 3000
    assert discount == 150
    assert total == 2850


def test_return():
    data = TestData()
    vm = VehicleManager(data)
    v = Vehicle("V1", "Test Car", "Car", 1000)
    v.available = False
    vm.vehicles.append(v)

    rm = RentalManager(vm)
    ok, msg = rm.return_vehicle("V1")
    assert ok is True
    assert v.available is True


if __name__ == "__main__":
    test_vehicle()
    test_bill()
    test_return()
    print("All basic tests passed.")
