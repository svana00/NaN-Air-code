import datetime
class VoyageLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI

    def get_all_voyages(self):
        voyage_list = self.ioAPI.load_all_voyages()
        voyage_info_list = []

        for voyage in voyage_list:
            dest_id = voyage.get_dest_id()
            departure_out = voyage.get_departure_out()
            voyage_info_list.append((dest_id, departure_out))

        return voyage_info_list

    def get_voyages_by_date(self):
        pass

    def get_voyages_by_week(self, start_of_desired_week_str):
        voyage_list = self.ioAPI.load_all_voyages()
        voyages_in_week_list = []
        voyage_info_list = []

        start_of_desired_week = datetime.datetime.fromisoformat(start_of_desired_week_str).date()
        end_of_desired_week = datetime.datetime.fromisoformat(start_of_desired_week_str) + datetime.timedelta(days = 6)

        for voyage in voyages_list:
            temp_date = datetime.datetime.fromisoformat(voyage.get_departure_out(), voyage.get_dest_id()).date()
            if temp_date >= start_of_desired_week and temp_date <= end_of_desired_week:
                voyages_in_week_list.append(voyage)

        for voyage in voyages_in_week_list:
            if voyage in voyages_in_week_list:
                voyage_info_list.append((departure_out, dest_id))

        return voyage_info_list

    def get_non_assigned_voyages(self):
        pass

    def check_if_fully_assigned(self):
        pass

    def check_voyages_state(self):
        pass

    def assign_voyage_staff(self):
        pass

    def make_voyage(self, voyage_info_list):
        pass