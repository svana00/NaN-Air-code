class Voyage():
    def __init__(self, voyage_id, flight_num_out, flight_num_back, departure_out, arrival_out, departure_home, arrival_home, destination_id, plane_id = "", captain = "", copilot = "", fsm = "", fa1 = "", fa2 = ""):
        self.__voyage_id = voyage_id
        self.__flight_number_out = flight_num_out
        self.__flight_number_back = flight_num_back
        self.__departure_out = departure_out
        self.__arrival_out = arrival_out
        self.__departure_home = departure_home
        self.__arrival_home = arrival_home
        self.__destination_id = destination_id
        self.__plane_id = plane_id
        self.__captain = captain
        self.__copilot = copilot
        self.__fsm = fsm
        self.__fa1 = fa1
        self.__fa2 = fa2

    def set_cabin_crew(self, staff_list):
        self.__captain = staff_list[0]
        self.__copilot = staff_list[1]
        self.__fsm = staff_list[2]
        self.__fa1 = staff_list[3]
        self.__fa2 = staff_list[4]

    def get_voyage_id(self):
        return self.__voyage_id

    def get_flight_number_out(self):
        return self.__flight_number_out

    def get_flight_number_back(self):
        return self.__flight_number_back

    def get_departure_out(self):
        return self.__departure_out

    def get_arrival_out(self):
        return self.__arrival_home

    def get_departure_home(self):
        return self.__departure_home

    def get_arrival_home(self):
        return self.__arrival_home

    def get_plane_id(self):
        return self.__plane_id

    def get_dest_id(self):
        return self.__destination_id

    def get_cabin_crew(self):
        return [self.__captain, self.__copilot, self.__fsm, self.__fa1, self.__fa2]

    def __str__(self):
        my_str = ""
        my_str += "Voyage ID: {}".format(self.__voyage_id)
        my_str += "Flight number out: {}".format(self.__flight_number_out)
        my_str += "Flight number back: {}".format(self.__flight_number_back)
        my_str += "Departure out: {}".format(self.__departure_out)
        my_str += "Arrival out: {}".format(self.__arrival_out)
        my_str += "Departue home: {}".format(self.__departure_home)
        my_str += "Arrival home: {}".format(self.__arrival_home)
        my_str += "Destination ID: {}".format(self.__destination_id)
        my_str += "Plane ID: {}".format(self.__plane_id)
        my_str += "Captain: {}".format(self.__captain)
        my_str += "Co-pilot: {}".format(self.__copilot)
        my_str += "Flight service manager: {}".format(self.__fsm)
        my_str += "Flight attendant: {}".format(self.__fa1)
        my_str += "Flight attendant: {}".format(self.__fa2)

        return my_str