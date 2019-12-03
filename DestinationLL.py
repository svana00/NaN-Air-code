from models import Destination
from IOAPI import IOAPI

class DestinationLL():
    
    def getDestinations(self):
        IOAPI_temp = IOAPI()
        dest_list = IOAPI_temp.load_all_dest_from_file()
        dest_info_list = []

        for dest in dest_list:
            dest_country = dest.get_country()
            dest_city = dest.get_city()
            dest_info_list.append((dest_country, dest_city))
        
        return dest_info_list
    
    def createDestination(self):
        IOAPI_temp = IOAPI()
        dest_list = IOAPI_temp.load_all_dest_from_file()
        LLAPI_temp = LLAPI()
        new_input_dest_list = LLAPI.create_destination
        joined_list = new_input_dest_list + dest_list
        dest_str = ", ".join(joined_list)
        return IOAPI_temp.storeNewDestinationtoFile(dest_str)

    def changeDestinationInfo(self):
        pass