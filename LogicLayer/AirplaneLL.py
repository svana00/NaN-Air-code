from MODELS.airplane import Airplane

class AirplaneLL():

    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
    
    def getallAirplaneTypes(self):
        pass

    def getAirplaneState(self):
        pass

    def makeAirplane(self, new_airplane_list):
        airplane_str = ",".join(new_airplane_list)
        return self.ioAPI.create_new_airplane(airplane_str)