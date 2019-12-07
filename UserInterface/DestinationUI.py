#from Validation.validation import Validate

class DestinationUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(13 - int((len(string)/2))) + string + form*(13 - int((len(string)/2))))

    def display_dest_menu(self):
        print("\n\n" + "*"*26 + "\n\t Destinations \n"+"*"*26)
        print("1. CHANGE\n2. OVERVIEW\n3. ADD")
        var = input("\nInput a command: ")
        if var == "1":
            self.change_destination_info()
        elif var == "2":
            self.show_destinations()
        elif var == "3":
            self.create_destination()

    def show_destinations(self):
        counter = 0
        self.header("-", " ALL DESTINATIONS ")
        dest_list = self.llAPI.get_destinations()

        for destination in dest_list:
            dest_id = destination[0]
            country = destination[1]
            city = destination[2]
            counter += 1
            print("{}. {}: {}".format(counter, country, city))

        choose_between = input("Do you want to see a specific destination? (y/n): ")
        if choose_between == "y":
            return self.show_destination_info(dest_list)

    def show_destination_info(self, dest_list):
        #Option to choose a specific destination
        choose_number = int(input("Enter number of destination: "))
        dest_id = dest_list[(choose_number) -1][0]
        destination = self.llAPI.get_destination_info(dest_id)
        self.header("-", " {} ".format(destination.get_city()))
        print(destination)

    def display_destination(self, a_dest_info_list):
        self.header("*", " {} ".format(a_dest_info_list[1]))
        counter = 0
        display_string = ["DESTINATION ID: ","CITY: ","COUNTRY: ", "AIRPORT: ", \
        "FLIGHT TIME: ", "DISTANCE: ","NAME OF CONTACT PERSONEL: ", "EMERGENCY PHONE NUMBER: "]

        for i in range(len(a_dest_info_list)):
            counter += 1
            print("{}. {} {}".format(counter, display_string[i] ,a_dest_info_list[i]))

    def create_destination(self):
        country_str = ""
        city_str = ""
        airport_str = ""
        flight_time_str = ""
        distance_str = ""
        name_of_contact_str = ""
        emergency_number_str = ""

        valid_input_list = ["1", "2", "3", "4", "5", "6", "7", "confirm"]
        destination_info_list = ["" for i in range(7)]

        self.header("-", " ADD DESTINATION ")
        print("\n1. COUNTRY: {}\n2. CITY: {}\n3. AIRPORT: {}\n4. FLIGHT TIME: {}\n5. DISTANCE: {}\n6. NAME OF CONTACT: {}\n7. EMERGENCY PHONE: {}"\
                .format(country_str, city_str, airport_str, flight_time_str, distance_str, name_of_contact_str, emergency_number_str))

        choice = input("\nInput which information you would like to add: ")

        while choice in valid_input_list:

            if choice == "1":
                country_str = input("\nEnter new country: ")
                destination_info_list[0] = country_str

            elif choice == "2":
                city_str = input("Enter new city: ")
                destination_info_list[1] = city_str

            elif choice == "3":
                airport_str = input("Enter new airport: ")
                destination_info_list[2] = airport_str

            elif choice == "4":
                flight_time_str = input("Enter new flight time: ")
                destination_info_list[3] = flight_time_str

            elif choice == "5":
                distance_str = input("Enter distance: ")
                destination_info_list[4] = distance_str

            elif choice == "6":
                name_of_contact_str = input("Enter name of contact: ")
                destination_info_list[5] = name_of_contact_str

            elif choice == "7":
                emergency_number_str = input("Enter emergency phone number: ")
                destination_info_list[6] = emergency_number_str

            elif choice == "confirm":
                print("Destination has been added")
                return self.llAPI.create_new_destination(destination_info_list)

            self.header("-", " ADD DESTINATION ")
            print("\n1. COUNTRY: {}\n2. CITY: {}\n3. AIRPORT: {}\n4. FLIGHT TIME: {}\n5. DISTANCE: {}\n6. NAME OF CONTACT: {}\n7. EMERGENCY PHONE: {}"\
                    .format(country_str, city_str, airport_str, flight_time_str, distance_str, name_of_contact_str, emergency_number_str))
            print("To confirm changes enter confirm")
            choice = input("\nInput what you want to add: ")

    def change_destination_info(self):
        dest_list = self.llAPI.get_all_dest()
        
        contact_str = ""
        
        emergency_number_str = ""
        
        valid_input_list  = ["1", "2", "confirm"]
        
        print("\n1. NAME OF CONTACT: {}\n2. EMERGENCY PHONE: {}".format(contact_str, emergency_number_str))
        
        choice =int(input("\nInput which information you would like to change: ")) #here hoices the user what dest he wants to change

        while choice in valid_input_list:
            print(dest_list)

            if choice == 1:
                contact_str = input("\n Enter new contact: ")
                dest_list[choice][0] = contact_str


            elif second_choice == 2:
                emergency_number_str = input("Enter new emergency number: ")
                dest_list[choice][1] = emergency_number_str

            elif choice == "confirm":
                print("Changes have been confirmed")
                return self.llAPI.change_destination(destination_info_list)

            self.header("-", " CHANGE DESTINATION ")
            print("\n1. NAME OF CONTACT: {}\n2. EMERGENCY PHONE: {}".format(contact_str, emergency_number_str))
            print("To confirm changes enter confirm")
            choice = input("\nInput what you want to add: ")

        destination_name = ""
        self.header("-", destination_name)

