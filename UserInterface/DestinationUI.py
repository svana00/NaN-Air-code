from Validation.validation import Validate
from MODELS.destination import Destination

class DestinationUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI
        self.validation = Validate()
    
    def going_back(self):
        ''' Gives the user the option to go back when called '''

        variable = input("\nTo go back enter b, to go home enter h: ")
        if variable == "b":
                return 0
        elif variable == "h":
            return "*"

    def header(self, form, string):
        ''' Creates a header with the form as decoration before the chosen string '''

        print("\n\n"+form*(28 - int((len(string)/2))) + string + form*(28 - int((len(string)/2))))

    def display_dest_menu(self):
        ''' Displays a submenu for the user to choose between actions they want to do with destinations '''

        return_val = 0
        while return_val == 0:
            print("\n\n"+"*"*56 + "\n"+" "*int((56-len(" DESTINATIONS "))/2)+" DESTINATIONS "+" "*int((56-len(" DESTINATIONS "))/2)+"\n"+"*"*56)
            print("1. CHANGE DESTINATION\n2. DESTINATIONS OVERVIEW\n3. ADD NEW DESTINATION")
            var = input("\nInput a command: ")

            _ = True
            while _:
                if var == "1":
                    _ = False
                    return_val = self.change_destination()
                elif var == "2":
                    _ = False
                    return_val = self.show_destinations()
                elif var == "3":
                    _ = False
                    return_val = self.create_destination()
                elif var == "b":
                    return 0
                elif var == "h":
                    return "*"
                else:
                    var = input("Whoops! Invalid input. Please try again: ")
        if return_val == "*":
            return "*"

    def show_destinations(self):
        ''' Shows a listing of all destinations '''

        return_val = 0
        while return_val == 0:
            counter = 0
            self.header("-", " ALL DESTINATIONS ")
            dest_list = self.llAPI.get_destinations()

            for destination in dest_list:
                country = destination.get_country()
                city = destination.get_city()
                counter += 1
                print("{:>3}. {}: {}".format(counter, country, city))
            choice = input("\nDo you want to see a specific destination? (y/n): ")
            if choice == "y":
                return_val = self.show_destination_info(dest_list)

            elif choice == "n":
                choice = input("\nEnter b to go back or h to go home: ")
                while True:
                    if choice == "b":
                        return 0
                    elif choice == "h":
                        return "*"
            else:
                choice = input("Whoops! Invalid input. Try again: ")
            
    def show_destination_info(self, dest_list):
        ''' Shows more information about a specific destination '''

        return_val = 0
        while return_val == 0:
            choice = int(input("Please enter number of destination: "))
            dest_id = dest_list[(choice) -1].get_id() # Matches choice to the index of the list
            destination = self.llAPI.get_destination_info(dest_id)
            self.header("-", " {} ".format(destination.get_city()))
            print(destination)

            back_option = input("To go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"

    def create_destination(self):
        ''' Creates a new destination for NaN-Air with information input from user '''

        # ---- Initialize a new instance of Destination with information as empty strings ----
        new_destination = Destination()

        self.header("-", " ADD DESTINATION ")

        choice = input("\nEnter b to go back, h to go home, or any other letter to start adding a new destination: ")
        if choice == "b":
            return 0
        elif choice == "h":
            return "*"

        # ---- Set the country of desired destination ----
        self.header("=", " ENTER COUNTRY ")
        print(new_destination)
        new_country_str = input("Please input the country of your desired destination: ")
        while not self.validation.validate_name(new_country_str):
            new_country_str = input("The country you entered is invalid. Please enter a new one: ")
        new_destination.set_country(new_country_str)

        # ---- Set the city of desired destination ----
        self.header("=", " ENTER CITY ")
        print(new_destination)
        new_city_str = input("Please input the city of your desired destination: ")
        while not self.validation.validate_name(new_city_str):
            new_city_str = input("The city you entered is invalid. Please enter a new one: ")
        new_destination.set_city(new_city_str)

        # ---- Set new destination ID ----
        self.header("=", " ENTER DESTINATION ID ")
        print(new_destination)
        new_dest_id_str = input("Please enter the ID of {}: ".format(new_city_str))

        # Get all destinations to avoid using the same ID
        dest_id_list = []
        dest_list = self.llAPI.get_destinations()
        for dest in dest_list:
            dest_id_list.append(dest.get_id())

        while new_dest_id_str in dest_id_list or not self.validation.validate_dest_id(new_dest_id_str):
            # Shows different error messages depending on user input error
            if new_dest_id_str in dest_id_list:
                new_dest_id_str = input("This destination ID is already in use. Please enter a new one: ")
            elif not self.validation.validate_dest_id(new_dest_id_str):
                new_dest_id_str = input("Please enter a new ID. It can only contain 3 uppercase letters: ")
        new_destination.set_id(new_dest_id_str)

        # ---- Set airport ----
        self.header("=", " ENTER AIRPORT ")
        print(new_destination)
        new_airport_str = input("Please enter the airport of {}: ".format(new_city_str))
        while not self.validation.validate_name(new_airport_str):
            new_airport_str = input("The airport you entered is invalid. Please refrain from using numbers: ")
        new_destination.set_airport(new_airport_str)

        # ---- Set flight time ----
        self.header("=", " ENTER FLIGHT TIME ")
        print(new_destination)
        new_flight_time_str = input("Please enter the flight time to {}: ".format(new_city_str))
        while not self.validation.validate_flight_time(new_flight_time_str):
            new_flight_time_str = input("Whoops! Invalid input. Please enter a positive integer between 1 and 10: ")
        new_destination.set_flight_time(new_flight_time_str)

        # ---- Set flight distance ----
        self.header("=", " ENTER FLIGHT DISTANCE ")
        print(new_destination)
        new_flight_distance_str = input("Please enter the flight distance in KM from KEF to {}: ".format(new_city_str))
        while not self.validation.validate_flight_distance(new_flight_distance_str):
            new_flight_distance_str = input("Invalid input. Please enter a positive integer smaller than 20,000: ")
        new_destination.set_distance(new_flight_distance_str)

        # ---- Set emergency contact ----
        self.header("=", " ENTER EMRGENCY CONTACT ")
        print(new_destination)
        new_contact_str = input("Please enter the name of the emergency contact for {}: ".format(new_city_str))
        while not self.validation.validate_name(new_contact_str):
            new_contact_str = input("Oh no! That name is invalid. Please enter a new name using only alphabetical letters: ")
        new_destination.set_new_contact(new_contact_str)

        # ---- Set emergency contact number ----
        self.header("=", "ENTER PHONE NUMBER OF CONTACT ")
        print(new_destination)
        new_contact_phone_str = input("Please enter the phone number of {}: ".format(new_contact_str))
        while not self.validation.validate_phone_num(new_contact_phone_str):
            new_contact_phone_str = input("Whoops! Only 7 number phone numbers are allowed. Please enter a new one: ")
        new_destination.set_new_emergency_number(new_contact_phone_str)

        # ---- Set flight number ID ----
        self.header("=", " ENTER FLIGHT NUMBER ID ")
        print(new_destination)
        new_flight_num_id = input("Please enter the two digit number used for creating flight numbers to {}: ".format(new_city_str))
        
        # Gets all destinations to avoid using the same ID when creating flight numbers
        flight_num_id_list = []
        dest_list = self.llAPI.get_destinations()
        for dest in dest_list:
            flight_num_id_list.append(dest.get_flight_number_id())
        
        while new_flight_num_id in flight_num_id_list or not self.validation.validate_flight_id(new_flight_num_id):
            # Shows different error messages depending on user input error
            if new_flight_num_id in flight_num_id_list:
                new_flight_num_id = input("That flight number ID is already in use. Please enter a new one: ")
            elif not self.validation.validate_flight_id(new_flight_num_id):
                new_flight_num_id = input("Invalid input. Please enter only two integers: ")
        new_destination.set_new_flight_num_id(new_flight_num_id)

        # ---- Confirm changes ----
        self.header("=", " CONFIRM ")
        print(new_destination)
        confirmation = input("Do you wish to save this information? (y/n): ")
        if confirmation == "y":
            self.llAPI.create_new_destination(new_destination)
            print("Ah, tres bien! The staff member has been stored in the database!")
        
        # Offers user to go back or home
        choice = input("\nEnter b to go back or h to go home: ")
        while True:
            if choice == "b":
                return 0
            elif choice == "h":
                return "*"
            else:
                choice = input("Whoops! Invalid input. Try again: ")

    def back_option(self, choice):
        if choice == "b":
            return 0
        elif choice == "h":
            return "*"

    def change_destination(self):
        ''' Lets the user change information about a specific destination '''

        return_val = 0
        while return_val == 0:
            dest_instance_list = self.llAPI.get_destinations()
            # Creates a dictionary with numbers as keys and instances of destinations as values
            dest_instance_dictionary = {str(i+1): dest_instance_list[i] for i in range(len(dest_instance_list))}
            self.header("*", " DESTINATIONS ")
            for counter, destination in dest_instance_dictionary.items():
                print("{:>3}. {}".format(counter, destination.get_city()))

            dest_choice = input("\nEnter which destination you want to change, or press b to go back or h to go home: ")
            if dest_choice == "b":
                return 0
            elif dest_choice == "h":
                return "*"

            # Sticks the user into an input loop until they are satisfied with the changes
            while dest_choice in dest_instance_dictionary.keys():
                destination = dest_instance_dictionary[dest_choice]
                self.header("*", " {} ".format(destination.get_city()))
                print("\n 1. NAME OF CONTACT: {}\n 2. EMERGENCY PHONE: {}".format(destination.get_contact(), destination.get_emergency_number()))
                change_info_choice = input("\nPlease enter number for info that you would like to change: ")
                
                if change_info_choice == "1":
                    new_contact_str = input("Please enter name of new contact: ")
                    while not self.validation.validate_name(new_contact_str):
                        new_contact_str = input("The name you entered is invalid. Please entere a new one: ")
                    destination.set_new_contact(new_contact_str)
                    
                elif change_info_choice == "2":
                    return_val = self.back_option(change_info_choice)
                    new_emergency_number_str = input("Please enter emergency number for contact: ")
                    while not self.validation.validate_phone_num(new_emergency_number_str):
                        new_emergency_number_str = input("The phone numebr you entered is invalid. Please enter one with 7 consecutive integers: ")
                    destination.set_new_emergency_number(new_emergency_number_str)

                else:
                    print("\nInvalid choice, please try again")

                choice = input("\nDo you want to make more changes? (y/n): ")
                if choice == "n":
                    return_val = self.llAPI.store_new_dest_changes(dest_instance_list)
                if choice == "y":
                    continue

                return self.back_option(choice)