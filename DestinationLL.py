from models import Destination

class DestinationLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
   
    def get_destinations(self):
        dest_list = self.ioAPI.load_all_dest_from_file()
        dest_info_list = []
    
        for dest in dest_list:
            dest_country = dest.get_country()
            dest_city = dest.get_city()
            dest_info_list.append((dest_country, dest_city))
        
        return dest_info_list
    
    def create_new_destination(self, dest_info_list):
        dest_str = ",".join(dest_info_list)
        return self.ioAPI.create_new_destination(dest_str)

    def change_destinationInfo(self):
        pass