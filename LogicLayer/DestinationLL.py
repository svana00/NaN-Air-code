from MODELS.destination import Destination

class DestinationLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
   
    def get_destinations(self):
        ''' Returns a list of destination tuples containing id, country and city '''
        dest_list = self.ioAPI.load_all_dest_from_file()
        dest_info_list = []
    
        for dest in dest_list:
            dest_id = dest.get_id()
            country = dest.get_country()
            city = dest.get_city()
            dest_info_list.append((dest_id, country, city))
        
        return dest_info_list

    def get_mutable_destination_info_list(self):
        dest_list = self.ioAPI.load_all_dest_from_file()
        dest_info_list = []

        for dest in dest_list:
            dest_country = dest.get_country()
            dest_city = dest.get_city()
            dest_id = dest.get_id()
            dest_airport = dest.get_airport()
            dest_flight_time = dest.get_flight_time()
            dest_distance = dest.get_distance()
            dest_emergency = dest.get_emergency_number()
            mutable_info_list = [dest.get_contact(), dest.get_emergency_number()]
            #dest_info_list.append((dest_id, dest_country, dest_city, dest_airport, dest_flight_time, dest_distance, mutable_info_list))
            dest_info_list.append(dest_id)
        return mutable_info_list, dest_info_list

    def get_destination_info(self, dest_id):
        dest_list = self.ioAPI.load_all_dest_from_file()
        
        for dest in dest_list:
            if dest.get_id() == dest_id:
                return dest

    def lets_see_if_this_works(self):
        dest_instance_list = self.ioAPI.load_all_dest_from_file()
        return dest_instance_list
    
    def create_new_destination(self, dest_info_list):
        dest_str = ",".join(dest_info_list)
        return self.ioAPI.create_new_destination(dest_str)
    
    def store_new_dest_changes(self, dest_instance_list):
        return self.ioAPI.storeDestinationInfo(dest_instance_list)

    #def change_destination(self, old_str, new_str):
    #    old_file = self.ioAPI.get_all_file()
    #    new_file = open("Destinations_temp.csv", "w")
    #    for line in old_file:
    #        new_file.write(line.replace(old_str, new_str)
    #    return self.ioAPI.change_destination()