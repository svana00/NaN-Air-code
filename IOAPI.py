from StaffMemberIO import StaffMemberIO
from DestinationIO import DestinationIO
from AirplaneIO import AirplaneIO
from VoyageIO import VoyageIO

class IOAPI:

    def __init__(self):
        self.staffIO = StaffMemberIO()
        self.destIO = DestinationIO()
        self.airplaneIO = AirplaneIO()
        self.voyageIO = VoyageIO()
    
    def load_all_staff_from_file(self):
        StaffMemberIO_temp = StaffMemberIO()
        return StaffMemberIO_temp.load_all_staff_from_file()

    def load_all_dest_from_file(self):
        DestinationIO_temp = DestinationIO()
        return DestinationIO_temp.load_all_dest_from_file()

    def load_all_airplanes(self):
        AirplaneIO_temp = AirplaneIO()
        return AirplaneIO_temp.load_all_airplanes()

    def load_airplane_types(self):
        AirplaneIO_temp = AirplaneIO()
        return AirplaneIO_temp.load_airplane_types()