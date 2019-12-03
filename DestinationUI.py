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
        self.header("-", " ADD DESTINATION ")
        print("")


    def change_destination_info(self):
        destination_name = ""
        self.header("-", destination_name)