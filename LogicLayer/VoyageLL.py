from datetime import datetime, timedelta
from MODELS.voyage import Voyage
class VoyageLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI

    def get_voyage_info(self, voyage_id):
        voyage_list = self.ioAPI.load_all_voyages()
        for voyage in voyage_list:
            if voyage.get_voyage_id() == voyage_id:
                return voyage

    def assign_voyage_staff(self):
        pass

    def get_all_voyages(self):

        voyage_list = self.ioAPI.load_all_voyages()
        return voyage_list

    def get_voyages_by_week(self, start_of_desired_week_str):
        voyages_list = self.ioAPI.load_all_voyages()
        voyages_in_week_list = []

        start_of_desired_week = datetime.datetime.fromisoformat(start_of_desired_week_str).date()
        end_of_desired_week = datetime.datetime.fromisoformat(start_of_desired_week_str) + datetime.timedelta(days = 6)

        for voyage in voyages_list:
            temp_date = datetime.datetime.fromisoformat(voyage.get_departure_out(), voyage.get_dest_id()).date()
            if temp_date >= start_of_desired_week and temp_date <= end_of_desired_week:
                voyages_in_week_list.append(voyage)

        return voyages_in_week_list

    def get_voyages_by_date(self, desired_date_str):
        
        voyages_list = self.ioAPI.load_all_voyages()
        target_date = datetime.date.fromisoformat(desired_date_str)
        voyages_on_date_list = []

        for voyage in voyages_list:
            departure_date = datetime.datetime.fromisoformat(voyage.get_departure_out()).date
            if target_date == departure_date:
                voyages_on_date_list.append(voyage)

        return voyages_on_date_list

    def get_non_assigned_voyages(self):
        pass

    def check_voyages_state(self):
        pass

    def make_voyage(self, voyage_info_list):
        voyages_list = self.ioAPI.load_all_voyages()

        # Create voyage id
        voyage_id_int = len(voyages_list) + 1

        if voyage_id_int < 10:
            voyage_id_str = "0" + "{}".format(voyage_id_int)

        elif voyage_id_int < 100:
            voyage_id_str = "0" + "{}".format(voyage_id_int)

        elif voyage_id_int < 100:
            voyage_id_str = "0" + "{}".format(voyage_id_int)
                
        # Create flight number for each flight
        target_id = voyage_info_list[0]
        destinations_list = self.ioAPI.load_all_dest_from_file()

        for destination in destinations_list:
            destination_id = destination.get_id()
            if target_id == destination_id:
                flight_time = destination.get_flight_time()
                dest_flight_number_id  = destination.get_flight_number_id()

        target_date = voyage_info_list[1]
        counter = 0

        for voyage in voyages_list: 
            dest_id = voyage.get_dest_id()
            departure_out_date = voyage.get_departure_out()
            date = datetime.fromisoformat(departure_out_date).date()
            date = str(date)
            if dest_id == target_id and date == target_date:
                counter += 1

        flight_number_out_str = "NA" + str(dest_flight_number_id) + str(counter * 2)
        flight_number_back_str = "NA" + str(dest_flight_number_id) + str(counter * 2 + 1)

        departure_out_str = ("T").join(voyage_info_list[1:]) # Departure out

        departure_out = datetime.fromisoformat(departure_out_str)
        arrival_out = departure_out + timedelta(hours = int(flight_time))
        arrival_out_str = arrival_out.isoformat()

        # An hour between flights
        departure_home = arrival_out + timedelta(hours = 1)
        departure_home_str = departure_home.isoformat()

        arrival_home = departure_home + timedelta(hours = int(flight_time))
        arrival_home_str = arrival_home.isoformat()

        new_voyage = Voyage(voyage_id_str, flight_number_out_str, flight_number_back_str, departure_out_str, \
                            arrival_out_str, departure_home_str, arrival_home_str, target_id)

        csv_str = new_voyage.instance_to_csv_string()

        return self.ioAPI.store_new_voyage(csv_str)