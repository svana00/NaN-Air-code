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

    def get_staff_member_info(self, ssn):
        return self.staffLL.get_staff_member_info(ssn)

    def get_all_airplane_types(self):
        return self.staffLL.get_all_airplane_types()

    def get_pilots_by_one_licence(self,airplane_type_id):
        return self.staffLL.get_pilots_by_one_licence(airplane_type_id)

    def get_pilots_by_all_licences(self):
        return self.staffLL.get_pilots_by_all_licences()

    def get_all_staff(self):
        return self.staffLL.get_all_staff()

    def get_destinations(self):
        return self.destLL.get_destinations()

    def get_destination_info(self, dest_id):
        return self.destLL.get_destination_info(dest_id)

    def get_mutable_destination_info_list(self):
        return self.destLL.get_mutable_destination_info_list()

    def create_new_destination(self, dest_list):
        self.dest_list = dest_list
        return self.destLL.create_new_destination(self.dest_list)

    def get_all_pilots(self):
        return self.staffLL.get_all_pilots()

    def get_all_flight_attendants(self):
        return self.staffLL.get_all_flight_attendants()

    def create_staff_member(self, staff_member_info_list):
        return self.staffLL.create_staff_member(staff_member_info_list)

    def get_all_voyages(self):
        return self.ioAPI.load_all_voyages()

    def create_new_airplane(self, airplane_str):
        self.airplane_str = airplane_str
        return self.airplaneLL.makeAirplane(airplane_str)

    def get_all_working(self, desired_date_str):
        return self.staffLL.get_all_working(desired_date_str)

    def get_all_not_working(self, desired_date_str):
        return self.staffLL.get_all_not_working(desired_date_str)

    def get_staff_member_schedule(self, ssn, start_of_target_week):
        return self.staffLL.get_staff_member_schedule(ssn, start_of_target_week)