from MODELS.airplane import Airplane
import datetime
class AirplaneLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
    
    def get_all_airplanes(self):
        airplane_info_list = self.ioAPI.load_all_airplanes()
        return airplane_info_list

    def get_all_airplane_types(self):
        pass

    def get_airplane(self, plane_id):
        airplanes_list = self.ioAPI.load_all_airplanes()
        
        for airplane in airplanes_list:
            if airplane.get_plane_id() == plane_id:
                return airplane

    def make_airplane(self, new_airplane_list):
        airplane_str = ",".join(new_airplane_list)
        return self.ioAPI.create_new_airplane(airplane_str)
    
    def get_airplane_state(self, airplane_instance):
        #free_airplane_set = get_free_airplanes(airplane_instance):
        #instance_list = self.ioAPI.load_all_airplanes()

        voyages_list = self.ioAPI.load_all_voyages() # List of voyages
        airplane_state = "IDLE"
        NOW = datetime.datetime.now.isoformat()

        for voyage in voyages_list:

            voyage_plane = voyage.get_plane_id()

            departure1_str = voyage.get_departure_out()
            departure1_str_temp = datetime.datetime.fromisoformat(departure1_str)

            arrival1_str = voyage.get_arrival_out()
            arrival1_str_temp = datetime.datetime.fromisoformat(arrival1_str)

            departure2_str = voyage.get_departure_home()
            departure2_str_temp = datetime.datetime.fromisoformat(departure2_str)

            arrival2_str = voyage.get_arrival_home()
            arrival2_str_temp = datetime.datetime.fromisoformat(arrival2_str)

            if voyage_plane == airplane_instance.get_plane_id():
                if departure1_str_temp <= NOW <= arrival1_str_temp:
                    airplane_state = "in flight 1"
                elif departure2_str_temp <= NOW <= arrival2_str_temp:
                    airplane_state = "in flight 2"
                elif arrival1_str_temp < NOW < departure2_str_temp:
                    airplane_state = "in intermission" 
                else:
                    airplane_state = "booked to fly at {}".format(departure1_str_temp)

        return airplane_state

    def get_free_airplanes(self, departure_out_str, arrival_home_str):
        voyages_list = self.ioAPI.load_all_voyages() # List of voyages
        free_airplanes_set = set()

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
            if not overlap:
                airplane_id = voyage.get_plane_id()
                airplane = self.get_airplane(airplane_id)
                free_airplanes_set.add(airplane)

        return free_airplanes_set