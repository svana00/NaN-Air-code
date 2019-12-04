
class StaffMemberUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(13 - int((len(string)/2))) + string + form*(13 - int((len(string)/2))))

    def display_staff_menu(self):
        print("\n\n" + "*"*26 + "\n\t STAFF \n"+"*"*26)
        print("1. CHANGE\n2. OVERVIEW\n3. ADD NEW")
        var = input("\nInput a command: ")
        if var == "1":
            return self.choose_in_staff()
        elif var == "2":
            return self.choose_in_staff()
        elif var == "3":
            pass
        else:
            print("Invalid choice")

    def show_staff_member_info(self):

        pass

    def show_pilots(self):
        pass

    def show_all_pilots(self):
        counter = 0
        self.header("*", " ALL PILOTS ")
        pilots_info_list = self.llAPI.get_all_pilots()
        for element in pilots_info_list:
            ssn = element[0]
            name = element[1]
            counter += 1
            print("{}. {}".format(counter, name))

    def show_all_flight_attendants(self):
        counter = 0
        self.header("*", " ALL FLIGHT ATTENDANTS ")
        flight_attendants_info_list = self.llAPI.get_all_flight_attendants()
        for element in flight_attendants_info_list:
            ssn = element[0]
            name = element[1]
            counter += 1
            print("{}. {}".format(counter, name))

    def show_all_staff(self):
        counter = 0
        self.header("*", " ALL STAFF MEMBERS ")
        staff_info_list = self.llAPI.get_all_staff()
        for element in staff_info_list:
            ssn = element[0]
            name = element[1]
            counter +=1
            print("{}. {}".format(counter, name))

    def show_pilots_by_one_license(self):
        airplane_type_dict = {}
        counter = 0
        self.header("*", " PICK ONE LICENSE ")
        airplane_types_info_list = self.llAPI.get_all_airplane_types()

        for element in airplane_types_info_list:
            counter += 1
            airplane_type_dict[str(counter)] = element
            print("{}. {}".format(counter, element))

        choose_between = input("\nInput a command: ")
        for key, value in airplane_type_dict.items():
            if key == choose_between:
                airplane_type_id = value
                self.header("*", " {} ".format(airplane_type_id))
                pilots_info_list = self.llAPI.get_pilots_by_one_license(airplane_type_id)
                print(pilots_info_list)


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
        if pick_staff == "1":
            self.pilot_sub_menu()
        elif pick_staff == "2":
            self.show_all_flight_attendants()
        elif pick_staff == "3":
            self.show_all_staff()
        else:
            print("Invalid choice")


    def choose_in_staff(self):
        self.header("*", " PICK STAFF ")
        print("1. STAFF \n2. WORK SCHEDULE")
        choose_between = input("\nInput a command: ")
        if choose_between == "1":
            return self.pick_staff_sub_menu()
        elif choose_between == "2":
            return self.work_schedule_sub_menu()
        else:
            print("Invalid choice")

    def pilot_sub_menu(self):
        self.header("*", " PICK SUBGROUP ")
        print("1. ALL PILOTS \n2. PILOTS BY LICENSE")
        choose_between = input("\nInput a command: ")
        if choose_between == "1":
            return self.show_all_pilots()
        elif choose_between == "2":
            return self.pilot_licence_sub_menu()
        else:
            print("Invalid choice")

    def work_schedule_sub_menu(self):
        self.header("*", " WORK SCHEDULE ")
        print("1. SHOW ALL WORKING \n2. SHOW ALL NOT WORKING")
        choose_between = input("\nInput a command: ")
        if choose_between == "1":
            pass
        elif choose_between == "2":
            pass
        else:
            print("Invalid choice")

    def pilot_licence_sub_menu(self):
        self.header("*", " PICK LICENSE SUBGROUP ")
        print("1. OVERVIEW OF ALL LICENSES \n2. ONE PARTICULAR LICENSE")
        choose_between = input("\nInput a command: ")
        if choose_between == "1":
            return self.show_pilots_by_all_licenses()
        elif choose_between == "2":
            return self.show_pilots_by_one_license()
        else:
            print("Invalid choice")

"""
staff = StaffMemberUI()
staff.show_all_staff()
choose_in_staff = staff.choose_in_staff()
staff.display_staff_menu(choose_in_staff)
staff.pick_staff_sub_menu()
"""
