from Validation.validation import Validate
from MODELS.staff_member import StaffMember

class StaffMemberUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI
        self.validation = Validate()

    def header(self, form, string):
        ''' Creates a header with the form as decoration before the chosen string '''

        print("\n\n"+form*(28 - int((len(string)/2))) + string + form*(28 - int((len(string)/2))))

    def footer(self, form):
        print("\n\n"+(form*56))

    def display_staff_menu(self):
        ''' Prints the main staff menu and calls the appropriate
            functions for the option that's picked '''
            
        return_val = 0
        while return_val == 0:

            print("\n\n"+"*"*56 + "\n"+" "*int((56-len(" STAFF "))/2)+" STAFF "+" "*int((56-len(" STAFF "))/2)+"\n"+"*"*56)
            print("1. CHANGE STAFF MEMBER\n2. OVERVIEW\n3. CREATE STAFF MEMBER")
            self.footer("_")
            var = input("\nInput a command: ")
            if var == "b":
                return 0
            elif var == "h":
                return "*"
            elif var == "1":
                return_val = self.change_staff_member_info()
            elif var == "2":
                return_val = self.choose_in_staff()
            elif var == "3":
                return_val =  self.create_staff_member()
            else:
                print("Invalid choice")

    def choose_in_staff(self):
        ''' Displays the submenu to choos between getting an overview of work schedules or staff members '''
        
        return_val = 0
        while return_val == 0:
            self.header("-", " OVERVIEW ")
            print("1. SEE STAFF OVERVIEW \n2. SEE WORK SCHEDULE")
            self.footer("_")
            choice = input("\nInput a command: ")
            if choice == "b":
                return 0
            elif choice == "h":
                return "*"
            elif choice == "1":
                return_val = self.pick_staff_sub_menu()
            elif choice == "2":
                return_val = self.work_schedule_sub_menu()
            else:
                print("Invalid choice")

    def pick_staff_sub_menu(self):
        ''' Displays the staff sub menu '''
        
        return_val = 0
        while return_val == 0:
            self.header("-", " PICK STAFF ")
            print("1. PILOTS \n2. FLIGHT ATTENDANTS \n3. ALL STAFF")
            pick_staff = input("\nInput a command: ")
            if pick_staff == "b":
                return 0
            elif pick_staff == "h":
                return "*"
            elif pick_staff == "1":
                return_val = self.pilot_sub_menu()
            elif pick_staff == "2":
                return_val = self.show_all_flight_attendants()
            elif pick_staff == "3":
                return_val = self.show_all_staff()
            else:
                print("Invalid choice")

    def pilot_sub_menu(self):
        ''' Displays the submenu for pilots '''
        
        return_val = 0
        while return_val == 0:
            self.header("-", " PICK STAFF SUBGROUP ")
            print("1. ALL PILOTS \n2. PILOTS BY LICENCE")
            choice = input("\nInput a command: ")
            if choice == "b":
                return 0
            elif choice == "h":
                return "*"
            elif choice == "1":
                return_val = self.show_all_pilots()
            elif choice == "2":
                return_val = self.pilot_licence_sub_menu()
            else:
                print("Invalid choice")

    def pilot_licence_sub_menu(self):
        ''' Displays the submenu for pilots to filter by licences '''
        
        return_val = 0
        while return_val == 0:
            self.header("-", " PICK LICENCE SUBGROUP ")
            print("1. OVERVIEW OF ALL LICENCES \n2. ONE PARTICULAR LICENCE")
            choice = input("\nInput a command: ")
            if choice == "b":
                return 0
            elif choice == "h":
                return "*"
            elif choice == "1":
                return_val = self.show_pilots_by_all_licences()
            elif choice == "2":
                return_val = self.show_pilots_by_one_licence()
            else:
                print("Invalid choice")

    def work_schedule_sub_menu(self):
        ''' Displays a sub menu for choosing more specific information for the user '''
        
        return_val = 0
        while return_val == 0:
            self.header("-", " WORK SCHEDULE ")
            print("1. SHOW ALL STAFF MEMBERS WORKING ON A SPECIFIC DAY \n2. SHOW ALL STAFF MEMBERS NOT WORKING ON A SPECIFIC DAY\
                    \n3. SHOW THE WORK SCHEDULE OF A SPECIFIC STAFF MEMBER FOR A SPECIFIC WEEK")
            choice = input("\nInput a command: ")

            if choice == "b":
                return 0
            elif choice == "h":
                return "*"

            elif choice == "1":
                return_val = self.show_all_working()

            elif choice == "2":
                return_val = self.show_all_not_working()

            elif choice == "3":
                return_val = self.show_staff_member_schedule()

            else:
                print("Invalid choice\nPlease try again")

    def show_staff_member_info(self, staff_info_list):
        ''' Prints more info about a specific staff member '''
        
        return_val = 0
        while return_val == 0:

            number = int(input("Please enter number for staff member: "))
            ssn = staff_info_list[(number) - 1].get_ssn()
            staff_member = self.llAPI.get_staff_member_info(ssn)
            self.header("-", " {} ".format(staff_member.get_name()))
            print(staff_member)
            choice = input("\nTo go back enter b, to go home enter h: ")
            if choice == "b":
                return 0
            elif choice == "h":
                return "*"

    def show_all_pilots(self):
        ''' Shows a listing of all pilots. Lets user choose if they want to see more info on a specific pilot '''
        
        return_val = 0
        while return_val == 0:
            counter = 0
            self.header("-", " ALL PILOTS ")
            pilots_list = self.llAPI.get_all_pilots()

            for pilot in pilots_list:
                name = pilot.get_name()
                counter += 1
                print("{:>3}. {}".format(counter, name))

            choice = input("\nDo you want to see more info about a specific staff pilot? (y/n): ")
            if choice == "y":
                return_val = self.show_staff_member_info(pilots_list)
            elif choice == "b" or choice == "n":
                return 0
            elif choice == "h":
                return "*"

    def show_all_flight_attendants(self):
        ''' Shows a listing of all Flight attendants. Lets user choose if 
            they want to see more info on a specific flight attendant '''

        return_val = 0
        while return_val == 0:

            counter = 0
            self.header("-", " ALL FLIGHT ATTENDANTS ")
            flight_attendants_list = self.llAPI.get_all_flight_attendants()

            for flight_attendant in flight_attendants_list:
                name = flight_attendant.get_name()
                counter += 1
                print("{:>3}. {}".format(counter, name))

            choice = input("\nDo you want to see more info about a specific flight attendant? (y/n): ")
            if choice == "y":
                return_val = self.show_staff_member_info(flight_attendants_list)
            elif choice == "b" or choice == "n":
                return 0
            elif choice == "h":
                return "*"


    def show_all_staff(self):
        ''' Shows a listing of all staff members. Lets user choose if they 
            want to see more info on a specific staff member '''

        return_val = 0
        while return_val == 0:
            counter = 0
            self.header("-", " ALL STAFF MEMBERS ")
            staff_list = self.llAPI.get_all_staff()
            for staff_member in staff_list:
                name = staff_member.get_name()
                counter +=1
                print("{:>3}. {}".format(counter, name))
                
            choice = input("\nDo you want to see more info about a specific staff member? (y/n): ")
            if choice == "y":
                return_val = self.show_staff_member_info(staff_list)
            elif choice == "b" or choice == "n":
                return 0
            elif choice == "h":
                return "*"


    def show_pilots_by_one_licence(self):
        ''' Shows a listing of all pilots that have a licence on a specific type of airplane '''
        
        return_val = 0
        while return_val == 0:
            self.header("-", " PICK ONE LICENCE ")
            airplane_types_info_list = self.llAPI.get_all_airplane_types()

            airplane_type_dict = {}
            counter = 0
            # Prints all pilots that have a specific licence
            for airplane_type_id in airplane_types_info_list:
                counter += 1
                airplane_type_dict[str(counter)] = airplane_type_id
                print("{:>3}. {}".format(counter, airplane_type_id))

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
                print("{:>3}. {}".format(counter, name))
            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"

    def show_pilots_by_all_licences(self):
        ''' Shows all pilots sorted by the airplane type they have a licence for '''
        
        return_val = 0
        while return_val == 0:
            self.header("-", " PILOTS BY LICENCES ")

            pilots_by_licences_dict = self.llAPI.get_pilots_by_all_licences()
            for airplane_type, pilots_list in pilots_by_licences_dict.items():
                print("\n{}".format(airplane_type))
                counter = 0
                for pilot in pilots_list:
                    name = pilot.get_name()
                    counter += 1
                    print("\t{:>3}. {}".format(counter, name))
            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"

    def show_all_working(self):
        ''' Shows a listing of all staff members working on a spcific day '''

        return_val = 0
        while return_val == 0:
            desired_date_str = input("Please enter a date (YYYY-MM-DD): ")
            if desired_date_str == "b":
                return 0
            elif desired_date_str == "h":
                return "*"

            while not self.validation.validate_date(desired_date_str):
                desired_date_str = input("Invalid input. You have to enter the date in the format (YYYY-MM-DD): ")

            self.header("-", " ALL STAFF MEMBERS WORKING ON {} ".format(desired_date_str))

            staff_working_dict = self.llAPI.get_all_working(desired_date_str)

            #Print the name of each staff member that is working
            for dest_id, staff_id_list in staff_working_dict.items():
                destination = self.llAPI.get_destination_info(dest_id)

                for staff_id in staff_id_list:
                    staff_member = self.llAPI.get_staff_member_info(staff_id)
                    name = staff_member.get_name()
                    dest_city = destination.get_city()
                    print("{:>3} {} is going to {}".format("-", name, dest_city))
                    
            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"

    def show_all_not_working(self):
        ''' Shows a listing of all staff members that are not working on a specific day '''
        
        return_val = 0
        while return_val == 0:
            desired_date_str = input("Please enter a date (YYYY-MM-DD): ")
            if desired_date_str == "b":
                return 0
            elif desired_date_str == "h":
                return "*"

            self.header("-", " ALL STAFF MEMBERS NOT WORKING ON {} ".format(desired_date_str))

            staff_not_working_list = self.llAPI.get_all_not_working(desired_date_str)

            #Print the name of each staff member that is not working
            for staff_member_id in staff_not_working_list:
                staff_member = self.llAPI.get_staff_member_info(staff_member_id)
                name = staff_member.get_name()
                print("{:>3} {}".format("-", name))

            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"

    def show_staff_member_schedule(self):
        ''' Shows a schedule for a specific staff member during a specific week '''

        return_val = 0
        while return_val == 0:

            start_of_desired_week_str = input("Please enter the start of your desired week (YYYY-MM-DD): ")
            if start_of_desired_week_str == "b":
                return 0
            elif start_of_desired_week_str == "h":
                return "*"

            counter = 0
            staff_info_list = self.llAPI.get_all_staff()
            self.header("-", " ALL STAFF ")

            for staff_member in staff_info_list:
                ssn = staff_member.get_ssn()
                name = staff_member.get_name()
                counter += 1
                print("{:>3}. {:<25} ssn: {:<15}".format(counter, name, ssn))

            choice = input("\nChoose the number staff member whose schedule you want to see: ")
            if choice == "b":
                return 0
            elif choice == "h":
                return "*"

            desired_ssn = staff_info_list[int(choice) - 1].get_ssn()
            desired_name = staff_info_list[int(choice) - 1].get_name()
            working_voyages_list = self.llAPI.get_staff_member_schedule(desired_ssn, start_of_desired_week_str)
            
            if working_voyages_list: # If staff member has any voyages for the chosen week
                print()
                print(desired_name + " is going to:")
                for voyage in working_voyages_list:
                    dest_id = voyage.get_dest_id()
                    dest_info = self.llAPI.get_destination_info(dest_id)
                    dest_city = dest_info.get_city()
                    date = voyage.get_departure_out()
                    print("\t{} on {}".format(dest_city, date))
            
            else:
                print("{} has no voyages for the week you chose!".format(desired_name))

            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"

    def create_staff_member(self):
        ''' Creates an new staff member with information that's input from the user '''

        return_val = 0
        while return_val == 0:
            # -------- displays the header and main body --------
            self.header("-", " ADD STAFF MEMBER ")

            # ---- Initialize an empty instance of Staff Member ----
            new_staff_member = StaffMember()
            
            # ---- Set ssn ----
            self.header("=", " ENTER SSN ")
            print(new_staff_member)
            ssn_str = input("Please enter new social security number: ")
            # --- Option to go back -----
            if ssn_str == "b":
                return 0
            elif ssn_str == "h":
                return "*"
            # ---- if user wants to keep going ------
            while not self.validation.validate_ssn(ssn_str):
                ssn_str = input("The ssn you entered is invalid. Please enter a new one: ")
            new_staff_member.set_new_ssn(ssn_str)

            # ---- Set name ----
            self.header("=", " ENTER NAME ")
            print(new_staff_member)
            name_str = input("Please enter new name: ")
            while not self.validation.validate_name(name_str):
                name_str = input("The name you entered is invalid: Please enter a new one: ")
            new_staff_member.set_new_name(name_str)

            # ---- Set role ----
            self.header("=", " CHOOSE ROLE ")
            print(new_staff_member)
            role_list = ["Pilot", "Flight Attendant"]
            print("\n1. {}\n2. {}".format(role_list[0], role_list[1]))
            role_choice = input("\nEnter number for new role: ")
            if role_choice == "1":
                role_str = "Pilot"
                new_staff_member.set_new_role(role_str)
            elif role_choice == "2":
                role_str = "Flight Attendant"
                new_staff_member.set_new_role(role_str)

            # ---- Set rank ----
            self.header("=", " CHOOSE RANK ")
            print(new_staff_member)
            rank_list = ["Captain", "Copilot", "Flight Service Manager", "Flight Attendant"]
            if new_staff_member.get_role() == "Pilot":
                print("\n1. {}\n2. {}".format(rank_list[0], rank_list[1]))
                rank_choice = input("\nEnter number for new rank: ")

                if rank_choice == "1":
                    rank_str = "Captain"
                    new_staff_member.set_new_rank(rank_str)
                elif rank_choice == "2":
                    rank_str = "Copilot"
                    new_staff_member.set_new_rank(rank_str)
            
            elif new_staff_member.get_role() == "Flight Attendant":
                print("\n  1. {}\n  2. {}".format(rank_list[2], rank_list[3]))
                rank_choice = input("\nEnter number for new rank: ")

                if rank_choice == "1":
                    rank_str = "Flight Service Manager"
                    new_staff_member.set_new_rank(rank_str)
                elif rank_choice == "2":
                    rank_str = "Flight Attendant"
                    new_staff_member.set_new_rank(rank_str)

            # ---- Set licence if applicable ----
            self.header("=", " CHOOSE LICENCE ")
            print(new_staff_member)
            counter = 0
            airplane_type_list = self.llAPI.get_all_airplane_types()

            if new_staff_member.get_role() == "Pilot":
                for airplane_type in airplane_type_list:
                    counter += 1
                    print("{}. Airplane type: {:<12}".format(counter, airplane_type))
                
                licence_choice = input("\nPlease enter the number of desired licence for {}: ".format(name_str))
                licence_str = airplane_type_list[int(licence_choice) - 1]
                new_staff_member.set_new_licence(licence_str)
            
            elif new_staff_member.get_role() == "Flight Attendant":
                licence_str = "N/A"
                new_staff_member.set_new_licence(licence_str)
            
            # ---- Set address ----
            self.header("=", " ENTER HOME ADDRESS ")
            print(new_staff_member)
            address_str = input("Please enter new address: ")
            while not self.validation.validate_address(address_str):
                address_str = input("The address you entered is invalid. Please enter another one: ")
            new_staff_member.set_new_address(address_str)
            
            # ---- Set phone number ----
            self.header("=", " ENTER PHONE NUMBER ")
            print(new_staff_member)
            phone_number_str = input("Please enter new phone number: ")
            while not self.validation.validate_phone_num(phone_number_str):
                phone_number_str = input("The phone number you entered is invalid. Please enter another one. Hint: Only 7 numbers are allowed ;): ")
            new_staff_member.set_new_phone_number(phone_number_str)

            # ---- Set email -------
            self.header("=", " ENTER EMAIL ADDRESS ")
            print(new_staff_member)
            email_str = input("Please enter new email address: ")
            while not self.validation.validate_email(email_str):
                email_str = input("The email you entered is invalid. Please enter another one. Hint: It has to end with '@nanair.is ;)': ")
            new_staff_member.set_new_email(email_str)

            # ---- Get confirmation from user ----
            print(new_staff_member)
            yes_or_no = input("Is all the information correct? (y/n): ")
            if yes_or_no == "y":
                self.llAPI.create_staff_member(new_staff_member)
                print("You did it! The new staff member has been stored in the database!")
            
            # ------- Give the option of going back or home ------------
            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"

    def change_staff_member_info(self):
        ''' Changes info about a specific staff member '''

        return_val = 0
        while return_val == 0:

            staff_members_list = self.llAPI.get_all_staff()

            # ----- Choosing a particular staff member ----
            self.header("*", " CHOOSE STAFF MEMBER ")
            for number, staff_member in enumerate(staff_members_list, 1):
                print("{}. {}".format(number, staff_member.get_name()))

            choice = input("\nEnter number for staff member you want to change: ")
            if choice == "b":
                return 0
            elif choice == "h":
                return "*"

            chosen_staff_member = staff_members_list[int(choice) - 1]

            # ---- Prints the chosen staff member ----
            self.header("*", " {} ".format(chosen_staff_member.get_name()))
            print(chosen_staff_member)

            print("Only a staff member's home address and phone number can be changed.")
            print("a: address  p: phone number")
            address_or_phone_number = input("\nPlease enter your choice: ")
            valid_choices_list = ["a", "p", "b", "h"] # All valid choices

            while address_or_phone_number not in valid_choices_list:
                # Lets users enter a choice until choice is valid
                address_or_phone_number = input("Invalid choice. Please try again: ")

            else:
                # ------- Changing home address ----------
                if address_or_phone_number == "a":
                    new_address = input("Please enter new address for {}: ".format(chosen_staff_member.get_name()))
                    while not self.validation.validate_address(new_address):
                        new_address = input("Invalid address. Please enter another address: ")
                    else:
                        chosen_staff_member.set_new_address(new_address)

                # ------- Changing phone number --------
                elif address_or_phone_number == "p":
                    new_phone_number = input("Please enter new phone number for {}: ".format(chosen_staff_member.get_name()))
                    while not self.validation.validate_phone_num(new_phone_number):
                        new_phone_number = input("Invalid phone number. Please enter another phone number: ")
                    else:
                        chosen_staff_member.set_new_phone_number(new_phone_number)

                elif choice == "b":
                    return 0

                elif choice == "h":
                    return "*"

            # ------ Prints chosen staff member with new information -----
            self.header("*", " {} ".format(chosen_staff_member.get_name()))
            print(staff_member)

            confirmation = input("Do you want to confirm these changes (y/n)? ")

            if confirmation == "y":
                print("Changes have been confirmed")
                staff_members_list[int(choice) - 1] = chosen_staff_member
                self.llAPI.store_new_staff_changes(staff_members_list)

                # ------- Give the option of going back or home ------------
                back_option = input("\nTo go back enter b, to go home enter h: ")
                if back_option == "b":
                    return 0
                elif back_option == "h":
                    return "*"

            # ------- Give the option of going back or home ------------
            elif confirmation == "n":
                back_option = input("\nTo go back enter b, to go home enter h: ")
                if back_option == "b":
                    return 0
                elif back_option == "h":
                    return "*"