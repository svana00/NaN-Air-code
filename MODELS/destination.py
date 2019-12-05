class Destination():
    def __init__(self, dest_id, country, city, airport, flight_time, distance, contact, emergency_number):
        self.__id = dest_id
        self.__country = country
        self.__city = city
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__contact = contact
        self.__emergency_number = emergency_number

    def get_id(self):
        return self.__id

    def get_country(self):
        return self.__country

    def get_city(self):
        return self.__city

    def get_airport(self):
        return self.__airport
    
    def get_flight_time(self):
        return self.__flight_time

    def get_distance(self):
        return self.__distance
    
    def get_contact(self):
        return self.__contact

    def get_emergency_number(self):
        return self.__emergency_number