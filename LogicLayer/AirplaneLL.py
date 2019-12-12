from MODELS.airplane import Airplane
import datetime
from datetime import date
class AirplaneLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
    
    def get_all_airplanes(self):
        airplane_info_list = self.ioAPI.load_all_airplanes()
        return airplane_info_list

    def get_all_airplane_types(self):
        ''' Returns a list of all instances of airplane types '''

        airplane_types_list = self.ioAPI.load_airplane_types()
        airplane_types_info_list = []

        for airplane_type in airplane_types_list:
            airplane_type_id = airplane_type.get_plane_type_id()
            airplane_types_info_list.append(airplane_type_id)

        return airplane_types_info_list

    def get_airplane(self, plane_id):
        airplanes_list = self.ioAPI.load_all_airplanes()
        
        for airplane in airplanes_list:
            if airplane.get_plane_id() == plane_id:
                return airplane

    def make_airplane(self, new_airplane_list):
        airplane_str = ",".join(new_airplane_list)
        return self.ioAPI.create_new_airplane(airplane_str)
    
    def get_airplane_state(self, airplane_instance, chosen_time_and_date):
        """ gets an airplane and chosen time and returns the state of the chosen airplane """

        chosen_airplane = airplane_instance
        voyages_list = self.ioAPI.load_all_voyages() # List of all voyages
        airplane_state = "IDLE" # initializes the airplane state at IDLE
        NOW = datetime.datetime.fromisoformat(chosen_time_and_date)
        #airplane_state_list = []
        for voyage in voyages_list:
            voyage_plane = voyage.get_plane_id()

            departure_out = datetime.datetime.fromisoformat(voyage.get_departure_out())
            arrival_out = datetime.datetime.fromisoformat(voyage.get_arrival_out())
            departure_home = datetime.datetime.fromisoformat(voyage.get_departure_home())
            arrival_home = datetime.datetime.fromisoformat(voyage.get_arrival_home())
            available = arrival_home + datetime.timedelta(hours = 1)
            
            if voyage_plane == chosen_airplane:
                if departure_out <= NOW and arrival_home > NOW:
                    break 
        else:
            return airplane_state
            
        if departure_out <= NOW and NOW <= arrival_out:
            airplane_state = "Flight nr. {} going to {}".format(voyage.get_voyage_id(), voyage.get_departure_out())
        elif departure_home <= NOW and NOW <= arrival_home:
            airplane_state = "Flight nr. {} going to KEF and will again be available: {}".format(voyage.get_voyage_id(), available)
        elif arrival_out <= NOW and NOW <= departure_home:
            airplane_state = "IN ITERMISSION" 
            #airplane_state_list.append(airplane_state)

        return airplane_state

    def get_free_airplanes(self, departure_out_str, arrival_home_str):
        voyages_list = self.ioAPI.load_all_voyages() # List of voyages
        airplanes_list = self.get_all_airplanes()
        plane_id_list = []
        
        for airplane in airplanes_list:
            plane_id = airplane.get_plane_id()
            plane_id_list.append(plane_id)
        
        departure_out = datetime.datetime.fromisoformat(departure_out_str)
        arrival_home = datetime.datetime.fromisoformat(arrival_home_str)

        # Get all aurplanes that are not on a voyage at time of voyage
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