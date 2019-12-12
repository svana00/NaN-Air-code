from MODELS.destination import Destination

class DestinationLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
   
    def get_destinations(self):
        ''' Returns a list of destination tuples containing id, country and city '''
        dest_list = self.ioAPI.load_all_destinations()
        return dest_list

    def get_destination_info(self, dest_id):
        dest_list = self.ioAPI.load_all_destinations()
        
        for dest in dest_list:
            if dest.get_id() == dest_id:
                return dest

    def lets_see_if_this_works(self):
        dest_instance_list = self.ioAPI.load_all_destinations()
        return dest_instance_list
    
    def create_new_destination(self, new_destination):

        # ---- Create Destination ID ----
        new_dest_id = new_destination.get_city()[:3].upper()

        dest_list = self.ioAPI.load_all_destinations()
        for dest in dest_list:
            temp_dest_id = dest.get_id()
            if new_dest_id == temp_dest_id:
                new_dest_id = new_destination.get_country()[:3].upper()
        
        new_destination.set_id(new_dest_id)

        return self.ioAPI.create_new_destination(new_destination)
    
    def store_new_changes(self, dest_instance_list):
        return self.ioAPI.store_destination_changes(dest_instance_list)