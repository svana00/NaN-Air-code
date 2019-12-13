import csv
from MODELS.airplane import Airplane
from MODELS.airplane_type import AirplaneType

class AirplaneIO():

    def load_all_airplanes(self):
        ''' Reads into the database. Returns an list of all airplanes as instances '''

        airplanes_list = []
        airplanes_file = open("csv_files/Airplane.csv", "r")
        airplane_type_file = open("csv_files/AirplaneType.csv", "r")
        planes_reader = csv.DictReader(airplanes_file)
        planne_type_reader = csv.DictReader(airplane_type_file)

        for row in planes_reader:
            plane_name = row["name"]
            plane_id = row["planeId"]
            plane_type = row["planeTypeId"]
        
        for row in planne_type_reader:
            if row["planeTypeId"] == plane_type:
                plane_capacity = row["capacity"]

            airplane = Airplane(plane_name, plane_id, plane_type, plane_capacity)
            airplanes_list.append(airplane)

        return airplanes_list
    
    def load_airplane_types(self):
        ''' Reads into the database. Returns a list of all instances of airplane types '''
        
        airplane_types_list = []

        planeType_file = open("csv_files/AirplaneType.csv", "r")
        type_reader = csv.DictReader(planeType_file)

        for row in type_reader:
            type_id = row["planeTypeId"]
            type_manufacturer = row["manufacturer"]
            type_model = ["model"]
            type_capacity = ["capacity"]

            airplaneType = AirplaneType(type_id, type_manufacturer, type_model, type_capacity)
            airplane_types_list.append(airplaneType)

        return airplane_types_list

    def store_new_airplane(self, new_airplane):
        ''' Stores new airplane to the existing file '''

        airplane_csv_str = new_airplane.instance_to_csv_string()
        airplane_file = open("csv_files/Airplane.csv", "a+")
        airplane_file.write(airplane_csv_str)
        airplane_file.close()
