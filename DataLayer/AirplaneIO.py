import csv
from MODELS.airplane import Airplane
from MODELS.airplane_type import AirplaneType

class AirplaneIO():
    def load_all_airplanes(self):
        airplanes_list = []
        
        airplanes_file = open("csv_files/Aircraft.csv", "r")
        planeType_file = open("csv_files/AircraftType.csv", "r")

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
    
    def load_airplane_types(self):
        types_list = []

        planeType_file = open("csv_files/AirplaneType.csv", "r")
        type_reader = csv.DictReader(planeType_file)

        for row in type_reader:
            type_id = row["planeTypeId"]
            type_manufacturer = row["manufacturer"]
            type_model = ["model"]
            type_capacity = ["capacity"]

            airplaneType = AirplaneType(type_id, type_manufacturer, type_model, type_capacity)
            types_list.append(airplaneType)

        return types_list

    def store_new_airplane_into_file(self, airplane_str):
        ''' Stores new airplane to the existing file '''
        airplane_file = open("csv_files/Airplane.csv", "a")
        airplane_file.write(airplane_str)
        airplane_file.write("\n")
        return airplane_file
