class Validate:
    def __init__(self):
        pass

    def check_if_letters(self):
        a_str = "hello is this the new number"
        new_str = a_str.replace(" ", "")
        if new_str.isalpha() == True:
            return a_str
        
    def check_if_number(self, a_str):
        new_str = a_str.replace(" ", "")
        if new_str.isdigit() == True:
            return a_str

    def check_ssn(self)

    def check_phonenumber(self)

    def check_id(self)