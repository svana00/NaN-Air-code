from LLAPI import LLAPI

class DestinationUI():

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
        LLAPI_temp = LLAPI()
        dest_list = LLAPI_temp.get_all_dest()
        for destination in dest_list:
            city = destination[0]
            country = destination[1]
            counter += 1
            print("{}. {}: {}".format(counter,country, city))

    def create_destination(self):
        destination_info_list = ["","","","","","",""]
        self.header("-", " ADD DESTINATION ")
        
        country_str = ""
        city_str = ""
        airport_str = ""
        flight_time_str = ""
        distance_str = ""
        name_of_contact_str = ""
        emergency_number_str = ""
        
        print("\n1. COUNTRY: {}\n2. CITY: {}\n3. AIRPORT: {}\n4. FLIGHT TIME: {}\n5. DISTANCE: {}\n6. NAME OF CONTACT: {}\n7. EMERGENCY PHONE: {}".format(country_str, city_str, airport_str, flight_time_str, distance_str, name_of_contact_str, emergency_number_str))
        choice = input("\n"+"Input what you want to add: ")
        VALID_LIST = ["1","2","3","4","5","6","7", "confirm"]

        while choice in VALID_LIST:
            if choice == "1":
                country_str = input("\nEnter new country: ")
                print("\n"+country_str)
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

            self.header("-", " ADD DESTINATION ")
            print("\n1. COUNTRY: {}\n2. CITY: {}\n3. AIRPORT: {}\n4. FLIGHT TIME: {}\n5. DISTANCE: {}\n6. NAME OF CONTACT: {}\n7. EMERGENCY PHONE: {}".format(country_str, city_str, airport_str, flight_time_str, distance_str, name_of_contact_str, emergency_number_str))
            choice = input("\nInput what you want to add: ")
            print(destination_info_list)
        return destination_info_list




    def change_destination_info(self):
        destination_name = ""
        self.header("-", destination_name)