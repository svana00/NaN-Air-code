import csv
from models import Destination

class DestinationIO: 
    def load_all_dest_from_file(self):
        dest_list = []
        with open("Destinations.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dest_id = row[dest_id]
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

    def storeNewDestinationtoFile(self):
        pass

    def storeDestinationInfo(self):
        pass
