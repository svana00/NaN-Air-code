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

    #------- get functions -----------
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
    def set_id(self, new_id):
        self.__id = new_id

    def set_country(self, new_country):
        self.__country = new_country

    def set_city(self, new_city):
        self.__city = new_city

    def set_airport(self, new_airport):
        self.__airport = new_airport
    
    def set_flight_time(self, new_flight_time):
        self.__flight_time = new_flight_time

    def set_distance(self, new_distance):
        self.__distance = new_distance

    def set_new_contact(self, new_contact):
        self.__contact = new_contact
        
    def set_new_emergency_number(self, new_emergency_number):
        self.__emergency_number = new_emergency_number

    def instance_to_csv_string(self):
        ''' Makes a csv string from destination instance '''
        csv_list = [self.__id, self.__city, self.__country,self.__airport, self.__flight_time, \
                    self.__distance, self.__contact, self.__emergency_number, self.__flight_number_id]
        
        csv_str = ",".join(csv_list)

        return csv_str 

    #------- string function -----------
    def __str__(self):
        my_str = ""
        my_str += "DESTINATION ID: {}\n".format(self.__id)
        my_str += "COUNTRY: {}\n".format(self.__country)
        my_str += "CITY: {}\n".format(self.__city)
        my_str += "AIRPORT: {}\n".format(self.__airport)
        my_str += "FLIGHT TIME: {} hours\n".format(self.__flight_time)
        my_str += "DISTANCE FROM KEF: {} km\n".format(self.__distance)
        my_str += "EMERGENCY CONTACT: {}\n".format(self.__contact)
        my_str += "PHONE NUMBER OF EMERGENCY CONTACT: {}\n".format(self.__emergency_number)
        my_str += "FLIGHT NUMBER ID: {}\n".format(self.__flight_number_id)

        return my_str