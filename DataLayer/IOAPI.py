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
        return self.staffIO.store_new_staff_member(staff_member_str)

    def create_new_airplane(self, airplane_str):
        self.airplane_str = airplane_str
        return self.airplaneIO.store_new_airplane_into_file(airplane_str)

    def load_all_voyages(self):
        return self.voyageIO.load_all_voyages()