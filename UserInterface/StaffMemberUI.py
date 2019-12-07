class StaffMemberUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(13 - int((len(string)/2))) + string + form*(13 - int((len(string)/2))))

    def display_staff_menu(self):
        """ prints the main staff menu and calls the appropriate
            functions for the option that's picked """
        print("\n\n" + "*"*26 + "\n\t STAFF \n"+"*"*26)
        print("1. CHANGE\n2. OVERVIEW\n3. ADD NEW \n4. test101")
        var = input("\nInput a command: ")
        if var == "1":
            return self.choose_in_staff()
        elif var == "2":
            return self.choose_in_staff()
        elif var == "3":
            return self.create_staff_member()
        elif var == "4":
            return self.show_staff_member_info()
        else:
            print("Invalid choice")

    def choose_in_staff(self):
        self.header("-", " PICK STAFF ")
        print("1. STAFF \n2. WORK SCHEDULE")
        choose_between = input("\nInput a command: ")
        if choose_between == "1":
            return self.pick_staff_sub_menu()
        elif choose_between == "2":
            return self.work_schedule_sub_menu()
        else:
            print("Invalid choice")

    def pick_staff_sub_menu(self):
        self.header("-", " PICK STAFF ")
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

    def pilot_sub_menu(self):
        self.header("-", " PICK SUBGROUP ")
        print("1. ALL PILOTS \n2. PILOTS BY LICENCE")
        choose_between = input("\nInput a command: ")
        if choose_between == "1":
            return self.show_all_pilots()
        elif choose_between == "2":
            return self.pilot_licence_sub_menu()
        else:
            print("Invalid choice")

    def pilot_licence_sub_menu(self):
        self.header("-", " PICK LICENCE SUBGROUP ")
        print("1. OVERVIEW OF ALL LICENCES \n2. ONE PARTICULAR LICENCE")
        choose_between = input("\nInput a command: ")
        if choose_between == "1":
            return self.show_pilots_by_all_licences()
        elif choose_between == "2":
            return self.show_pilots_by_one_licence()
        else:
            print("Invalid choice")

    def work_schedule_sub_menu(self):
        self.header("-", " WORK SCHEDULE ")
        print("1. SHOW ALL WORKING \n2. SHOW ALL NOT WORKING")
        choose_between = input("\nInput a command: ")
        if choose_between == "1":
            pass
        elif choose_between == "2":
            pass
        else:
            print("Invalid choice")

    def show_staff_member_info(self):
        counter = 0
        self.header("-", " BLEE ")
        staff_member_info_list = self.llAPI.get_all_staff_info()
        print(staff_member_info_list)

    def show_pilots(self):
        pass

    def show_all_pilots(self):
        """ prints the name of all the pilots from a list of their ssn and name """
        counter = 0
        self.header("-", " ALL PILOTS ")
        pilots_info_list = self.llAPI.get_all_pilots()
        for element in pilots_info_list:
            ssn = element[0]
            name = element[1]
            counter += 1
            print("{}. {}".format(counter, name))

    def show_all_flight_attendants(self):
        """ prints the name of all the flight attendants from a list of their
            ssn and names """
        counter = 0
        self.header("-", " ALL FLIGHT ATTENDANTS ")
        flight_attendants_info_list = self.llAPI.get_all_flight_attendants()
        for element in flight_attendants_info_list:
            ssn = element[0]
            name = element[1]
            counter += 1
            print("{}. {}".format(counter, name))

    def show_all_staff(self):
        """ prints the names of all of the staff members from a lis of their ssn and name """
        counter = 0
        self.header("-", " ALL STAFF MEMBERS ")
        staff_info_list = self.llAPI.get_all_staff()
        for element in staff_info_list:
            ssn = element[0]
            name = element[1]
            counter +=1
            print("{}. {}".format(str.counter, name))

        choose_between = input("\nInput a command: ")
        for counter in choose_between:
            if counter in choose_between:
                return self.show_staff_member_info()
        else:
            print("Invalid choice")

    def show_pilots_by_one_licence(self):
        """ prints all of the pilots who have a license for one particular airplane """
        airplane_type_dict = {}
        counter = 0
        self.header("-", " PICK ONE LICENCE ")
        airplane_types_info_list = self.llAPI.get_all_airplane_types()

        """ makes a dict for  """
        for element in airplane_types_info_list:
            counter += 1
            airplane_type_dict[str(counter)] = element
            print("{}. {}".format(counter, element))

        choose_between = input("\nInput a command: ")
        for key, value in airplane_type_dict.items():
            if key == choose_between:
                airplane_type_id = value
                self.header("-", " {} ".format(airplane_type_id))
                pilots_info_list = self.llAPI.get_pilots_by_one_licence(airplane_type_id)

        counter_2 = 0

        for list_thang in pilots_info_list:
            ssn = list_thang[0]
            name = list_thang[1]
            counter_2 += 1
            print("{}. {}".format(counter_2, name))


    def show_pilots_by_all_licences(self):
        self.header("-", " PILOTS BY LICENCES ")
        pilots_by_licences_dict = self.llAPI.get_pilots_by_all_licences()
        for airplane_type, pilots_info_list in pilots_by_licences_dict.items():
            print("\n{}".format(airplane_type))
            counter = 1
            for pilot_tuple in pilots_info_list:
                ssn = pilot_tuple[0]
                name = pilot_tuple[1]
                print("\t{}. {}".format(counter, name))
                counter += 1

    def create_staff_member(self):
        ssn_str = ""
        name_str = ""
        role_str = ""
        rank_str = ""
        staff_licence_str = ""
        address_str = ""
        phone_number_str = ""
        email_str = ""

        staff_member_info_list = [ "" for i in range(15)]

        ### displays the header and main body
        self.header("-", " ADD STAFF MEMBER ")
        print("\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}".format(ssn_str, name_str, role_str, rank_str, staff_licence_str, address_str, phone_number_str, email_str))
        choice = input("\nInput what you want to add: ")

        VALID_INPUT_LIST = [str(i+1) for i in range(15)]
        VALID_INPUT_LIST.append("confirm")

        #the worse but it works way to do this:

        while choice in VALID_INPUT_LIST:

            if choice == "1":
                ssn_str = input("\nEnter new ssn: ")
                staff_member_info_list[0] = ssn_str

            elif choice == "2":
                name_str = input("Enter new name: ")
                staff_member_info_list[1] = name_str

            elif choice == "3":
                role_str = input("Enter new role: ")
                staff_member_info_list[2] = role_str

            elif choice == "4":
                rank_str = input("Enter new rank: ")
                staff_member_info_list[3] = rank_str

            elif choice == "5":
                staff_licence_str = input("Enter new staff license: ")
                staff_member_info_list[4] = staff_licence_str

            elif choice == "6":
                address_str = input("Enter new address: ")
                staff_member_info_list[5] = address_str

            elif choice == "7":
                phone_number_str = input("Enter new phone number: ")
                staff_member_info_list[6] = phone_number_str

            elif choice == "8":
                email_str = input("Enter emergency phone number: ")
                staff_member_info_list[7] = email_str

            elif choice == "confirm":
                print("Changes have been confirmed")
                return self.llAPI.create_new_destination(staff_member_info_list)

            self.header("-", " ADD STAFF MEMBER ")
        print("\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}".format(ssn_str, name_str, role_str, rank_str, staff_licence_str, address_str, phone_number_str, email_str))
        choice = input("\nInput what you want to add: ")

    def change_staff_member_info(self):
        pass

    def show_all_working(self):
        pass

    def show_all_not_working(self):
        pass

    def show_staff_member_schedule(self):
        pass


