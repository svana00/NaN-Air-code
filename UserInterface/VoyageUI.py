from Validation.validation import Validate
from MODELS.voyage import Voyage
import datetime
class VoyageUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI
        self.validation = Validate()

    def header(self, form, string):
        ''' Creates a header with the form as decoration before the chosen string '''
        print("\n\n"+form*(28 - int((len(string)/2))) + string + form*(28 - int((len(string)/2))))

    def display_voyages_menu(self):
        ''' Displays the main menu for voyages giving the user the 
            options to assign, see overview or create new voyage '''

        return_val = 0
        while return_val == 0:
            print("\n\n"+"*"*56 + "\n"+" "*int((56-len(" VOYAGES "))/2)+"VOYAGES"+" "*int((56-len(" VOYAGES "))/2)+"\n"+"*"*56)
            print("1. ASSIGN VOYAGE\n2. VOYAGES OVERVIEW\n3. CREATE VOYAGE")
            var = input("\nInput a command: ")

            if var == "b":
                return 0
            elif var == "h":
                return "*"
            elif var == "1":
                return_val = self.assign_voyage()
            elif var == "2":
                return_val = self.display_voyages_overview_menu() # menu for overview choices
            elif var == "3":
                return_val = self.create_voyage()

    def display_voyages_overview_menu(self):
        ''' Menu for choosing overview type for voyages '''

        return_val = 0
        while return_val == 0:
            self.header("-", " GET OVERVIEW ")
            print("1. ALL VOYAGES \n2. VOYAGES BY DATE \n3. VOYAGES BY WEEK")
            option = input("\nInput a command: ")
            if option == "b":
                return 0
            elif option == "h":
                return "*"
            elif option == "1":
                all_voyages_list = self.llAPI.get_all_voyages()
                return_val = self.show_voyages(all_voyages_list)
            elif option == "2":
                desired_date_str = input("Please enter your desired date (YYYY-MM-DD): ")
                while not self.validation.validate_date(desired_date_str):
                    desired_date_str = input("Invalid date: please try again: ")
                voyages_by_date = self.llAPI.get_voyages_by_date(desired_date_str)
                return_val = self.show_voyages(voyages_by_date)
            elif option == "3":
                start_of_desired_week_str = input("Please enter the start of your desired week (YYYY-MM-DD): ")
                while not self.validation.validate_date(start_of_desired_week_str):
                    start_of_desired_week_str = input("Invalid date: please try again: ")
                voyages_by_week = self.llAPI.get_voyages_by_week(start_of_desired_week_str)
                return_val = self.show_voyages(voyages_by_week)

    def show_voyages(self, voyage_list):
        ''' Shows all voyages from a list of voyages in a specific format '''

        return_val = 0
        while return_val == 0:

            self.header("-", " VOYAGES ")

            for num, voyage in enumerate(voyage_list, 1):
                voyage_id = voyage.get_voyage_id()
                dest_id = voyage.get_dest_id()
                destination =  self.llAPI.get_destination_info(dest_id)
                city = destination.get_city()
                departure_out = voyage.get_departure_out()

                if voyage.is_fully_assigned() == "True":
                    fully_assigned_str = " "
                else:
                    fully_assigned_str = " not "
                print("{:>2}. ID: {:<5} Destination: {:<20} Departure at: {:<15} {:<6}Voyage is{}fully assigned"\
                        .format(num, voyage_id, city, departure_out," ",fully_assigned_str))

            if voyage_list == []:
                choice = input("\nTo go back enter b, to go home enter h: ")
                if choice == "b":
                    return 0
                elif choice =="h":
                    return "*"

            # Users can choose whether they want to see more info about a specific voyage
            choice = input("\nDo you want to see more info about a specific voyage? (y/n): ")
            if choice == "y":
                number = int(input("Please enter number for voyage: "))
                return self.display_voyage(voyage_list, number)
            elif choice == "n":
                choice = input("To go back enter b, to go home enter h: ")
                if choice == "b":
                    return 0
                elif choice =="h":
                    return "*"

            elif choice == "b":
                return 0
            elif choice == "h":
                return "*"

    def display_voyage(self, voyage_list, number):
        ''' Displays a specific voyage from the list of voyages '''

        return_val = 0
        while return_val == 0:
            voyage = voyage_list[(number) - 1]
            voyage_id = voyage.get_voyage_id()

            self.header("-", " Voyage {} ".format(voyage_id))
            print(voyage)

            plane_id = voyage.get_plane_id()
            date_and_time = datetime.datetime.now()
            date_and_time_str = datetime.datetime.isoformat(date_and_time)

            # Get the current state of the plane
            airplane_state = self.llAPI.get_airplane_state(plane_id, date_and_time_str)

            print("Current state of voyage: {}".format(airplane_state))

            var = input("\nEnter b to go back and h to go to home page: ")

            if var == "b":
                return 0
            elif var == "h":
                return "*"
        
    def create_voyage(self):
        ''' Returns a list of information about a new voyage '''

        return_val = 0
        while return_val == 0:
            new_voyage = Voyage()
    
            # User chooses destination
            destinations_list = self.llAPI.get_destinations()
            counter = 1

            self.header("-", " CHOOSE DESTINATION ")
            for destination in destinations_list:
                city = destination.get_city()
                print("{}. {}".format(counter,city))
                counter += 1

            number = input("\nEnter number of desired destination for voyage: ")
            # Option to go back before creating voyage
            if number == "b":
                return 0
            elif number == "h":
                return "*"

            valid_list = [str(num) for num in range(len(destinations_list))]
            while number not in valid_list:
                    print("Invalid choice. Enter again.")
                    number = input("\nEnter number of desired destination for voyage: ")
            else:
                destination = destinations_list[(int(number) - 1)]
                dest_id = destination.get_id()
                city = destination.get_city()
                new_voyage.set_dest_id(dest_id)

            # ---- Choosing date for voyage ----
            self.header("-", " CHOOSE DATE ")
            date_str = input("Please enter a date for the voyage (YYYY-MM-DD): ")

            while not self.validation.validate_date(date_str):
                print("\nInvalid date.")
                date_str = input("Please enter another date for the voyage (YYYY-MM-DD): ")      

            # ---- Choosing time for voyage ----
            self.header("-", " CHOOSE TIME ")
            time_str = input("Please enter a time for the voyage (HH:MM:SS): ")

            while not self.validation.validate_time(time_str):
                print("\nInvalid time.")
                time_str = input("Please enter another time for the voyage (HH:MM:SS): ")

            # User enters a new date and time if it overlaps a departure of another voyage until they find an appropriate time
            departure_out_str = "T".join([date_str, time_str])

            while not self.llAPI.voyage_date_check(departure_out_str):
                print("\nInvalid departure time. There is already a plane leaving Keflavik at that hour.")
                
                departure_date = input("Please enter a new departure date for your voyage (YYYY-MM-DD): ")
                while not self.validation.validate_date(departure_date):
                    departure_date = input("Invalid date. Please enter a new departure date for your voyage (YYYY-MM-DD): ")

                departure_time = input("Please enter another time for the voyage (HH:MM:SS): ")
                while not self.validation.validate_time(time_str):
                    time_str = input("Invalid time. Please enter another time for the voyage (HH:MM:SS): ")
                
                departure_out_str = "T".join([departure_date, departure_time])
            
            new_voyage.set_departure_out(departure_out_str)
                
            self.header("-", " ADD VOYAGE ")
            print("\n1. DESTINATION: {}\n2. DATE: {}\n3. TIME OF FLIGHT FROM KEFLAVIK TO DESTINATION: {}".format(city, date_str, time_str))

            # ---- Get confirmation from user ----
            yes_or_no = input("Is all the information correct? (y/n): ")
            if yes_or_no == "y":
                self.llAPI.make_voyage(new_voyage)
                print("You did it! The new voyage has been stored in the database!")
            elif yes_or_no == "n":
                back_option = input("\nTo go back enter b, to go home enter h: ")
                if back_option == "b":
                    return 0
                elif back_option == "h":
                    return "*"
            
            # ------- Give the option of going back or home ------------
            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"
    
    def choose_voyage_to_assign(self):
        ''' Returns voyage instance chosen by user out of non assigned voyages '''

        return_val = 0
        while return_val == 0:
            voyages_list = self.llAPI.get_non_assigned_voyages() # List of instances

            # Choose voyage menu
            self.header("-", " CHOOSE VOYAGE ")
            for number, voyage in enumerate(voyages_list, 1):
                voyage_id = voyage.get_voyage_id()
                dest_id = voyage.get_dest_id()
                destination =  self.llAPI.get_destination_info(dest_id)
                city = destination.get_city()
                departure_out = voyage.get_departure_out()

                print("{:>2}. ID: {:<5} Destination: {:<20} Departure at: {:<15}".format(number, voyage_id, city, departure_out))

            choice = input("\nEnter number for desired voyage: ")
            valid_list = [str(num) for num in range(len(voyages_list))]

            while choice not in valid_list:
                print("Invalid choice")
                choice = input("\nEnter number for desired voyage: ")
            else:
                chosen_voyage = voyages_list[int(choice) - 1]
                return chosen_voyage

    def choose_airplane_for_voyage(self, chosen_voyage):
        ''' Returns airplane id for airplane chosen by user '''

        departure_out_str = chosen_voyage.get_departure_out()
        arrival_home_str = chosen_voyage.get_departure_home()

        airplane_id_list = self.llAPI.get_free_airplanes(departure_out_str, arrival_home_str)

        self.header("-", " CHOOSE AIRPLANE ")
        for number, airplane_id in enumerate(airplane_id_list, 1):
            airplane = self.llAPI.get_airplane(airplane_id)
            name = airplane.get_name()
            print("{}. {} ".format(number, name))

        choice = input("\nEnter number for desired plane: ")
        plane_id = airplane_id_list[int(choice) - 1]

        return plane_id

    def choose_staff_member(self, staff_member_list):
        ''' Template for showing a list of staff members when assigning staff to voyage '''

        return_val = 0
        while return_val == 0:
            for number, staff_member in enumerate(staff_member_list, 1):
                ssn = staff_member.get_ssn()
                name = staff_member.get_name()
                print("{}. {:<25} ssn: {}".format(number, name, ssn))

            choice = input("\nEnter number for {}: ".format(staff_member.get_rank().lower()))
            chosen_staff_member = staff_member_list[int(choice) - 1]

            return chosen_staff_member

    def choose_pilots_for_voyage(self, captain_list, copilot_list):
        ''' Returns chosen captain and copilot for voyage '''

        return_val = 0
        while return_val == 0:
            # Choosing captain
            self.header("-", " CHOOSE CAPTAIN ")
            captain = self.choose_staff_member(captain_list)

            self.header("-", " CHOOSE COPILOT ")
            copilot = self.choose_staff_member(copilot_list)
            
            return captain, copilot

    def choose_flight_attendants_for_voyage(self, fsm_list, flight_attendant_list):
        ''' Returns chosen flight attendants for voyage '''

        return_val = 0
        while return_val == 0:
            # Choosing flight service manager
            self.header("-", " CHOOSE FLIGHT SERVICE MANAGER ")
            fsm = self.choose_staff_member(fsm_list)

            # Choosing flight attendant 1
            self.header("-", " CHOOSE FLIGHT ATTENDANT 1 ")
            fa1 = self.choose_staff_member(flight_attendant_list)
            flight_attendant_list.remove(fa1)

            # Choosing flight attendant 2
            self.header("-", " CHOOSE FLIGHT ATTENDANT 2 ")
            fa2 = self.choose_staff_member(flight_attendant_list)

            return fsm, fa1, fa2

    def assign_voyage(self):
        ''' Assigns plane and staff to a voyage that has not been assigned yet '''

        return_val = 0
        while return_val == 0:
            # Choose a voyage
            chosen_voyage = self.choose_voyage_to_assign()
            
            # Choose a plane
            plane_id = self.choose_airplane_for_voyage(chosen_voyage)

            chosen_voyage.set_plane_id(plane_id)
            chosen_airplane = self.llAPI.get_airplane(plane_id)

            # Find all staff members that are not busy at time of voyage
            departure_out_str = chosen_voyage.get_departure_out()
            arrival_home_str = chosen_voyage.get_departure_home()

            free_staff_departure_out = self.llAPI.get_all_not_working(departure_out_str)
            free_staff_arrival_home = self.llAPI.get_all_not_working(arrival_home_str)

            staff_members_id_list = list(set(free_staff_departure_out) & set(free_staff_arrival_home))
            staff_members_list = []

            for staff_member_id in staff_members_id_list:
                staff_member = self.llAPI.get_staff_member_info(staff_member_id)
                staff_members_list.append(staff_member)

            # Sort staff members according to their role and rank
            captain_list = []
            copilot_list = []
            fsm_list = []
            flight_attendant_list = []

            for staff_member in staff_members_list:
                if staff_member.rank == "Captain" and staff_member.get_licence() == chosen_airplane.get_type_id():
                    captain_list.append(staff_member)
                elif staff_member.rank == "Copilot" and staff_member.get_licence() == chosen_airplane.get_type_id():
                    copilot_list.append(staff_member)
                elif staff_member.rank == "Flight Service Manager":
                    fsm_list.append(staff_member)
                elif staff_member.rank == "Flight Attendant":
                    flight_attendant_list.append(staff_member)

            # Choose pilots
            captain, copilot = self.choose_pilots_for_voyage(captain_list, copilot_list)

            # Choose flight attendants
            fsm, fa1, fa2 = self.choose_flight_attendants_for_voyage(fsm_list, flight_attendant_list)

            # Add cabin crew to voyage instance
            cabin_crew_list = [captain.get_ssn(), copilot.get_ssn(), fsm.get_ssn(), fa1.get_ssn(), fa2.get_ssn()]
            chosen_voyage.set_cabin_crew(cabin_crew_list)
            chosen_voyage.set_fully_assigned()

            self.header("-", " VOYAGE ")
            print(chosen_voyage)

            choice = input("\nIs this correct information (y/n)? ")

            if choice == "y":
                print("\nChanges have been confirmed")

                return self.llAPI.assign_voyage(chosen_voyage)