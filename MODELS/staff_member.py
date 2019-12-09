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