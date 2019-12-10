class Destination():
    def __init__(self, dest_id = "", country = "", city = "", airport = "", flight_time = "", distance = "", contact = "", emergency_number = "", flight_number_id = ""):
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
    
    #------- set functions -----------

    def set_new_contact(self, new_contact):
        self.__contact = new_contact
        
    def set_new_emergency_number(self, new_emergency_number):
        self.__emergency_number = new_emergency_number

    def instance_to_csv_string(self):
        csv_list = [self.__id, self.__country, self.__city, self.__airport, self.__flight_time, \
                    self.__distance, self.__contact, self.__emergency_number, self.__flight_number_id]
        
        csv_str = ",".join(csv_list)

        return csv_str 

    def __str__(self):
        my_str = ""
        my_str += "Destination ID: {}\n".format(self.__id)
        my_str += "Country: {}\n".format(self.__country)
        my_str += "City: {}\n".format(self.__city)
        my_str += "Airport: {}\n".format(self.__airport)
        my_str += "Flight time: {} hours\n".format(self.__flight_time)
        my_str += "Distance: {} km from Keflavik Airport\n".format(self.__distance)
        my_str += "Emergency contact: {}\n".format(self.__contact)
        my_str += "Phone number of emergency contact: {}\n".format(self.__emergency_number)
        my_str += "Flight number ID: {}\n".format(self.__flight_number_id)

        return my_str


