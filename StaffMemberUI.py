from LLAPI import LLAPI

class StaffMemberUI():

    def show_staff_member_info(self):
        pass

    def show_pilots(self):
        pass

    def show_all_pilots(self):
        pass

    def show_all_flight_attendants(self):
        pass

    def show_all_staff(self):
        LLAPI_temp = LLAPI()
        a_list = LLAPI_temp.get_all_staff()
        for element in a_list:
            print(element)

    def show_pilots_by_license(self):
        pass

    def show_pilots_by_one_license(self):
        pass

    def show_pilots_by_all_licenses(self):
        pass

    def create_staff_members(self):
        pass

    def change_staff_member_info(self):
        pass

    def show_all_working(self):
        pass

    def show_all_not_working(self):
        pass

    def show_staff_member_schedule(self):
        pass

staff = StaffMemberUI()

staff.show_all_staff()