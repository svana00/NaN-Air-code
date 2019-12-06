import csv
import datetime
#from MODELS.voyage import Voyage
#from MODELS.airplane import Airplane

class VoyageIO():
    def loadVoyagefromFile(self):
        pass

    def loadVoyagesbyDate(self):
        #date = "2019-11-10T06:18:00"

        voyages_file = open("csv_files/PastFlights.csv", "r")
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

    def loadnonAssignedVoyages(self):
        pass

    def storeStafftoVoyage(self,staffID):
        pass

    def storeNewVoyagetoFile(self):
        pass

    def loadStaffFromFile(self, staffID):
        pass

    def load_all_voy_flipp(self):
        
        voyages_file = open("csv_files/PastFlights.csv", "r")
        staff_file = open("csv/Staff_Members.csv", "r")
        dest_file = open("csv/Destinations.csv", "r")

        voyages_reader = csv.DictReader(voyages_file)
        staff_reader = csv.DictReader(staff_file)
        dest_reader = csv.DictReader(dest_file)

flippkisi = VoyageIO()
flippkisi.loadVoyagesbyDate()
