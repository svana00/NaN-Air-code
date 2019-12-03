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

    def get_all_staff_names(self):
        ''' Returns a list of staff member names '''
        IOAPI_temp = IOAPI()
        staff_list = IOAPI_temp.load_all_staff_from_file()
        staff_names_list = []

        for staff_member in staff_list:
            name = staff_member.get_name()
            staff_names_list.append(name)
        
        return staff_names_list

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