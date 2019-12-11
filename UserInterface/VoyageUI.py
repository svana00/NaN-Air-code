from Validation.validation import Validate
class VoyageUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI
        self.validate = Validate()

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(28 - int((len(string)/2))) + string + form*(28 - int((len(string)/2))))

    def display_voyages_menu(self):
        """ displays the main menu for voyages giving the user 
        the options to change, add, or see overview of voyages """
        print("*"*56 + "\n"+" "*int((56-len(" VOYAGES "))/2)+"VOYAGES"+" "*int((56-len(" VOYAGES "))/2)+"\n"+"*"*56)
        print("1. ASSIGN\n2. OVERVIEW\n3. ADD")
        var = input("\nInput a command: ")
        if var == "1":
            self.assign_voyage()
        elif var == "2":
            self.overview_options() # menu for overview choices
        elif var == "3":
            self.create_voyage()

    def overview_options(self):
        """ menu for overview choices """
        self.header("-", " GET OVERVIEW ")
        print("1. ALL VOYAGES \n2. VOYAGES BY DATE \n3. VOYAGES BY WEEK")
        option = input("\nInput a command: ")
        if option == "1":
            all_voyages_list = self.llAPI.get_all_voyages()
            self.show_voyages(all_voyages_list)
        elif option == "2":
            desired_date_str = input("Please enter you desired date (YYYY-MM-DD): ")
            voyages_by_date = self.llAPI.get_voyages_by_date(desired_date_str)
            self.show_voyages(voyages_by_date)
        elif option == "3":
            start_of_desired_week_str = input("Please enter the start of your desired week (YYYY-MM-DD): ")
            voyages_by_week = self.llAPI.get_voyages_by_week(start_of_desired_week_str)
            self.show_voyages(voyages_by_week)

    def show_voyages(self, voyage_list):
        counter = 0

        self.header("-", " VOYAGES ")

        for voyage in voyage_list:
            counter += 1
            voyage_id = voyage.get_voyage_id()
            dest_id = voyage.get_dest_id()
            destination =  self.llAPI.get_destination_info(dest_id)
            city = destination.get_city()
            departure_out = voyage.get_departure_out()
            if voyage.is_fully_assigned():
                fully_assigned_str = " "
            else:
                fully_assigned_str = "not "
                #{1:<4}
            print("{:>2}. ID: {:<5} Destination: {:<20} Departure at: {:<15} {:<6}Voyage is{}fully assigned".format(counter, voyage_id, city, departure_out," ",fully_assigned_str))

        choice = input("\nDo you want to see more info about a specific voyage? (y/n): ")
        if choice == "y":
            return self.display_voyage(voyage_list)

    def display_voyage(self, voyage_list):
        number = int(input("Enter number of voyage: "))
        voyage = voyage_list[(number) - 1]
        voyage_id = voyage.get_voyage_id()
        self.header("-", " Voyage {} ".format(voyage_id))
        print(voyage)

    def create_voyage(self):
        ''' Returns a list of information about a new voyage '''
        voyage_info_list = []
 
        # User chooses destination
        destinations_list = self.llAPI.get_destinations()
        counter = 1

        self.header("-", " CHOOSE DESTINATION ")
        for destination in destinations_list:
            city = destination.get_city()
            print("{}. {}".format(counter,city))
            counter += 1

        valid_list = [str(num) for num in range(len(destinations_list))]
        invalid_input = True
        number = input("\nEnter number of desired destination for voyage: ")

        while invalid_input == True:
            if number in valid_list:
                destination = destinations_list[(int(number) - 1)]
                dest_id = destination.get_id()
                city = destination.get_city()
                voyage_info_list.append(dest_id)
                invalid_input = False
            else:
                print("Invalid choice. Enter again.")
                number = input("\nEnter number of desired destination for voyage: ")

        invalid_input = True

        # User chooses date for voyage
        self.header("-", " CHOOSE DATE ")
        date_str = input("Enter date of voyage (YYYY-MM-DD): ")

        while not self.validate.validate_date(date_str):
            print("Invalid date.")
            date_str = input("Enter date of voyage (YYYY-MM-DD): ")
        else:
            voyage_info_list.append(date_str)        

        # User chooses time for voyage
        self.header("-", " CHOOSE TIME ")
        time_str = input("Enter time of voyage (HH:MM:SS): ")

        while not self.validate.validate_time(time_str):
            print("Invalid time.")
            time_str = input("Enter time of voyage (HH:MM:SS): ")
        else:
            voyage_info_list.append(time_str)   

        self.header("-", " ADD VOYAGE ")
        print("\n1. DESTINATION: {}\n2. DATE: {}\n3. TIME OF FLIGHT FROM KEFLAVIK TO DESTINATION: {}".format(city, date_str, time_str))

        print("\nChanges have been confirmed")

        return self.llAPI.make_voyage(voyage_info_list)

    def assign_voyage(self):
        ''' Assigns plane and staff to a voyage that has not been assigned yet '''

        voyages_list = self.llAPI.get_non_assigned_voyages() # List of instances

        # Choose voyage menu
        self.header("-", " CHOOSE VOYAGE ")
        for number, voyage in enumerate(voyages_list, 1):
            voyage_id = voyage.get_voyage_id()
            dest_id = voyage.get_dest_id()
            destination =  self.llAPI.get_destination_info(dest_id)
            city = destination.get_city()
            departure_out = voyage.get_departure_out()

            print("{}. ID: {:<5} Destination: {:<20} Departure at: {:<15}".format(number, voyage_id, city, departure_out))

        choice = input("\nEnter number for desired voyage: ")

        # Get info about chosen voyage
        chosen_voyage = voyages_list[int(choice) - 1]
        departure_out_str = chosen_voyage.get_departure_out()
        arrival_home_str = chosen_voyage.get_departure_home()

        # Get list of all airplanes free at time of voyage
        airplane_id_set = self.llAPI.get_free_airplanes(departure_out_str, arrival_home_str)
        airplane_id_list = list(airplane_id_set)

        self.header("-", " CHOOSE PLANE ")

        for number, airplane_id in enumerate(airplane_id_list, 1):
            airplane = self.llAPI.get_airplane(airplane_id)
            name = airplane.get_name()
            print("{}. {}".format(number, name))

        choice = input("\nEnter number for desired plane: ")
        plane_id = airplane_id_list[int(choice) - 1]

        chosen_voyage.set_plane_id(plane_id) 
        airplane = self.llAPI.get_airplane(plane_id)

        free_staff_day_1 = self.llAPI.get_all_not_working(departure_out_str)
        free_staff_day_2 = self.llAPI.get_all_not_working(arrival_home_str)

        staff_members_id_list = list(set(free_staff_day_1) & set(free_staff_day_2))
        staff_members_list = []

        for staff_member_id in staff_members_id_list:
            staff_member = self.llAPI.get_staff_member_info(staff_member_id)
            staff_members_list.append(staff_member)

        captain_list = []
        copilot_list = []
        flight_service_manager_list = []
        flight_attendant_list = []

        for staff_member in staff_members_list:
            if staff_member.rank == "Captain" and staff_member.get_licence() == airplane.get_type_id():
                captain_list.append(staff_member)
            elif staff_member.rank == "Copilot" and staff_member.get_licence() == airplane.get_type_id():
                copilot_list.append(staff_member)
            elif staff_member.rank == "Flight Service Manager":
                flight_service_manager_list.append(staff_member)
            else:
                flight_attendant_list.append(staff_member)

        # Choosing captain
        self.header("-", " CHOOSE CAPTAIN ")
        for number, captain in enumerate(captain_list, 1):
            ssn = captain.get_ssn()
            name = captain.get_name()
            print("{}. {}, ssn: {}".format(number, name, ssn))

        choice = input("\nEnter number for captain: ")
        captain = captain_list[int(choice) - 1]

        # Choosing copilot
        self.header("-", " CHOOSE COPILOT ")
        for number, copilot in enumerate(copilot_list, 1):
            ssn = copilot.get_ssn()
            name = copilot.get_name()
            print("{}. {}, ssn: {}".format(number, name, ssn))

        choice = input("\nEnter number for copilot: ")
        copilot = copilot_list[int(choice) - 1]

        # Choosing flight service manager
        self.header("-", " CHOOSE FLIGHT SERVICE MANAGER ")
        for number, flight_service_manager in enumerate(flight_service_manager_list, 1):
            ssn = flight_service_manager.get_ssn()
            name = flight_service_manager.get_name()
            print("{}. {}, ssn: {}".format(number, name, ssn))
        
        choice = input("\nEnter number for flight service manager: ")
        flight_service_manager = flight_service_manager_list[int(choice) - 1]

        # Choosing flight attendant 1
        self.header("-", " CHOOSE FLIGHT ATTENDANT 1 ")
        for number, flight_attendant in enumerate(flight_attendant_list, 1):
            ssn = flight_attendant.get_ssn()
            name = flight_attendant.get_name()
            print("{}. {}, ssn: {}".format(number, name, ssn))

        choice = input("\nEnter number for flight attendant 1: ")
        flight_attendant_1 = flight_attendant_list[int(choice) - 1]

        flight_attendant_list.remove(flight_attendant_1)

        # Choosing flight attendant 2
        self.header("-", " CHOOSE FLIGHT ATTENDANT 2 ")
        for number, flight_attendant in enumerate(flight_attendant_list, 1):
            ssn = flight_attendant.get_ssn()
            name = flight_attendant.get_name()
            print("{}. {}, ssn: {}".format(number, name, ssn))

        choice = input("\nEnter number for flight attendant 2: ")
        flight_attendant_2 = flight_attendant_list[int(choice) - 1]

        cabin_crew_list = [captain.get_ssn(), copilot.get_ssn(), flight_service_manager.get_ssn(), \
                            flight_attendant_1.get_ssn(), flight_attendant_2.get_ssn()]

        chosen_voyage.set_cabin_crew(cabin_crew_list)
        chosen_voyage.set_fully_assigned()

        self.header("-", " VOYAGE ")
        print(chosen_voyage)
        choice = input("\nIs this correct information (y/n)? ")

        if choice == "y":
            print("\nChanges have been confirmed")

            return self.llAPI.assign_voyage(chosen_voyage)