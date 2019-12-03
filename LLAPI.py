from StaffMemberLL import StaffMemberLL
from VoyageLL import VoyageLL
from AirplaneLL import AirplaneLL
from DestinationLL import DestinationLL

class LLAPI():

    def get_all_staff(self):
        return StaffMemberLL.get_all_staff()

    def get_all_dest(self):
        return DestinationLL.getDestinations()