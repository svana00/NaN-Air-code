class Voyage():
    def __init__(self, voyage_id = "", flight_num_out = "", flight_num_back = "", departure_out = "", arrival_out = "", departure_home = "", arrival_home = "", destination_id = "", plane_id = "", captain = "", copilot = "", fsm = "", fa1 = "", fa2 = "", fully_assigned = "False"):
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
        self.__fully_assigned = fully_assigned

    #------- get functions -----------
    def get_voyage_id(self):
        return self.__voyage_id

    def get_flight_number_out(self):
        return self.__flight_number_out

    def get_flight_number_back(self):
        return self.__flight_number_back

    def get_departure_out(self):
        return self.__departure_out

    def get_arrival_out(self):
        return self.__arrival_out

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

    #------- set functions -----------

    def set_voyage_id(self, new_voyage_id):
        self.__voyage_id = new_voyage_id

    def set_flight_number_out(self, flight_number_out):
        self.__flight_number_out = flight_number_out
    
    def set_flight_number_back(self, flight_number_back):
        self.__flight_number_back = flight_number_back
    
    def set_departure_out(self, new_departure_out):
        self.__departure_out = new_departure_out
    
    def set_arrival_out(self, new_arrival_out):
        self.__arrival_out = new_arrival_out
    
    def set_departure_home(self, new_departure_home):
        self.__departure_home = new_departure_home

    def set_arrival_home(self, new_arrival_home):
        self.__arrival_home = new_arrival_home
    
    def set_dest_id(self, new_destination_id):
        self.__destination_id = new_destination_id

    def set_plane_id(self, plane_id):
        self.__plane_id = plane_id

    def set_cabin_crew(self, staff_list):
        self.__captain = staff_list[0]
        self.__copilot = staff_list[1]
        self.__fsm = staff_list[2]
        self.__fa1 = staff_list[3]
        self.__fa2 = staff_list[4]

    def set_fully_assigned(self):
        self.__fully_assigned = "True"

    def is_fully_assigned(self):
        return self.__fully_assigned

    def instance_to_csv_string(self):
        csv_list = [self.__voyage_id, self.__flight_number_out, self.__flight_number_back, \
                    self.__departure_out, self.__arrival_out, self.__departure_home, self.__arrival_home, \
                    self.__destination_id, self.__plane_id, self.__captain, self.__copilot, \
                    self.__fsm, self.__fa1, self.__fa2, self.__fully_assigned]

        csv_str = ",".join(csv_list)

        return csv_str

    #------- string function -----------
    def __str__(self):
        my_str = ""
        my_str += "VOYAGE ID: {}\n".format(self.__voyage_id)
        my_str += "FLIGHT NUMBER OUT: {}\n".format(self.__flight_number_out)
        my_str += "FLIGHT NUMBER BACK: {}\n".format(self.__flight_number_back)
        my_str += "DEPARTURE OUT: {}\n".format(self.__departure_out)
        my_str += "ARRIVAL OUT: {}\n".format(self.__arrival_out)
        my_str += "DEPARTURE HOME: {}\n".format(self.__departure_home)
        my_str += "ARRIVAL HOME: {}\n".format(self.__arrival_home)
        my_str += "DESTINATION ID: {}\n".format(self.__destination_id)
        my_str += "PLANE ID: {}\n".format(self.__plane_id)
        my_str += "CAPTAIN ID: {}\n".format(self.__captain)
        my_str += "CO-PILOT ID: {}\n".format(self.__copilot)
        my_str += "FLIGHT SERVICE MANAGER service manager ID: {}\n".format(self.__fsm)
        my_str += "FLIGHT ATTENDANT 1 ID: {}\n".format(self.__fa1)
        my_str += "FLIGHT ATTENDANT 2 ID: {}\n".format(self.__fa2)
        my_str += "VOYAGE FULLY ASSIGNED: {}".format(self.is_fully_assigned())

        return my_str
