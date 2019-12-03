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
    
    def makeDestination(self):
        pass

    def changeDestinationInfo(self):
        pass
