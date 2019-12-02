class StaffMember():
    def __init__(self, staff_id, name, role, rank, licence, address, phone_number):
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.rank = rank
        self.licence = licence
        self.address = address
        self.phone_number = phone_number

class Airplane():
    def __init__(self, plane_id, type_id, seat_number):
        self.id = plane_id
        self.type = type_id
        self.seat_number = seat_number

class AirplaneType():
    def __init__(self, plane_type_id, manufacturer, model, capacity, empty_weight, max_takeoff_weight, unit_thrust, service_ceiling, length, height, wingspan):
        self.plane_type_id = plane_type_id
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.empty_weight = empty_weight
        self.max_takeoff_weight = max_takeoff_weight
        self.unit_thrust = unit_thrust
        self.service_ceiling = service_ceiling
        self.length = length
        self.height = height
        self.wingspan = wingspan

class Destination():
    def __init__(self, dest_id, city):
        self.id = dest_id
        self.city = city