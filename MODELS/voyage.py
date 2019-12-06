class Voyage():
    def __init__(self, flight_num_out, flight_num_back, departure_date, departure_time, departure_back_date, departure_back_time, plane_id, dest_id):
        self.__flight_number_out = flight_num_out
        self.__flight_number_back = flight_num_back
        self.__departure_date = departure_date
        self.__departure_time = departure_time
        self.__departure_back_date = departure_back_date
        self.__departure_back_time = departure_back_time
        self.__plane_id = plane_id
        self.__destination_id = dest_id