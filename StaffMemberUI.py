from LLAPI import LLAPI

class StaffMemberUI():

    def DisplayStaffMainMenu(self):
        print("*"*26 + "\n\t STAFF \n"+"*"*26)
        print("1. CHANGE\n2. GET\n3. ADD")
        var = input("\nInput a command: ")


    def show_staff_member_info(self): 
        print("* SHOW ALL STAFF * ")
        pass

    def show_pilots(self):
        pass

    def show_all_pilots(self):
        pass

    def show_all_flight_attendants(self):
        pass

    def show_all_staff(self):
        print("*"*8 + " ALL STAFF "+"*"*8)
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