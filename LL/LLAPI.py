from LL.StaffMemberLL import StaffMemberLL
from LL.VoyageLL import VoyageLL
from LL.AirplaneLL import AirplaneLL
from LL.DestinationLL import DestinationLL
from IO.IOAPI import IOAPI

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
