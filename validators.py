def valid_vehicle_id(value):
    return bool(value.strip())


def valid_vehicle_name(value):
    return bool(value.strip())


def valid_vehicle_type(value):
    return bool(value.strip())


def valid_price(value):
    try:
        return float(value) > 0
    except ValueError:
        return False


def valid_days(value):
    try:
        return int(value) >= 1
    except ValueError:
        return False


def valid_phone(value):
    value = value.strip()
    return value.isdigit() and len(value) >= 10
