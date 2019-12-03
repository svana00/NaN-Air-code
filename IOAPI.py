from Staff_Members_IO import StaffMemberIO
from Destination_IO import DestinationIO

class IOAPI():
    
    def load_all_staff_from_file(self):
        StaffMemberIO_temp = StaffMemberIO()
        return StaffMemberIO_temp.load_all_staff_from_file()

    def load_all_dest_from_file(self):
        DestinationIO_temp = DestinationIO()
        return DestinationIO_temp.load_all_dest_from_file()