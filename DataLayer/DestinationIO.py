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
            dest_flight_time = row["flight_time"]
            dest_distance = row["distance"]
            dest_contact = row["contact"]
            dest_emergency_number = row["emergency_number"]
            dest_flight_number_id = row["flight_number_id"]

            destination = Destination(dest_id, dest_country, dest_city, dest_airport, dest_flight_time, dest_distance, dest_contact, dest_emergency_number, dest_flight_number_id)
            dest_list.append(destination)
            
        return dest_list

    def storeNewDestinationtoFile(self,dest_str):
        ''' Stores new destination to the existing file '''
        dest_file = open("csv_files/Destinations.csv", "a")
        dest_file.write(dest_str)
        dest_file.write("\n")
        return dest_file

    def storeDestinationInfo(self, dest_list):
        ''' Changes/adds info to an existing destination '''
        big_csv = ""
        for dest in dest_list:
            big_csv += dest.instance_to_csv_string() + "\n"
        dest_file = open("csv_files/Destinations.csv", "w+")
        dest_file.write(big_csv)


    def get_all_file(self):
        the_file = open("Destinations.csv", "r")
        return the_file
        