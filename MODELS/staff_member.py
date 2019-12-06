class StaffMember():
    def __init__(self, ssn, name, role, rank, licence, address, phone_number, email):
        self.__ssn = ssn
        self.__name = name
        self.role = role
        self.rank = rank
        self.licence = licence
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def get_ssn(self):
        return self.__ssn

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.role
    
    def get_licence(self):
        return self.licence

    def __str__(self):
        my_str = "Ssn: {}".format(self.__ssn)
        my_str += "\nName: {}".format(self.__name)
        my_str += "\nRole: {}".format(self.role)
        my_str += "\nLicence: {}".format(self.licence)
        my_str += "\nAddress: {}".format(self.address)
        my_str += "\nPhone number: {}".format(self.phone_number)
        my_str += "\nEmail: {}".format(self.email)

        return my_str