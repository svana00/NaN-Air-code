import datetime

class VoyageLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI

    def assign_voyage_staff(self):
        pass

    def get_all_voyages(self):
        voyage_list = self.ioAPI.load_all_voyages()
        voyage_info_list = []

        for voyage in voyage_list:
            dest_id = voyage.get_dest_id()
            departure_out = voyage.get_departure_out()
            voyage_id = voyage.get_voyage_id()
            voyage_info_list.append((dest_id, departure_out, voyage_id))

        return voyage_info_list

    def get_all_voyages_for_week(self, start_of_desired_week_str):
        voyages_list = self.ioAPI.load_all_voyages()
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

    def get_voyages_by_date(self):
        pass

    def get_voyages_by_week(self):
        pass

    def get_non_assigned_voyages(self):
        pass

    def check_voyages_state(self):
        pass

    def check_if_fully_assigned(self):
        pass

    def make_voyage(self, voyage_info_list):
        voyages_list = self.ioAPI.load_all_voyages()
        voyage_id = len(voyages_list)

        if voyage_id < 10:
            voyage_id = "0" + "{}".format(voyage_id)
        elif voyage < 100:
<<<<<<< HEAD
            voyage_id = "0" + "{}".format(voyage_id)

    def get_all_voyages(self):
        voyage_list = self.ioAPI.load_all_voyages()
        voyage_info_list = []

        for voyage in voyage_list:
            voyage_id = voyage.get_voyage_id()
            dest_id = voyage.get_dest_id()
            departure_out = voyage.get_departure_out()
            voyage_info_list.append((voyage_id, dest_id, departure_out))

        return voyage_info_list
=======
            voyage_id = "0" + "{}".format(voyage_id)
>>>>>>> 5cc38d0b27dd389863933101bfc13808ae515666
