import datetime
from datetime import date
class AirplaneLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
    
    def get_all_airplanes(self):
        airplane_info_list = self.ioAPI.load_all_airplanes()
        return airplane_info_list

    def get_all_airplane_types(self):
        ''' Returns a list of all airplane types '''

        airplane_types_list = self.ioAPI.load_airplane_types()
        airplane_types_info_list = []

        for airplane_type in airplane_types_list:
            airplane_type_id = airplane_type.get_plane_type_id()
            airplane_types_info_list.append(airplane_type_id)

        return airplane_types_info_list

    def get_airplane(self, plane_id):
        ''' Filters out a single airplane using its ID '''
        airplanes_list = self.ioAPI.load_all_airplanes()
        
        for airplane in airplanes_list:
            if airplane.get_plane_id() == plane_id:
                return airplane

    def make_airplane(self, new_airplane):
        ''' Sends a new instance of an airplane down to the database for storing '''

        return self.ioAPI.store_new_airplane(new_airplane)

    def get_airplane_state(self, airplane_id, chosen_time_and_date):
        ''' Gets an airplane and chosen time and returns the state of the chosen airplane '''

        chosen_airplane = airplane_id
        voyages_list = self.ioAPI.load_all_voyages() # List of all voyages
        airplane_state = "IDLE" # initializes the airplane state at IDLE
        NOW = datetime.datetime.fromisoformat(chosen_time_and_date) # Makes the input date and time from user a datetime object

        for voyage in voyages_list:
            voyage_plane = voyage.get_plane_id()

            # Gets all timestamps from a single voyage including when it will be available again...
            # ... which is an hour after it arrives back to Keflavik.
            departure_out = datetime.datetime.fromisoformat(voyage.get_departure_out())
            arrival_out = datetime.datetime.fromisoformat(voyage.get_arrival_out())
            departure_home = datetime.datetime.fromisoformat(voyage.get_departure_home())
            arrival_home = datetime.datetime.fromisoformat(voyage.get_arrival_home())
            available = arrival_home + datetime.timedelta(hours = 1)
            
        # If the chosen airplane matches the airplane of the voyage and the chosen datetime object is within the timefram of the voyage..
        # .. The loop breaks and the state is updated.
            if voyage_plane == chosen_airplane:
                if departure_out <= NOW and arrival_home > NOW:
                    break 
        # If no matches are found, the plane is idle
        else:
            return airplane_state
            
        # If the airplane is on its way from KEF:
        if departure_out <= NOW and NOW <= arrival_out:
            airplane_state = "Flight {} is on its way to {} and will be available again on: {}".format(voyage.get_flight_number_out(), voyage.get_dest_id(), available)
        # If the airplane is in intermission:
        elif departure_home <= NOW and NOW <= arrival_home:
            airplane_state = "Flight {} is on its way to KEF and will be available again on: {}".format(voyage.get_flight_number_back(), available)
        # If the airplane is on its way back to KEF
        elif arrival_out <= NOW and NOW <= departure_home:
            airplane_state = "IN INTERMISSION" 

        return airplane_state

    def get_free_airplanes(self, departure_out_str, arrival_home_str):
        ''' Returns a list of all the plane ID's of the planes that are available '''

        voyages_list = self.ioAPI.load_all_voyages() # List of voyages
        airplanes_list = self.get_all_airplanes()
        plane_id_list = []
        
        for airplane in airplanes_list:
            plane_id = airplane.get_plane_id()
            plane_id_list.append(plane_id)
        
        # Converts to datetime objects
        departure_out = datetime.datetime.fromisoformat(departure_out_str)
        arrival_home = datetime.datetime.fromisoformat(arrival_home_str)

        # Checks if the chosen time for the new voyage overlaps with any existing voyage
        # If so, the corresponding plane ID is removed from the list of all plane ID's leaving available Airplanes
        for voyage in voyages_list:
            departure_out_str = voyage.get_departure_out()
            departure_out_temp = datetime.datetime.fromisoformat(departure_out_str)

            arrival_home_str = voyage.get_arrival_home()
            arrival_home_temp = datetime.datetime.fromisoformat(arrival_home_str)

            overlap = (departure_out < arrival_home_temp and departure_out_temp < arrival_home)

            # startDate1 < endDate2 and startDate2 < endDate1 = overlap
            if overlap:
                plane_id = voyage.get_plane_id()
                if plane_id in plane_id_list:
                    plane_id_list.remove(plane_id)

        return plane_id_list