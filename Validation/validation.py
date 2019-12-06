class Validate:
    def __init__(self):
        pass

    def check_if_letters(self):
        new_str = a_str.replace(" ", "")
        if new_str.isalpha() == True:
            return a_str
        else:
            return -1
        
    def check_if_number(self, a_str):
        new_str = a_str.replace(" ", "")
        if new_str.isdigit() == True:
            return a_str
        else:
            return -1

    def check_ssn(self, a_str):
        if len(a_str) == 10 and a_str.isdigit():
            return a_str
        else:
            return -1

    def check_phonenumber(self):
        if len(a_str) == 7 and a_str.isdigit():
            return a_str
        else:
            return -1

    def check_id(self)
        pass

    def check_email(self):
        #take the input and split by @ and by .
        #check if the first is all letters
        #check if the second is nanair.is
        #

    def check_address(self):
        pass

    def plane_type(self):
        pass

    def plane_id(self):
        pass

    def check_time(self):
        pass

    def check_if_working(self):
        pass

    def check_destination(self):
        pass

    def check_arrival(self):
        pass

    def check_flight_num(self):
        pass

