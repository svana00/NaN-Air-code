class Voyage():
    def __init__(self, voyage_id, flight_num_out, flight_num_back, departure_out, arrival_out, departure_home, arrival_home, destination_id, plane_id = "", captain = "", copilot = "", fsm = "", fa1 = "", fa2 = "", fully_assigned = "False"):
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

    def instance_to_csv_string(self):
        csv_list = [self.__voyage_id, self.__flight_number_out, self.__flight_number_back, \
                    self.__departure_out, self.__arrival_out, self.__departure_home, self.__arrival_home, \
                    self.__destination_id, self.__plane_id, self.__captain, self.__copilot, \
                    self.__fsm, self.__fa1, self.__fa2, self.__fully_assigned]

        csv_str = ",".join(csv_list)

        return csv_str

    def __str__(self):
        my_str = ""
        my_str += "Voyage ID: {}\n".format(self.__voyage_id)
        my_str += "Flight number out: {}\n".format(self.__flight_number_out)
        my_str += "Flight number back: {}\n".format(self.__flight_number_back)
        my_str += "Departure out: {}\n".format(self.__departure_out)
        my_str += "Arrival out: {}\n".format(self.__arrival_out)
        my_str += "Departue home: {}\n".format(self.__departure_home)
        my_str += "Arrival home: {}\n".format(self.__arrival_home)
        my_str += "Destination ID: {}\n".format(self.__destination_id)
        my_str += "Plane ID: {}\n".format(self.__plane_id)
        my_str += "Captain: {}\n".format(self.__captain)
        my_str += "Co-pilot: {}\n".format(self.__copilot)
        my_str += "Flight service manager: {}\n".format(self.__fsm)
        my_str += "Flight attendant: {}\n".format(self.__fa1)
        my_str += "Flight attendant: {}\n".format(self.__fa2)
        my_str += "Voyage fully assigned: {}".format(self.is_fully_assigned())

        return my_str
