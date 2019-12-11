from MODELS.airplane import Airplane

class AirplaneLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
    
    def get_all_airplanes(self):
        airplane_info_list = self.ioAPI.load_all_airplanes()
        return airplane_info_list

    def getallAirplaneTypes(self):
        pass

    def getAirplaneState(self, instance_of_airplane):
        airplane_instance_list = self.ioAPI.load_all_airplanes()
        pass
        

    def makeAirplane(self, new_airplane_list):
        airplane_str = ",".join(new_airplane_list)
        return self.ioAPI.create_new_airplane(airplane_str)
    
    def get_airplane_state(self, airplane_instance):
        #instance_list = self.ioAPI.load_all_airplanes()
        pass
