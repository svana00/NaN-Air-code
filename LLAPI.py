from StaffMemberLL import StaffMemberLL
from VoyageLL import VoyageLL
from AirplaneLL import AirplaneLL
from DestinationLL import DestinationLL
from IOAPI import IOAPI

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

    def new_destination(self, dest_list):
        pass
    
    def get_all_pilots(self):
        return self.staffLL.get_all_pilots()
    
    def get_all_flightattendants(self):
        return self.staffLL.get_all_flight_attendants
        
        