from models import Destination
from IOAPI import IOAPI

class DestinationLL():
    def getDestinations(self):
        return IOAPI.load_all_dest_from_file()
    
    def makeDestination(self):
        pass

    def changeDestinationInfo(self):
        pass
