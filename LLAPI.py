from StaffMemberLL import StaffMemberLL
from IOAPI import IOAPI


class LLAPI():
    IOAPI_temp = IOAPI()

    def get_all_staff(self):
        return self.IOAPI_temp.load_all_staff_from_file()

    def get_all_dest(self):
        return self.IOAPI_temp.load_all_dest_from_file()
