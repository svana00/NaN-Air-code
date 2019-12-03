from models import Destination
from IOAPI import IOAPI

class DestinationLL():
    
    def getDestinations(self):
        IOAPI_temp = IOAPI()
        return IOAPI_temp.load_all_dest_from_file()
    
    def makeDestination(self):
        pass

    def changeDestinationInfo(self):
        pass
