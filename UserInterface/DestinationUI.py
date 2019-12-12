from Validation.validation import Validate
from MODELS.destination import Destination

class DestinationUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI
        self.validation = Validate()
    
    def going_back(self):
        variable = input("\nTo go back enter b, to go home enter h: ")
        if variable == "b":
                return 0
        elif variable == "h":
            return "*"

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(28 - int((len(string)/2))) + string + form*(28 - int((len(string)/2))))

    def display_dest_menu(self):
        #I've added back and home
        return_val = 0
        while return_val == 0:
            print("\n\n"+"*"*56 + "\n"+" "*int((56-len(" DESTINATIONS "))/2)+" DESTINATIONS "+" "*int((56-len(" DESTINATIONS "))/2)+"\n"+"*"*56)
            print("1. CHANGE\n2. OVERVIEW\n3. ADD NEW")
            var = input("\nInput a command: ")
            if var == "1":
                #self.change_destination_info()
                return_val = self.change_destination()
            elif var == "2":
                return_val = self.show_destinations()
            elif var == "3":
                return_val = self.create_destination()
            elif var == "b":
                return 0
            elif var == "h":
                return "*"
        if return_val == "*":
            return "*"

    def show_destinations(self):
        #added back and home
        return_val = 0
        while return_val == 0:
            counter = 0
            self.header("-", " ALL DESTINATIONS ")
            dest_list = self.llAPI.get_destinations()

            for destination in dest_list:
                country = destination.get_country()
                city = destination.get_city()
                counter += 1
                print("{}. {}: {}".format(counter, country, city))

            choose_between = input("\nDo you want to see a specific destination? (y/n): ")
            if choose_between == "y":
                return_val = self.show_destination_info(dest_list)
            elif choose_between == "b":
                return 0
            elif choose_between == "h":
                return "*"

    def show_destination_info(self, dest_list):
        #Option to choose a specific destination
        #added back and home
        return_val = 0
        while return_val == 0:
            choose_number = int(input("Enter number of destination: "))
            dest_id = dest_list[(choose_number) -1].get_id()
            destination = self.llAPI.get_destination_info(dest_id)
            self.header("-", " {} ".format(destination.get_city()))
            print(destination)
            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"

    def display_destination(self, a_dest_info_list):
        #added back and home
        return_val = 0
        while return_val == 0:
            self.header("*", " {} ".format(a_dest_info_list[1]))
            counter = 0
            display_string = ["DESTINATION ID: ","CITY: ","COUNTRY: ", "AIRPORT: ", \
            "FLIGHT TIME: ", "DISTANCE: ","NAME OF CONTACT PERSONEL: ", "EMERGENCY PHONE NUMBER: "]

            for i in range(len(a_dest_info_list)):
                counter += 1
                print("{}. {} {}".format(counter, display_string[i] ,a_dest_info_list[i]))
            self.going_back()

    def create_destination(self):
        ''' Creates a new destination for NaN-Air with information input from user '''

        # ---- Initialize a new instance of Destination with information as empty strings ----
        new_destination = Destination()
        country_str = ""
        city_str = ""
        airport_str = ""
        flight_time_str = ""
        distance_str = ""
        name_of_contact_str = ""
        emergency_number_str = ""

        valid_input_list = ["1", "2", "3", "4", "5", "6", "7", "confirm"]
        chosen_input_list = set()

        self.header("-", " ADD DESTINATION ")
        new_info_str = "\n1. COUNTRY: {}\n2. CITY: {}\n3. AIRPORT: {}\n4. FLIGHT TIME: {}\n5. DISTANCE: {}\n6. NAME OF CONTACT: {}\n7. EMERGENCY PHONE: {}"\
                .format(country_str, city_str, airport_str, flight_time_str, distance_str, name_of_contact_str, emergency_number_str)
        print(new_info_str)

        choice = input("\nPlease enter the number corresponding to the information you would like to add: ")
        if choice == "b":
            return 0
        elif choice == "h":
            return "*"

        while choice in valid_input_list:

            if choice == "1":
                country_str = input("\nPlease enter the country of your desired destination: ")
                while not self.validation.validate_name(country_str):
                    if country_str == "b":
                        return 0
                    elif country_str == "h":
                        return "*"
                    country_str = input("The country you entered is invalid. Please enter a country using letters only: ")
                new_destination.set_country(country_str)
                chosen_input_list.add(choice)

            elif choice == "2":
                city_str = input("Please enter the city of your desired destination: ")
                while not self.validation.validate_name(city_str):
                    if city_str == "b":
                        return 0
                    elif city_str == "h":
                        return "*"
                    city_str = input("The city you entered is invalid. Please enter a city using letters only: ")
                new_destination.set_city(city_str)
                chosen_input_list.add(choice)

            elif choice == "3":
                airport_str = input("Please enter the airport of your desired destination: ")
                while not self.validation.validate_name(airport_str):
                    if airport_str == "b":
                        return 0
                    elif airport_str == "h":
                        return "*"
                    city_str = input("The airport you entered is invalid. Please enter an airport using letters only: ")
                new_destination.set_airport(airport_str)
                chosen_input_list.add(choice)

            elif choice == "4":
                flight_time_str = input("Please enter the flight time to your desired destination in whole hours: ")
                while not self.validation.validate_flight_time(flight_time_str):
                    if flight_time_str == "b":
                        return 0
                    elif flight_time_str == "h":
                        return "*"
                    flight_time_str = input("The flight time you entered is invalid. It has to be at least one hour. Please enter it again: ")
                new_destination.set_flight_time(flight_time_str)
                chosen_input_list.add(choice)

            elif choice == "5":
                distance_str = input("Please enter the distance between Keflavik airport and your desired destination in km: ")
                while not self.validation.validate_flight_distance(distance_str):
                    if distance_str == "b":
                        return 0
                    elif distance_str == "h":
                        return "*"
                    distance_str = input("Flight distance cannot be negative. Please enter it again: ")
                new_destination.set_distance(distance_str)
                chosen_input_list.add(choice)

            elif choice == "6":
                name_of_contact_str = input("Please enter the name of the emergency contact at your desired destination: ")
                while not self.validation.validate_name(name_of_contact_str):
                    if name_of_contact_str == "b":
                        return 0
                    elif name_of_contact_str == "h":
                        return "*"
                    name_of_contact_str = input("The name you entered is invalid. Please enter a new one using only letters: ")
                new_destination.set_new_contact(name_of_contact_str)
                chosen_input_list.add(choice)

            elif choice == "7":
                emergency_number_str = input("Please enter the number of the emergency contact at your desired destination: ")
                while not self.validation.validate_phone_num(emergency_number_str):
                    if emergency_number_str == "b":
                        return 0
                    elif emergency_number_str == "h":
                        return "*"
                    emergency_number_str = input("The phone number you entered is invalid. Please enter a new one. Hint: it can only contain 7 numbers ;): ")
                new_destination.set_new_emergency_number(emergency_number_str)
                chosen_input_list.add(choice)

            elif choice == "confirm":
                if len(chosen_input_list) == 7:
                    print("Great job! A new destination for NanAir has been registered to the system! Bon voyage!")
                    return self.llAPI.create_new_destination(new_destination)
                else:
                    print("Uh oh! There is still some information missing! Please continue filling it out.")

            self.header("-", " ADD DESTINATION ")
            new_info_str = "\n1. COUNTRY: {}\n2. CITY: {}\n3. AIRPORT: {}\n4. FLIGHT TIME: {}\n5. DISTANCE: {}\n6. NAME OF CONTACT: {}\n7. EMERGENCY PHONE: {}"\
                .format(country_str, city_str, airport_str, flight_time_str, distance_str, name_of_contact_str, emergency_number_str)
            print(new_info_str)
            choice = input("\nInput the number of what you want to add or type 'confirm' to confirm changes: ")
            self.back_option(choice)

        else: # choice not in valid_input_list:
            print("Whoops! Invalid input. We are guiding you back to the main page. Sorry for the inconvenience")

    def back_option(self,var):
        if var == "b":
            return 0
        elif var == "h":
            return "*"

    def change_destination(self):
        return_val = 0
        while return_val == 0:
            dest_instance_list = self.llAPI.get_destination_instance_list()
            dest_instance_dictionary = {str(i+1): dest_instance_list[i] for i in range(len(dest_instance_list))}
            self.header("*", " DESTINATIONS ")
            for key,val in dest_instance_dictionary.items():
                print("{}. {}".format(key, val.get_city()))

            dest_choice = input("\nEnter which destination you want to change: ")
            if dest_choice == "b":
                return 0
            elif dest_choice == "h":
                return "*"

            while dest_choice in dest_instance_dictionary.keys():
                self.header("*", " {} ".format(dest_instance_dictionary[dest_choice].get_city()))
                print("\n1. NAME OF CONTACT: {}\n2. EMERGENCY PHONE: {}".format(dest_instance_dictionary[dest_choice].get_contact(), dest_instance_dictionary[dest_choice].get_emergency_number()))
                change_info_choice = input("\nEnter which info you want to change: ")
                
                if change_info_choice == "1":
                    new_contact_str = input("Enter new contact: ")
                    if self.validation.validate_name(new_contact_str):
                        dest_instance_dictionary[dest_choice].set_new_contact(new_contact_str)
                        print("\n{}".format(dest_instance_dictionary[dest_choice]))
                    else:
                        print("\nInvalid name")

                elif change_info_choice == "2":
                    return_val = self.back_option(change_info_choice)
                    new_emergency_number_str = input("Enter new emergency number: ")
                    if self.validation.validate_phone_num(new_emergency_number_str):
                        dest_instance_dictionary[dest_choice].set_new_emergency_number(new_emergency_number_str)
                        print("\n{}".format(dest_instance_dictionary[dest_choice]))
                    else:
                        print("\nInvalid phone number")

                else:
                    print("\nInvalid choice, please try again")

                choice = input("\nDo you want to make more changes? (y/n): ")
                if choice == "n":
                    return_val = self.llAPI.store_new_dest_changes(dest_instance_list)
                return self.back_option(choice)