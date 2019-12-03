import csv
from models import Destination

class DestinationIO: #ekki fast nafn
    def load_all_dest_from_all(self):
        dest_list = []
        with open("Destinations.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dest_country = row["country"]
                dest_city = row["city"]
                dest_list.append((dest_country, dest_city))
            return dest_list

    def storeNewDestinationtoFile(self):
        pass

    def storeDestinationInfo(self):
        pass
