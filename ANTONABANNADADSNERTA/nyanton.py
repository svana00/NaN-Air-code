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

    def get_airplane_state(self, airplane_instance):
        """ gets an airplane and chosen time and returns the state of the chosen airplane """
        airplane_state = "BOOKED"
        chosen_airplane = airplane_instance
        voyages_list = self.ioAPI.load_all_voyages() # List of all voyages
        NOW = datetime.datetime.now()

        for voyage in voyages_list:
            voyage_plane = voyage.get_plane_id()

            departure_out = datetime.datetime.fromisoformat(voyage.get_departure_out())
            arrival_out = datetime.datetime.fromisoformat(voyage.get_arrival_out())
            departure_home = datetime.datetime.fromisoformat(voyage.get_departure_home())
            arrival_home = datetime.datetime.fromisoformat(voyage.get_arrival_home())

            if voyage_plane == chosen_airplane:

                if departure_out <= NOW and NOW <= arrival_out:
                    airplane_state = "in flight 1"
                    return airplane_state

                elif departure_home <= NOW and NOW <= arrival_home:
                    airplane_state = "in flight 2"
                    return airplane_state

                elif arrival_out <= NOW and NOW <= departure_home:
                    airplane_state = "in intermission" 
                    return airplane_state

                elif arrival_home < NOW or NOW < departure_out:
                    airplane_state = "IDLE"
                    return airplane_state

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


def overview_of_airplanes(self):
        #smá flipp
        counter = 0
        self.header("-", " ALL AIRPLANES ")
        airplane_info_list = self.llAPI.get_all_airplanes()

        chosen_date = input("Please enter date in the format (YYYY-MM-DD): ")
        chosen_time = input("Please enter the time in the format (HH:MM:00): ")

        for airplane in airplane_info_list:
            counter += 1
            airplane_name_str = airplane.get_name()
            airplane_id_str = airplane.get_plane_id()
            airplane_type_str =  airplane.get_type_id()    #2019-11-12T06:20:00
            date_and_time = chosen_date + "T" + chosen_time
            #chosen_time = datetime.datetime(2019,11,20,6,40,00)
            airplane_state_str = self.llAPI.get_airplane_state(airplane.get_plane_id(),date_and_time)
            print("{}. Name: {:<30} ID: {:<10} Type: {:<20} State: {:<15}".format(counter, airplane_name_str, airplane_id_str, airplane_type_str, airplane_state_str))
