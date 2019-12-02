from Staff_Members_IO import StaffMemberIO

class IOAPI():
    
    def load_all_staff_from_file(self):
        StaffMemberIO_temp = StaffMemberIO()
        return StaffMemberIO_temp.load_all_staff_from_file()