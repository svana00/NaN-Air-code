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

    def get_all_staff(self):
        return self.staffLL.get_all_staff()

    def get_all_dest(self):
        return self.destLL.get_destinations()

    def create_new_destination(self, dest_list):
        self.dest_list = dest_list
        return self.destLL.create_new_destination(self.dest_list)
    
    def get_all_pilots(self):
        return self.staffLL.get_all_pilots()
    
    def get_all_flight_attendants(self):
        return self.staffLL.get_all_flight_attendants()
