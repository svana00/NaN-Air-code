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
    def __init__(self, plane_type_id, manufacturer, model, capacity):
        self.plane_type_id = plane_type_id
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity

class Destination():
    def __init__(self, dest_id, country, city, airport, flight_time, distance, contact, emergency_number):
        self.id = dest_id
        self.country = country
        self.city = city
        self.airport = airport
        self.flight_time = flight_time
        self.distance = distance
        self.contact = contact
        self.emergency_number = emergency_number

class Voyage():
    def __init__(self, departure_date, departure_time, departure_back_date, departure_back_time):
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.departure_back_date = departure_back_date
        self.departure_back_time = departure_back_time

class Flight():
    def __init__(self,flight_number):
        self,flight_number = flight_number