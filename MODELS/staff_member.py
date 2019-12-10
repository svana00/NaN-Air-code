class StaffMember():
    def __init__(self, ssn = "", name = "", role = "", rank = "", licence = "", address = "", phone_number = "", email = ""):
        self.__ssn = ssn
        self.__name = name
        self.role = role
        self.rank = rank
        self.licence = licence
        self.address = address
        self.phone_number = phone_number
        self.email = email


#------ get functions ---------
    def get_ssn(self):
        return self.__ssn

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.role
    
    def get_rank(self):
        return self.rank

    def get_licence(self):
        return self.licence

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email

#------- set functions  ---------

    def set_new_name(self, new_name):
        self.__name = new_name

    def set_new_licence(self, new_licence):
        self.licence = new_licence

    def set_new_address(self, new_address):
        self.address = new_address

    def set_new_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def set_new_email(self, new_email):
        self.email = new_email

    def instance_to_csv_string(self):
        csv_str = ""
        csv_str += "{},".format(self.__ssn)
        csv_str += "{},".format(self.__name)
        csv_str += "{},".format(self.role)
        csv_str += "{},".format(self.rank)
        csv_str += "{},".format(self.licence)
        csv_str += "{},".format(self.address)
        csv_str += "{},".format(self.phone_number)
        csv_str += "{},".format(self.email)
        
        return csv_str


#------- string function --------
    def __str__(self):
        my_str = ""
        my_str += "Ssn: {}\n".format(self.__ssn)
        my_str += "Name: {}\n".format(self.__name)
        my_str += "Role: {}\n".format(self.role)
        my_str += "Rank: {}\n".format(self.rank)
        my_str += "Licence: {}\n".format(self.licence)
        my_str += "Address: {}\n".format(self.address)
        my_str += "Phone number: {}\n".format(self.phone_number)
        my_str += "Email: {}\n".format(self.email)

        return my_str