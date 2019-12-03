class StaffMember():
    def __init__(self, ssn, name, role, rank, licence, address, phone_number, email):
        self.__ssn = ssn
        self.__name = name
        self.role = role
        self.rank = rank
        self.licence = licence
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def get_ssn(self):
        return self.__ssn

    def get_name(self):
        return self.__name

    def __str__(self):
        return "{}".format(self.__name)
    
class Airplane():
    def __init__(self, name, plane_id, type_id, capacity):
        self.name = name
        self.id = plane_id
        self.type = type_id
        self.capacity = capacity

class AirplaneType():
    def __init__(self, plane_type_id, manufacturer, model, capacity):
        self.__plane_type_id = plane_type_id
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity

    def get_plane_type_id(self):
        return self.__plane_type_id

class Destination():
    def __init__(self, dest_id, country, city, airport, flight_time, distance, contact, emergency_number):
        self.__id = dest_id
        self.__country = country
        self.__city = city
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.contact = contact
        self.emergency_number = emergency_number

    def get_id(self):
        return self.__id

    def get_country(self):
        return self.__country

    def get_city(self):
        return self.__city

class Voyage():
    def __init__(self, departure_date, departure_time, departure_back_date, departure_back_time):
        self.__departure_date = departure_date
        self.__departure_time = departure_time
        self.__departure_back_date = departure_back_date
        self.__departure_back_time = departure_back_time

class Flight():
    def __init__(self,flight_number):
        self.__flight_number = flight_number