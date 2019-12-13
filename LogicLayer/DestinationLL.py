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
        return self.ioAPI.create_new_destination(new_destination)
    
    def store_new_changes(self, dest_instance_list):
        return self.ioAPI.store_destination_changes(dest_instance_list)