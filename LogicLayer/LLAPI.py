from LogicLayer.StaffMemberLL import StaffMemberLL
from LogicLayer.VoyageLL import VoyageLL
from LogicLayer.AirplaneLL import AirplaneLL
from LogicLayer.DestinationLL import DestinationLL
from DataLayer.IOAPI import IOAPI

class LLAPI():

    def __init__(self):
        self.ioAPI = IOAPI()
        self.destLL = DestinationLL(self.ioAPI)
        self.staffLL = StaffMemberLL(self.ioAPI)
        self.voyageLL = VoyageLL(self.ioAPI)
        self.airplaneLL = AirplaneLL(self.ioAPI)

    # ---- Staff member functions ----

    def get_staff_member_info(self, ssn):
        return self.staffLL.get_staff_member_info(ssn)

    def get_all_airplane_types(self):
        return self.airplaneLL.get_all_airplane_types()

    def get_pilots_by_one_licence(self,airplane_type_id):
        return self.staffLL.get_pilots_by_one_licence(airplane_type_id)

    def get_pilots_by_all_licences(self):
        return self.staffLL.get_pilots_by_all_licences()

    def get_all_staff(self):
        return self.staffLL.get_all_staff()
   
    def get_all_pilots(self):
        return self.staffLL.get_all_pilots()

    def get_all_flight_attendants(self):
        return self.staffLL.get_all_flight_attendants()

    def create_staff_member(self, new_staff_member):
        return self.staffLL.create_staff_member(new_staff_member)

    def get_all_working(self, departure_out_date):
        return self.staffLL.get_all_working(departure_out_date)

    def get_all_not_working(self, departure_out_date):
        return self.staffLL.get_all_not_working(departure_out_date)
    
    def get_staff_member_schedule(self, ssn, start_of_desired_week_str):
        return self.staffLL.get_staff_member_schedule(ssn, start_of_desired_week_str)

    def store_new_staff_changes(self, staff_member_instance_list):
        return self.staffLL.store_new_staff_changes(staff_member_instance_list)

    # ---- Destination functions ----
    def get_destinations(self):
        return self.destLL.get_destinations()

    def get_destination_info(self, dest_id):
        return self.destLL.get_destination_info(dest_id)

    def create_new_destination(self, new_destination):
        return self.destLL.create_new_destination(new_destination)
    
    #def anton_og_magga_eru_best(self):
    def get_destination_instance_list(self):
        destination_instance_list = self.destLL.lets_see_if_this_works()
        return destination_instance_list

    def store_new_dest_changes(self, destination_instance_list):
        return self.destLL.store_new_changes(destination_instance_list)

    # ---- Voyage functions ----
    def get_voyage_info(self, voyage_id):
        return self.voyageLL.get_voyage_info(voyage_id)

    def get_all_voyages(self):
        return self.voyageLL.get_all_voyages()

    def make_voyage(self, voyage_info_list):
        return self.voyageLL.make_voyage(voyage_info_list)

    def get_voyages_by_date(self, desired_date_str):
        return self.voyageLL.get_voyages_by_date(desired_date_str)

    def get_non_assigned_voyages(self):
        return self.voyageLL.get_non_assigned_voyages()

    def check_voyages_state(self):
        return self.voyageLL.check_voyages_state()

    def get_voyages_by_week(self, start_of_desired_week_str):
        return self.voyageLL.get_voyages_by_week(start_of_desired_week_str)

    def assign_voyage(self, chosen_voyage):
        return self.voyageLL.assign_voyage(chosen_voyage)

    # ---- Airplane functions ----
    def create_new_airplane(self, airplane_str):
        self.airplane_str = airplane_str
        return self.airplaneLL.make_airplane(airplane_str)

    def get_all_airplanes(self):
        return self.airplaneLL.get_all_airplanes()

    def get_airplane(self, plane_id):
        return self.airplaneLL.get_airplane(plane_id)
    
    def get_airplane_state(self, airplane_instance, date_and_time):
        return self.airplaneLL.get_airplane_state(airplane_instance, date_and_time)

    def get_free_airplanes(self, departure_out_str, arrival_home_str):
        return self.airplaneLL.get_free_airplanes(departure_out_str, arrival_home_str)