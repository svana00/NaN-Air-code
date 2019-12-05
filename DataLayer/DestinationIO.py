import csv
from MODELS.destination import Destination

class DestinationIO: 
    def load_all_dest_from_file(self):
        dest_list = []
        dest_file = open("csv_files/Destinations.csv", "r")
        reader = csv.DictReader(dest_file)

        for row in reader:
            dest_id = row["dest_id"]
            dest_country = row["country"]
            dest_city = row["city"]
            dest_airport = row["airport"]
            dest_flight_time = ["flight_time"]
            dest_distance = ["distance"]
            dest_contact = ["contact"]
            dest_emergency_number = ["emergency_number"]

            destination = Destination(dest_id, dest_country, dest_city, dest_airport, dest_flight_time, dest_distance, dest_contact, dest_emergency_number)
            dest_list.append(destination)
            
        return dest_list

    def storeNewDestinationtoFile(self,dest_str):
        ''' Stores new destination to the existing file '''
        dest_file = open("csv_files/Destinations.csv", "a")
        dest_file.write(dest_str + "\n" )
        return dest_file

    def storeDestinationInfo(self):
        ''' Changes/adds info to an existing destination '''
        pass
