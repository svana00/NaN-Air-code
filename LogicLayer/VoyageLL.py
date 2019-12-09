import datetime
class VoyageLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
        
    def assign_voyage_staff(self):
        pass

    def make_voyage(self):
        pass

    def get_all_voyages(self, start_of_desired_week_str):
        voyage_list = self.ioAPI.load_all_voyages()
        voyage_info_list = []

        end_of_desired_week = datetime.datetime.fromisoformat(start_of_desired_week_str) + datetime.timedelta(days = 6)

        for voyage in voyage_list:
            departure_out = voyage.get_departure_out()
            dest_id = voyage.get_dest_id()
            voyage_info_list.append((departure_out, dest_id))

        return voyage_info_list

    def get_voyages_by_date(self):
        pass

    def get_voyages_by_week(self):
        pass

    def get_non_assigned_voyages(self):
        pass

    def check_if_fully_assigned(self):
        pass

    def check_voyages_state(self):
        pass