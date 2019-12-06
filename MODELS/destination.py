class Destination():
    def __init__(self, dest_id, country, city, airport, flight_time, distance, contact, emergency_number, flight_number_id):
        self.__id = dest_id
        self.__country = country
        self.__city = city
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__contact = contact
        self.__emergency_number = emergency_number
        self.__flight_number_id = flight_number_id

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
    
    def get_flight_number_id(self):
        return self.__flight_number_id

    def __string__(self):
        my_str = "Destination id: {}".format(self.__id)
        my_str += "\nCountry: {}".format(self.__country)
        my_str += "\nCity: {}".format(self.__city)
        my_str += "\nAirport: {}".format(self.__airport)
        my_str += "\nFlight time: {} hours".format(self.__flight_time)
        my_str += "\nDistance: {} km".format(self.__distance)
        my_str += "\nEmergency contact: {}".format(self.__contact)
        my_str += "\nPhone number of emergency contact: {}".format(self.__emergency_number)