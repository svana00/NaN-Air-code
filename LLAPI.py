from StaffMemberLL import StaffMemberLL
from VoyageLL import VoyageLL
from AirplaneLL import AirplaneLL
from DestinationLL import DestinationLL

class LLAPI():

    def get_all_staff(self):
        Staff_Member_LL = StaffMemberLL()
        return Staff_Member_LL.get_all_staff()

    def get_all_dest(self):
        Destination_LL = DestinationLL()
        return Destination_LL.getDestinations()

    def new_destination(self, dest_list):
        pass
    
    def get_all_pilots(self):
        Staff_Member_LL = StaffMemberLL()
        return Staff_Member_LL.get_all_pilots()
    
    def get_all_flightattendants(self):
        Staff_MemberLL = StaffMemberLL()
        return Staff_MemberLL.get_all_flight_attendants
        
        