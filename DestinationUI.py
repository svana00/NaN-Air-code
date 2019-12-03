from LLAPI import LLAPI

class DestinationUI():

    def display_dest_menu(self):
        print("*"*26 + "\n\t Destinations \n"+"*"*26)
        print("1. CHANGE\n2. GET\n3. ADD")
        var = input("\nInput a command: ")
        if var == "1":
            pass
        elif var == "2":
            self.show_destinations()
        elif var == "3":
            pass

    def show_destinations(self):
        LLAPI_temp = LLAPI()
        dest_list = LLAPI_temp.get_all_dest()
        for destination in dest_list:
            city = destination[0]
            country = destination[1]
            print("{}: {}".format(country, city))

    def create_destination(self):
        pass

    def change_destination_info(self):
        pass