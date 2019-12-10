import csv
import datetime
from MODELS.voyage import Voyage

class VoyageIO():
    def loadVoyagefromFile(self):
        pass

    def loadVoyagesbyDate(self):
        #date = "2019-11-10T06:18:00"

        voyages_file = open("csv_files/Voyages.csv", "r")
        voyage_reader = csv.DictReader(voyages_file)

        start_date = datetime.datetime(2019, 11, 29, 6, 18, 0)
        end_date = start_date + datetime.timedelta(days=7)
        end_date = end_date.isoformat()
        date = datetime.datetime.fromisoformat(end_date)
        print(date)

        #for row in voyage_reader:
        #    depart_datetime = row["departure"]

        #    if depart_datetime >= start_date.isoformat() and depart_datetime <= end_date.isoformat():
        #        print(row["flightNumber"])

    def storeStafftoVoyage(self,staffID):
        pass

    def store_new_voyage(self, csv_str):
        voyage_file = open("csv_files/Voyages.csv", "a")
        voyage_file.write(csv_str)
        voyage_file.write("\n")
        return voyage_file

    def load_all_voyages(self):
        
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

flippkisi = VoyageIO()
flippkisi.loadVoyagesbyDate()
