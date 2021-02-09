import csv
from MODELS.destination import Destination

class DestinationIO: 

    def load_all_destinations(self):
        ''' Reads into the database. Returns a list of all destinations as instances '''

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

    def store_new_destination(self, new_destination):
        ''' Stores new destination to the existing file '''

        destination_csv_str = new_destination.instance_to_csv_string() + "\n"
        dest_file = open("csv_files/Destinations.csv", "a+")
        dest_file.write(destination_csv_str)
        dest_file.close()

    def store_destination_changes(self, dest_list):
        ''' Changes/adds info to an existing destination '''

        big_csv = self.get_csv_header()
        for dest in dest_list:
            big_csv += dest.instance_to_csv_string() + "\n"
        dest_file = open("csv_files/Destinations.csv", "w+")
        dest_file.write(big_csv)
    
    def get_csv_header(self):
        ''' Gets the header from the csv file '''

        dest_file = open("csv_files/Destinations.csv", "r")
        for index, line in enumerate(dest_file):
            if index == 0:
                header = line
        
        return header