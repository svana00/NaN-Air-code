import csv
from models import Airplane

class AirplaneIO:
    def load_all_airplanes(self):
        airplanes_list = []
        
        airplanes_file = open("Aircraft.csv", "r")
        planeType_file = open("AircraftType.csv", "r")

        planes_reader = csv.DictReader(airplanes_file)
        type_reader = csv.DictReader(planeType_file)

        for row in planes_reader:
            plane_name = row["name"]
            plane_id = row["planeId"]
            plane_type = row["planeTypeId"]

            for row2 in type_reader:
                if plane_type == row2["planeTypeId"]:
                    plane_capacity = row2["capacity"]
            
            airplane = Airplane(plane_name, plane_id, plane_type, plane_capacity)
            airplanes_list.append(airplane)

        return airplanes_list
