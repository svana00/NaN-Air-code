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

    def __str__(self):
        return "{}".format(self.__name)