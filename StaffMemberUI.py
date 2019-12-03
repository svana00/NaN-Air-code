from LLAPI import LLAPI

class StaffMemberUI():

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(13 - int((len(string)/2))) + string + form*(13 - int((len(string)/2))))

    def display_staff_menu(self):
        print("\n\n" + "*"*26 + "\n\t STAFF \n"+"*"*26)
        print("1. CHANGE\n2. GET\n3. ADD")
        var = input("\nInput a command: ")
        if var == "1":
            pass
        elif var == "2":
            return self.choose_in_staff()
        elif var == "3":
            pass

    def show_staff_member_info(self):

        pass

    def show_pilots(self):
        pass

    def show_all_pilots(self):
        pass

    def show_all_flight_attendants(self):
        pass

    def show_all_staff(self):
        self.header("*", " ALL STAFF MEMBERS ")
        LLAPI_temp = LLAPI()
        a_list = LLAPI_temp.get_all_staff_info()
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

    def pick_staff_sub_menu(self):
        self.header("*", " PICK STAFF ")
        print("1. PILOTS \n2. FLIGHT ATTENDANTS \n3. ALL STAFF")
        pick_staff = input("\nInput a command: ")
        if pick_staff == "3":
            self.show_all_staff()

    def choose_in_staff(self):
        self.header("*", " PICK STAFF ")
        print("1. STAFF \n2. WORK SCHEDULE")
        choose_between = input("\nInput a command: ")
        if choose_between == "1":
            self.pick_staff_sub_menu()
        elif choose_between == "2":
            pass
        else:
            print("invalid choice")


"""
staff = StaffMemberUI()
staff.show_all_staff()
choose_in_staff = staff.choose_in_staff()
staff.display_staff_menu(choose_in_staff)
staff.pick_staff_sub_menu()
"""
