class Airplane():
    def __init__(self, name = "", plane_id = "", type_id = ""): #status
        self.__name = name
        self.__plane_id = plane_id
        self.__type_id = type_id

    #------- get functions -----------
    def get_name(self):
        return self.__name

    def get_plane_id(self):
        return self.__plane_id

    def get_type_id(self):
        return self.__type_id

    #------- set functions -----------
    def set_name(self, new_name):
        self.__name = new_name 
    
    def set_plane_id(self, new_plane_id):
        self.__plane_id = new_plane_id

    def set_type_id(self, new_type_id):
        self.__type_id = new_type_id

    def instance_to_csv_string(self):
        ''' Makes a csv string from airplane instance '''
        csv_list = [self.__name, self.__plane_id, self.__type_id]

        csv_str = ",".join(csv_list)

        return csv_str

    #------- string function -----------
    def __str__(self):
        my_str = ""
        my_str += "NAME: {}\n".format(self.__name)
        my_str += "ID: {}\n".format(self.__plane_id)
        my_str += "TYPE: {}\n".format(self.__type_id)

        return my_str