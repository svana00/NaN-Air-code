from IOAPI import IOAPI

class StaffMemberLL():

    def get_staff_member_info(self):
        pass

    def get_pilots(self):
        pass

    def get_all_pilots(self):
        pass

    def get_all_flight_attendants(self):
        pass

    def get_all_staff_info(self):
        ''' Returns a list of staff member names '''
        IOAPI_temp = IOAPI()
        staff_list = IOAPI_temp.load_all_staff_from_file()
        staff_info_list = []

        for staff_member in staff_list:
            ssn = staff_member.get_ssn()
            name = staff_member.get_name()
            staff_info_list.append((ssn, name))
        
        return staff_info_list

    def get_pilots_by_license(self):
        pass

    def get_pilots_by_one_license(self):
        pass

    def get_pilots_by_all_licenses(self):
        pass

    def create_staff_members(self):
        pass

    def change_staff_member_info(self):
        pass

    def get_all_working(self):
        pass

    def get_all_not_working(self):
        pass

    def get_staff_member_schedule(self):
        pass

staff = StaffMemberLL()
a_list = staff.get_all_staff_info()
print(a_list)
