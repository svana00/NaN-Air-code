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
        pass

    def get_airplane(self, plane_id):
        airplanes_list = self.ioAPI.load_all_airplanes()
        
        for airplane in airplanes_list:
            if airplane.get_plane_id() == plane_id:
                return airplane

    def make_airplane(self, new_airplane_list):
        airplane_str = ",".join(new_airplane_list)
        return self.ioAPI.create_new_airplane(airplane_str)


    def gets_int_list_and_returns_datetime_format(self, int_list):
        year = int_list[0]
        month = int_list[1]
        day = int_list[2]
        hour = int_list[3]
        minute = int_list[4]
        return datetime.datetime(year, month, day, hour, minute)

    def gets_instance_attribute_and_returns_int_list(self, voyage_attribute):
        temp_attribute = voyage_attribute
        temp_attribute_str = temp_attribute.replace("T","-").replace(":", "-")
        temp_attribute_str_list = temp_attribute_str.split("-")
        attribute_int_list = [int(i) for i in temp_attribute_str_list]
        return attribute_int_list
    
    def get_airplane_state(self, airplane_instance, chosen_time_and_date):
        """ gets an airplane and chosen time and returns the state of the chosen airplane """

        chosen_airplane = airplane_instance
        voyages_list = self.ioAPI.load_all_voyages() # List of all voyages
        airplane_state = "IDLE" # initializes the airplane state at IDLE
        NOW = datetime.datetime.fromisoformat(chosen_time_and_date)

        for voyage in voyages_list:
            voyage_plane = voyage.get_plane_id()

            departure1_int_list = self.gets_instance_attribute_and_returns_int_list(voyage.get_departure_out())
            departure1_date = self.gets_int_list_and_returns_datetime_format(departure1_int_list)

            arrival1_int_list = self.gets_instance_attribute_and_returns_int_list(voyage.get_arrival_out())
            arrival1_date = self.gets_int_list_and_returns_datetime_format(arrival1_int_list)

            departure2_int_list = self.gets_instance_attribute_and_returns_int_list(voyage.get_departure_home())
            departure2_date = self.gets_int_list_and_returns_datetime_format(departure2_int_list)

            arrival2_int_list = self.gets_instance_attribute_and_returns_int_list(voyage.get_arrival_home())
            arrival2_date = self.gets_int_list_and_returns_datetime_format(arrival2_int_list)

            if voyage_plane == chosen_airplane:

                if departure1_date <= NOW <= arrival1_date:
                    airplane_state = "in flight 1"
                elif departure2_date <= NOW <= arrival2_date:
                    airplane_state = "in flight 2"
                elif arrival1_date < NOW < departure2_date:
                    airplane_state = "in intermission" 
                else:
                    airplane_state = "booked to fly at {}".format(voyage.get_departure_out())

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