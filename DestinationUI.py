from LLAPI import LLAPI

class DestinationUI():

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