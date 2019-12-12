import csv
import datetime
from MODELS.voyage import Voyage

class VoyageIO():

    def load_all_voyages(self):
        ''' Reads into the database. Returns a list of all voyages as instances '''
        
        voyages_file = open("csv_files/Voyages.csv", "r")
        voyages_reader = csv.DictReader(voyages_file)
        voyages_list = []

        for row in voyages_reader:
            voyage_id = row["voyage_id"]
            flight_number_out = row["flight_num_out"]
            flight_number_back = row["flight_num_back"]
            departure_out = row["departure_out"]
            arrival_out = row["arrival_out"]
            departure_home = row["departure_home"]
            arrival_home = row["arrival_home"]
            destination_id = row["destination_id"]
            plane_id = row["plane_id"]
            captain = row["captain"]
            copilot = row["copilot"]
            fsm = row["fsm"] # Flight Service Manager
            fa1 = row["fa1"] # Flight Attendant 1
            fa2 = row["fa2"] # Flight Attendant 2
            fully_assigned = row["fully_assigned"]

            voyage = Voyage(voyage_id, flight_number_out, flight_number_back, departure_out, arrival_out, departure_home, arrival_home, destination_id, plane_id, captain, copilot, fsm, fa1, fa2, fully_assigned)
            voyages_list.append(voyage)

        return voyages_list

    def store_voyage_changes(self, voyages_list):
        ''' Adds plane and staff to specific voyage '''

        big_csv = self.get_csv_header()
        for voyage in voyages_list:
            big_csv += voyage.instance_to_csv_string() + "\n"
        voyages_file = open("csv_files/Voyages.csv", "w+")
        voyages_file.write(big_csv)

    def store_new_voyage(self, csv_str):
        ''' Stores a new voyages to the database '''
        
        voyage_file = open("csv_files/Voyages.csv", "a")
        voyage_file.write(csv_str)
        voyage_file.write("\n")
        return voyage_file

    def get_csv_header(self):
        ''' Gets the header from the csv file '''

        voyages_file = open("csv_files/Voyages.csv", "r")
        for index, line in enumerate(voyages_file):
            if index == 0:
                header = line
        
        return header