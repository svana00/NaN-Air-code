class Airplane():
    def __init__(self, name, plane_id, type_id, capacity): #status
        self.name = name
        self.id = plane_id
        self.type = type_id
        self.capacity = capacity
        #self.plane_status = plane_status

    def get_name(self):
        return self.name

    def get_plane_id(self):
        return self.id

    def get_type_id(self):
        return self.type

    def get_capacity(self):
        return self.capacity