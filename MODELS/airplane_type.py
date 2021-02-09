class AirplaneType():
    def __init__(self, plane_type_id, capacity):
        self.__plane_type_id = plane_type_id
        self.capacity = capacity

    #------- get functions -----------
    def get_plane_type_id(self):
        return self.__plane_type_id

    def get_capacity(self):
        return self.capacity