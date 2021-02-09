class DestinationLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
   
    def get_destinations(self):
        ''' Returns a list of instances of all destinations '''

        dest_list = self.ioAPI.load_all_destinations()
        return dest_list

    def get_destination_info(self, dest_id):
        ''' Filters out a single instance of a destination with its ID '''

        dest_list = self.ioAPI.load_all_destinations()
        
        for dest in dest_list:
            if dest.get_id() == dest_id:
                return dest
    
    def create_new_destination(self, new_destination):
        ''' Sends a new instance of a destination down to the database for storing '''

        return self.ioAPI.create_new_destination(new_destination)
    
    def store_new_changes(self, dest_instance_list):
        ''' Sends a list of all instances, with a specific instance changed, down to the database for storing '''
        
        return self.ioAPI.store_destination_changes(dest_instance_list)