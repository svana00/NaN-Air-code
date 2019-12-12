from Validation.validation import Validate
from MODELS.staff_member import StaffMember

class StaffMemberUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI
        self.validation = Validate()

    def header(self, form, string):
        ''' Creates a header with the form as decoration before the chosen string '''

        print("\n\n"+form*(28 - int((len(string)/2))) + string + form*(28 - int((len(string)/2))))

    def display_staff_menu(self):
        ''' Prints the main staff menu and calls the appropriate
            functions for the option that's picked '''

        print("\n\n"+"*"*56 + "\n"+" "*int((56-len(" STAFF "))/2)+" STAFF "+" "*int((56-len(" STAFF "))/2)+"\n"+"*"*56)
        print("1. CHANGE\n2. OVERVIEW\n3. ADD NEW")
        var = input("\nInput a command: ")
        if var == "1":
            return self.change_staff_member_info()
        elif var == "2":
            return self.choose_in_staff()
        elif var == "3":
            return self.create_staff_member()
        else:
            print("Invalid choice")

    def choose_in_staff(self):
        ''' Displays the submenu to choos between getting an overview of work schedules or staff members ''' 

        self.header("-", " PICK STAFF ")
        print("1. STAFF \n2. WORK SCHEDULE")
        choice = input("\nInput a command: ")
        if choice == "1":
            return self.pick_staff_sub_menu()
        elif choice == "2":
            return self.work_schedule_sub_menu()
        else:
            print("Invalid choice")

    def pick_staff_sub_menu(self):
        ''' Displays the staff sub menu '''

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
        ''' Displays the submenu for pilots '''

        self.header("-", " PICK SUBGROUP ")
        print("1. ALL PILOTS \n2. PILOTS BY LICENCE")
        choice = input("\nInput a command: ")
        if choice == "1":
            return self.show_all_pilots()
        elif choice == "2":
            return self.pilot_licence_sub_menu()
        else:
            print("Invalid choice")

    def pilot_licence_sub_menu(self):
        ''' Displays the submenu for pilots to filter by licences '''

        self.header("-", " PICK LICENCE SUBGROUP ")
        print("1. OVERVIEW OF ALL LICENCES \n2. ONE PARTICULAR LICENCE")
        choice = input("\nInput a command: ")
        if choice == "1":
            return self.show_pilots_by_all_licences()
        elif choice == "2":
            return self.show_pilots_by_one_licence()
        else:
            print("Invalid choice")

    def work_schedule_sub_menu(self):
        ''' Shows a work schedule, for a single week, for a specific staff member '''

        self.header("-", " WORK SCHEDULE ")
        print("1. SHOW ALL STAFF MEMBERS WORKING ON A SPECIFIC DAY \n2. SHOW ALL STAFF MEMBERS NOT WORKING ON A SPECIFIC DAY\n3. SHOW THE WORK SCHEDULE OF A SPECIFIC STAFF MEMBER FOR A SPECIFIC WEEK")
        choice = input("\nInput a command: ")

        if choice == "1":
            self.show_all_working()

        elif choice == "2":
            self.show_all_not_working()

        elif choice == "3":
            self.show_staff_member_schedule()

        else:
            print("Invalid choice\nPlease try again")

    def show_staff_member_info(self, staff_info_list):
        ''' Prints more info about a specific staff member '''

        number = int(input("Enter number of staff member: "))
        ssn = staff_info_list[(number) - 1].get_ssn()
        staff_member = self.llAPI.get_staff_member_info(ssn)
        self.header("-", " {} ".format(staff_member.get_name()))
        print(staff_member)

    def show_all_pilots(self):
        """ Prints the name of all the pilots from a list of their ssn and name """

        counter = 0
        self.header("-", " ALL PILOTS ")
        pilots_list = self.llAPI.get_all_pilots()

        for pilot in pilots_list:
            name = pilot.get_name()
            counter += 1
            print("{}. {}".format(counter, name))

        choice = input("\nDo you want to see more info about a specific staff pilot? (y/n): ")
        if choice == "y":
            return self.show_staff_member_info(pilots_list)

    def show_all_flight_attendants(self):
        """ Prints the name of all the flight attendants from a list of their
            ssn and names """

        counter = 0
        self.header("-", " ALL FLIGHT ATTENDANTS ")
        flight_attendants_list = self.llAPI.get_all_flight_attendants()

        for flight_attendant in flight_attendants_list:
            name = flight_attendant.get_name()
            counter += 1
            print("{}. {}".format(counter, name))

        choice = input("\nDo you want to see more info about a specific flight attendant? (y/n): ")
        if choice == "y":
            return self.show_staff_member_info(flight_attendants_list)

    def show_all_staff(self):
        """ Prints the names of all of the staff members from a lis of their ssn and name """
    
        counter = 0
        self.header("-", " ALL STAFF MEMBERS ")
        staff_list = self.llAPI.get_all_staff()
        for staff_member in staff_list:
            name = staff_member.get_name()
            counter +=1
            print("{}. {}".format(counter, name))
            
        choice = input("\nDo you want to see more info about a specific staff member? (y/n): ")
        if choice == "y":
            return self.show_staff_member_info(staff_list)

    def show_pilots_by_one_licence(self):
        """ Prints all of the pilots who have a license for one particular airplane """

        self.header("-", " PICK ONE LICENCE ")
        airplane_types_info_list = self.llAPI.get_all_airplane_types()

        airplane_type_dict = {}
        counter = 0
        # Prints all pilots that have a specific licence
        for airplane_type_id in airplane_types_info_list:
            counter += 1
            airplane_type_dict[str(counter)] = airplane_type_id
            print("{}. {}".format(counter, airplane_type_id))

        choice = input("\nPlease input the number corresponding to the licence you want to see: ")

        for number, airplane_type_id in airplane_type_dict.items():
            if number == choice:
                airplane_type_id = airplane_type_id
                self.header("-", " {} ".format(airplane_type_id))
                pilots_info_list = self.llAPI.get_pilots_by_one_licence(airplane_type_id)

        counter = 0
        for pilot in pilots_info_list:
            name = pilot.get_name()
            counter += 1
            print("{}. {}".format(counter, name))

    def show_pilots_by_all_licences(self):
        ''' Displays pilots sorted by the aircraft type they have a licence for '''

        self.header("-", " PILOTS BY LICENCES ")

        pilots_by_licences_dict = self.llAPI.get_pilots_by_all_licences()
        for airplane_type, pilots_list in pilots_by_licences_dict.items():
            print("\n{}".format(airplane_type))
            counter = 0
            for pilot in pilots_list:
                name = pilot.get_name()
                counter += 1
                print("\t{}. {}".format(counter, name))
                

    def show_all_working(self):
        desired_date_str = input("Enter date (YYYY-MM-DD): ")

        self.header("-", " ALL STAFF MEMBERS WORKING ON {} ".format(desired_date_str))

        staff_working_dict = self.llAPI.get_all_working(desired_date_str)

        #Print the name of each staff member that is working
        for dest_id, staff_id_list in staff_working_dict.items():
            destination = self.llAPI.get_destination_info(dest_id)
            counter = 1
            for staff_id in staff_id_list:
                staff_member = self.llAPI.get_staff_member_info(staff_id)
                name = staff_member.get_name()
                dest_city = destination.get_city()
                print("{} {} is going to {}".format("-", name, dest_city))
                counter += 1

    def show_all_not_working(self):
        desired_date_str = input("Enter date (YYYY-MM-DD): ")

        self.header("-", " ALL STAFF MEMBERS NOT WORKING ON {} ".format(desired_date_str))

        staff_not_working_list = self.llAPI.get_all_not_working(desired_date_str)

        #Print the name of each staff member that is not working
        for staff_member_id in staff_not_working_list:
            staff_member = self.llAPI.get_staff_member_info(staff_member_id)
            name = staff_member.get_name()
            print("{} {}".format("-", name))

    def show_staff_member_schedule(self):

        start_of_desired_week_str = input("Please enter the start of your desired week (YYYY-MM-DD): ")

        counter = 0
        staff_info_list = self.llAPI.get_all_staff()
        self.header("-", " ALL STAFF ")

        for staff_member in staff_info_list:
            ssn = staff_member[0]
            name = staff_member[1]
            counter += 1
            print("{:>3}. {:<25} ssn: {:<15}".format(counter, name, ssn))
        choice = input("\nChoose the number staff member whose schedule you want to see: ")

        desired_ssn = staff_info_list[int(choice) - 1][0]
        desired_name = staff_info_list[int(choice) - 1][1]
        working_voyages_list = self.llAPI.get_staff_member_schedule(desired_ssn, start_of_desired_week_str)
        
        if working_voyages_list: # if staff member has any voyages for the chosen week
            print()
            print(desired_name + " is going to:")
            for voyage in working_voyages_list:
                dest_id = voyage.get_dest_id()
                dest_info = self.llAPI.get_destination_info(dest_id)
                dest_city = dest_info.get_city()
                date = voyage.get_departure_out()   # Takes only the date from the string
                print("\t{} on {}".format(dest_city, date))
        
        else:
            print("{} has no voyages for the week you chose!".format(desired_name))
        
    def create_staff_member(self):
        ''' Creates an new staff member with information that's input from the user '''

        ### displays the header and main body
        self.header("-", " ADD STAFF MEMBER ")
        ssn_str = ""
        name_str = ""
        role_str = ""
        rank_str = ""
        licence_str = ""
        address_str = ""
        phone_number_str = ""
        email_str = ""

        # ---- Initialize an empty instance of Staff Member ----
        new_staff_member = StaffMember()
        
        # ---- Set ssn ----
        new_info_str = "\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}\n".format(ssn_str, name_str, role_str, rank_str, licence_str, address_str, phone_number_str, email_str)
        print(new_info_str)
        ssn_str = input("Enter new ssn: ")
        while not self.validation.validate_ssn(ssn_str):
            ssn_str = input("The ssn you entered is invalid. Please enter a new one: ")
        new_staff_member.set_new_ssn(ssn_str)

        # ---- Set name ----
        new_info_str = "\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}\n".format(ssn_str, name_str, role_str, rank_str, licence_str, address_str, phone_number_str, email_str)
        print(new_info_str)
        name_str = input("Enter new name: ")
        while not self.validation.validate_name(name_str):
            name_str = input("The name you entered is invalid: Please enter a new one: ")
        new_staff_member.set_new_name(name_str)

        # ---- Set role ----
        new_info_str = "\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}\n".format(ssn_str, name_str, role_str, rank_str, licence_str, address_str, phone_number_str, email_str)
        print(new_info_str)
        role_list = ["Pilot", "Flight Attendant"]
        print("\n1. {}\n2. {}".format(role_list[0], role_list[1]))
        role_choice = input("\nEnter number of new role: ")
        if role_choice == "1":
            role_str = "Pilot"
            new_staff_member.set_new_role(role_str)
        elif role_choice == "2":
            role_str = "Flight Attendant"
            new_staff_member.set_new_role(role_str)

        # ---- Set rank ----
        new_info_str = "\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}\n".format(ssn_str, name_str, role_str, rank_str, licence_str, address_str, phone_number_str, email_str)
        print(new_info_str)
        rank_list = ["Captain", "Copilot", "Flight Service Manager", "Flight Attendant"]
        if new_staff_member.get_role() == "Pilot":
            print("\n  1. {}\n  2. {}".format(rank_list[0], rank_list[1]))
            rank_choice = input("\nEnter number of new role: ")

            if rank_choice == "1":
                rank_str = "Captain"
                new_staff_member.set_new_rank(rank_str)
            elif rank_choice == "2":
                rank_str = "Copilot"
                new_staff_member.set_new_rank(rank_str)
        
        elif new_staff_member.get_role() == "Flight Attendant":
            print("\n  1. {}\n  2. {}".format(rank_list[2], rank_list[3]))
            rank_choice = input("\nEnter number of new role: ")

            if rank_choice == "1":
                rank_str = "Flight Service Manager"
                new_staff_member.set_new_rank(rank_str)
            elif rank_choice == "2":
                rank_str = "Flight Attendant"
                new_staff_member.set_new_rank(rank_str)

        # ---- Set licence if applicable ----
        new_info_str = "\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}\n".format(ssn_str, name_str, role_str, rank_str, licence_str, address_str, phone_number_str, email_str)
        print(new_info_str)
        counter = 0
        airplane_type_list = self.llAPI.get_all_airplane_types()

        if new_staff_member.get_role() == "Pilot":
            print()
            for airplane_type in airplane_type_list:
                counter += 1
                print("{:>3}. Airplane type: {:<12}".format(counter, airplane_type))
            
            licence_choice = input("Please enter the number of desired licence for {}: ".format(name_str))
            licence_str = airplane_type_list[int(licence_choice) - 1]
            new_staff_member.set_new_licence(licence_str)
        
        elif new_staff_member.get_role() == "Flight Attendant":
            licence_str = "N/A"
            new_staff_member.set_new_licence(licence_str)
        
        # ---- Set address ----
        new_info_str = "\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}\n".format(ssn_str, name_str, role_str, rank_str, licence_str, address_str, phone_number_str, email_str)
        print(new_info_str)
        address_str = input("Enter new address: ")
        while not self.validation.validate_address(address_str):
            address_str = input("The address you entered is invalid. Please enter another one: ")
        new_staff_member.set_new_address(address_str)
        
        # ---- Set phone number ----
        new_info_str = "\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}\n".format(ssn_str, name_str, role_str, rank_str, licence_str, address_str, phone_number_str, email_str)
        print(new_info_str)
        phone_number_str = input("Enter new phone number: ")
        while not self.validation.validate_phone_num(phone_number_str):
            phone_number_str = input("The phone number you entered is invalid. Please enter another one. Hint: Only 7 numbers are allowed ;): ")
        new_staff_member.set_new_phone_number(phone_number_str)

        # ---- Set email ---- 
        new_info_str = "\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}\n".format(ssn_str, name_str, role_str, rank_str, licence_str, address_str, phone_number_str, email_str)
        print(new_info_str)
        email_str = input("Enter new email: ")
        while not self.validation.validate_email(email_str):
            email_str = input("The email you entered is invalid. Please enter another one. Hint: It has to end with '@nanair.is ;)': ")
        new_staff_member.set_new_email(email_str)

        # ---- Get confirmation from user ----
        new_info_str = "\n1. SSN: {}\n2. NAME: {}\n3. ROLE: {}\n4. RANK: {}\n5. LICENSE: {}\n6. ADDRESS: {}\n7. PHONE NUMBER: {}\n8. EMAIL ADDRESS: {}\n".format(ssn_str, name_str, role_str, rank_str, licence_str, address_str, phone_number_str, email_str)
        print(new_info_str)
        yes_or_no = input("Is all the information correct? (y/n): ")
        if yes_or_no == "y":
            self.llAPI.create_staff_member(new_staff_member)
            print("You did it! The new staff member has been stored in the database!")


    def change_staff_member_info(self):

            staff_instance_list = self.llAPI.get_all_staff()
            staff_instance_dictionary = {str(i+1): staff_instance_list[i] for i in range(len(staff_instance_list))}


            #prints header and main body of the menu for choosing a particular staff member
            self.header("*", " CHOOSE STAFF MEMBER ")
            for key,val in staff_instance_dictionary.items():
                print("{}. {}".format(key, val.get_name()))
            staff_choice = input("\nEnter which staff member you want to change: ")
            

            while staff_choice in staff_instance_dictionary.keys():
                instance = staff_instance_dictionary[staff_choice] #to make our lives easier
                 #shortens the code a bit

                self.header("*", " {} ".format(instance.get_name()))
                print("\n1. SSN: {}\n2. NAME: {}\n3. LICENSE: {}\n4. ADDRESS: {}\n5. PHONE NUMBER: {}\n6. EMAIL ADDRESS: {}".format(instance.get_ssn(), instance.get_name(), instance.get_licence(), instance.get_address(), instance.get_phone_number(), instance.get_email()))
                change_info_choice = input("\nEnter which info you want to change: ")

                if change_info_choice == "1":
                    print("Invalid: can't make changes to ssn")

                elif change_info_choice == "2":
                    print("Invalid: can't make changes to name")

                elif change_info_choice == "3":
                    print("Invalid: can't make changes to licence")

                elif change_info_choice == "4":
                    new_address_str = input("Enter new address: ")
                    if self.validation.validate_address(new_address_str):
                        instance.set_new_address(new_address_str)

                elif change_info_choice == "5":
                    new_phone_num_str = input("Enter new phone number: ")
                    if self.validation.validate_phone_num(new_phone_num_str):
                        instance.set_new_phone_number(new_phone_num_str)

                elif change_info_choice == "6":
                    print("Invalid: can't make changes to email address")

                elif change_info_choice == "confirm":
                    print("Changes have been confirmed")
                    return self.llAPI.store_new_staff_changes(staff_instance_list)

