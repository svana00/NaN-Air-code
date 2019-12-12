import datetime
from MODELS.voyage import Voyage
class VoyageLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI

    def get_voyage_info(self, voyage_id):
        voyage_list = self.ioAPI.load_all_voyages()
        for voyage in voyage_list:
            if voyage.get_voyage_id() == voyage_id:
                return voyage

    def assign_voyage(self, chosen_voyage):
        voyages_list = self.get_all_voyages()

        for num, voyage in enumerate(voyages_list):
            if voyage.get_voyage_id() == chosen_voyage.get_voyage_id():
                    voyages_list[num] = chosen_voyage

        return self.ioAPI.store_voyage_changes(voyages_list)

    def get_all_voyages(self):

        voyage_list = self.ioAPI.load_all_voyages()
        return voyage_list

    def get_voyages_by_week(self, start_of_desired_week_str):
        voyages_list = self.ioAPI.load_all_voyages()
        voyages_in_week_list = []

        start_of_desired_week = datetime.date.fromisoformat(start_of_desired_week_str)
        end_of_desired_week = datetime.date.fromisoformat(start_of_desired_week_str) + datetime.timedelta(days = 6)

        for voyage in voyages_list:
            temp_date = datetime.datetime.fromisoformat(voyage.get_departure_out()).date()
            if temp_date >= start_of_desired_week and temp_date <= end_of_desired_week:
                voyages_in_week_list.append(voyage)

        return voyages_in_week_list

    def get_voyages_by_date(self, desired_date_str):
        
        voyages_list = self.ioAPI.load_all_voyages()
        target_date = datetime.date.fromisoformat(desired_date_str)
        voyages_on_date_list = []

        for voyage in voyages_list:
            departure_date = datetime.datetime.fromisoformat(voyage.get_departure_out()).date()
            if target_date == departure_date:
                voyages_on_date_list.append(voyage)

        return voyages_on_date_list

    def get_non_assigned_voyages(self):
        ''' Returns a list of voyages that are not fully assigned '''
        non_assigned_voyages_list = []
        voyages_List = self.ioAPI.load_all_voyages()
        for voyage in voyages_List:
            is_fully_assigned = voyage.is_fully_assigned()
            if is_fully_assigned == "False":
                non_assigned_voyages_list.append(voyage)
        
        return non_assigned_voyages_list

    def check_voyages_state(self):
        pass

    def create_flight_numbers_for_voyage(self, voyage_info_list, target_dest_id):
        voyages_list = self.ioAPI.load_all_voyages()
        destinations_list = self.ioAPI.load_all_destinations()

        for destination in destinations_list:
            destination_id = destination.get_id()
            if target_dest_id == destination_id:
                # Find flight time for chosen destination for voyage
                flight_time = destination.get_flight_time()
                dest_flight_number_id  = destination.get_flight_number_id()

        target_date = voyage_info_list[1]
        counter = 0

        # Find how many flights are already to that destination that same day
        for voyage in voyages_list: 
            dest_id = voyage.get_dest_id()
            departure_out_date = voyage.get_departure_out()
            date = datetime.datetime.fromisoformat(departure_out_date).date()
            date = str(date)
            if dest_id == target_dest_id and date == target_date:
                counter += 1

        flight_number_out_str = "NA" + str(dest_flight_number_id) + str(counter * 2)
        flight_number_back_str = "NA" + str(dest_flight_number_id) + str(counter * 2 + 1)

        return flight_time, flight_number_out_str, flight_number_back_str

    def make_voyage(self, voyage_info_list):
        voyages_list = self.ioAPI.load_all_voyages()
        target_dest_id = voyage_info_list[0]

        # Create voyage id
        voyage_id_int = len(voyages_list) + 1

        if voyage_id_int < 10:
            voyage_id_str = "00" + "{}".format(voyage_id_int)
        elif voyage_id_int < 100:
            voyage_id_str = "0" + "{}".format(voyage_id_int)

        # Create flight numbers
        flight_time, flight_number_out_str, flight_number_back_str = \
        self.create_flight_numbers_for_voyage(voyage_info_list, target_dest_id)

        # Find time of each flight
        departure_out_str = ("T").join(voyage_info_list[1:]) # Departure out

        departure_out = datetime.datetime.fromisoformat(departure_out_str)
        arrival_out = departure_out + datetime.timedelta(hours = int(flight_time))
        arrival_out_str = arrival_out.isoformat()

        # An hour between the flights
        departure_home = arrival_out + datetime.timedelta(hours = 1)
        departure_home_str = departure_home.isoformat()

        arrival_home = departure_home + datetime.timedelta(hours = int(flight_time))
        arrival_home_str = arrival_home.isoformat()

        new_voyage = Voyage(voyage_id_str, flight_number_out_str, flight_number_back_str, departure_out_str, \
                            arrival_out_str, departure_home_str, arrival_home_str, target_dest_id)

        csv_str = new_voyage.instance_to_csv_string()

        return self.ioAPI.store_new_voyage(csv_str)

    def voyage_date_check(self, departure_out_str):
        ''' Returns whether a date is valid for a voyage '''
        voyages_list = self.ioAPI.load_all_voyages()
        departure_out = datetime.datetime.fromisoformat(departure_out_str)

        for voyage in voyages_list:
            departure_out_2_str = voyage.get_departure_out()
            departure_out_2 = datetime.datetime.fromisoformat(departure_out_2_str)

            start_date = departure_out_2 + datetime.timedelta(hours = -1)
            end_date = departure_out_2 + datetime.timedelta(hours = 1)

            if start_date <= departure_out <= end_date:
                return False

        return True