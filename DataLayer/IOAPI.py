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

    # ---- Staff member functions ----

    def load_all_staff(self):
        return self.staffIO.load_all_staff()

    def store_staff_changes(self, staff_member_instance_list):
        return self.staffIO.store_staff_member_info(staff_member_instance_list)

    def store_new_staff_member(self,staff_member_str):
        return self.staffIO.store_new_staff_member(staff_member_str)

    # ---- Destination functions ----

    def load_all_destinations(self):
        return self.destIO.load_all_destinations()

    def store_destination_changes(self, dest_list):
        return self.destIO.store_destination_changes(dest_list)

    def create_new_destination(self, dest_str):
        return self.destIO.store_new_destination(dest_str)

    # ---- Airplane functions ----
    
    def load_all_airplanes(self):
        return self.airplaneIO.load_all_airplanes()

    def load_airplane_types(self):
        return self.airplaneIO.load_airplane_types()

    def create_new_airplane(self, airplane_str):
        self.airplane_str = airplane_str
        return self.airplaneIO.store_new_airplane_into_file(airplane_str)
    
    # ---- Voyage functions ----

    def load_all_voyages(self):
        return self.voyageIO.load_all_voyages()

    def store_voyage_changes(self, voyages_list):
        return self.voyageIO.store_voyage_changes(voyages_list)

    def store_new_voyage(self, csv_str):
        return self.voyageIO.store_new_voyage(csv_str)