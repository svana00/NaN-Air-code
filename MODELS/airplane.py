class Airplane():
    def __init__(self, name, plane_id, type_id): #status
        self.name = name
        self.plane_id = plane_id
        self.type_id = type_id
        #self.plane_status = plane_status

    def get_name(self):
        return self.name

    def get_plane_id(self):
        return self.plane_id

    def get_type_id(self):
        return self.type_id

    def __str__(self): #status
        my_str = ""
        my_str += "Name: {}\n".format(self.name)
        my_str += "ID: {}\n".format(self.plane_id)
        my_str += "Type: {}\n".format(self.type_id)
        #self.plane_status = plane_status
        return my_str
