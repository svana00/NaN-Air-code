from StaffMemberIO import StaffMemberIO
from DestinationIO import DestinationIO
from AirplaneIO import AirplaneIO

class IOAPI():
    
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