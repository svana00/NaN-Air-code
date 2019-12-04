from DataLayer.StaffMemberIO import StaffMemberIO
from DataLayer.DestinationIO import DestinationIO
from DataLayer.AirplaneIO import AirplaneIO
from DataLayer.VoyageIO import VoyageIO

class IOAPI:

    def __init__(self):
        self.staffIO = StaffMemberIO()
        self.destIO = DestinationIO()
        self.airplaneIO = AirplaneIO()
        self.voyageIO = VoyageIO()
    
    def load_all_staff_from_file(self):
        return self.staffIO.load_all_staff_from_file()

    def load_all_dest_from_file(self):
        return self.destIO.load_all_dest_from_file()

    def create_new_destination(self, dest_str):
        return self.destIO.storeNewDestinationtoFile(dest_str)
    
    def load_all_airplanes(self):
        return self.airplaneIO.load_all_airplanes()

    def load_airplane_types(self):

        return self.airplaneIO.load_airplane_types()

    def store_new_staff_member(self,staff_member_str):
        return self.staffIO.store_new_staff_member(self,staff_member_str)