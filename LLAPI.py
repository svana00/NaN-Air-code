from StaffMemberLL import StaffMemberLL
from VoyageLL import VoyageLL
from AirplaneLL import AirplaneLL
from DestinationLL import DestinationLL

class LLAPI():

    def get_all_staff_info(self):
        Staff_Member_LL = StaffMemberLL()
        return Staff_Member_LL.get_all_staff_info()

    def get_all_dest(self):
        Destination_LL = DestinationLL()
        return Destination_LL.getDestinations()