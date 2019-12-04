
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
        a_dict = dict()
        self.header("-", " ALL DESTINATIONS ")
        dest_list = self.llAPI.get_all_dest()
        for destination in dest_list:
            city = destination[0]
            country = destination[1]
            counter += 1
            a_dict[str(counter)] = destination
            print("{}. {}: {}".format(counter,country, city))
        
        ########  option to choose a specific destination
        input_choice = input("To choose a destination enter it's number: ")
        if input_choice in a_dict:
            self.display_destination(a_dict[input_choice])

    def display_destination(self, a_dest_info_list):
        self.header("*", " {} ".format(a_dest_info_list[0]))
        counter = 0
        for info in a_dest_info_list:
            counter += 1
            print("{}. {}".format(counter, info))

    def create_destination(self):
        destination_info_list = ["","","","","","",""]
        country_str = ""
        city_str = ""
        airport_str = ""
        flight_time_str = ""
        distance_str = ""
        name_of_contact_str = ""
        emergency_number_str = ""
        destination_dict_values_list = [country_str, city_str, airport_str, flight_time_str, distance_str, name_of_contact_str, emergency_number_str]
        destination_info_str = ["country", "city", "airport", "flight time", "distance", "name of contact", "emergency phone number"]
        input_text_list = ["please enter new {}: ".format(destination_info_str[i] for i in range(len(destination_info_str)))]
        destination_dict = { str(i+1) : destination_dict_values_list[i] for i in range(0, len(destination_dict_values_list) ) }

        # prints out the header and main body
        self.header("-", " ADD DESTINATION ")
        print("\n1. COUNTRY: {}\n2. CITY: {}\n3. AIRPORT: {}\n4. FLIGHT TIME: {}\n5. DISTANCE: {}\n6. NAME OF CONTACT: {}\n7. EMERGENCY PHONE: {}".format(country_str, city_str, airport_str, flight_time_str, distance_str, name_of_contact_str, emergency_number_str))
        choice = input("\n"+"Input what you want to add: ")

        ###### a while loop that asks for and replaces values for a new destination

        while choice in destination_dict.keys():
            new_value = input(input_text_list[int(choice) - 1]) # prints out the corresponding text to what the user wants to change and takes in the input
            destination_dict[choice] = new_value # changes the value in the dict to the entered value

            #### printing the header and modified main body ##
            self.header("-", " ADD VOYAGE ")
            for i in range(len(destination_dict_values_list)):
                print("{}. {}: {}".format((i+1), destination_info_str[i], destination_dict[str(i+1)]))
            print("To confirm changes enter confirm")
            #######

            choice = input("\nInput what you want to add: ")
        if choice == "confirm":
            return 0 ### need to find a way to return the list of values from the dict

        """
        while choice in VALID_LIST:
            
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
                print("Changes have been confirmed")
                return self.llAPI.create_new_destination(destination_info_list)

            self.header("-", " ADD DESTINATION ")
            print("\n1. COUNTRY: {}\n2. CITY: {}\n3. AIRPORT: {}\n4. FLIGHT TIME: {}\n5. DISTANCE: {}\n6. NAME OF CONTACT: {}\n7. EMERGENCY PHONE: {}".format(country_str, city_str, airport_str, flight_time_str, distance_str, name_of_contact_str, emergency_number_str))
            print("To confirm changes enter confirm")
            choice = input("\nInput what you want to add: ")
        return 
        """


    def change_destination_info(self):
        destination_name = ""
        self.header("-", destination_name)