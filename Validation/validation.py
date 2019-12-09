import datetime

class Validate:
    def __init__(self):
        # bæta við 
        pass

    def validate_letter(self, letter_str):
        new_str = letter_str.replace(" ", "")
        if new_str.isalpha() == True:
            return letter_str
        else:
            return -1
        
    def validate_number(self, num_str):
        new_str = num_str.replace(" ", "")
        if new_str.isdigit() == True:
            return a_str
        else:
            return -1

    def validate_ssn(self, ssn_num):
        if len(ssn_num) == 10 and ssn_str.isdigit():
            return ssn_num
        else:
            return -1

    def validate_phone_num(self, phone_num_int):
        if len(phone_num_int) == 7 and a_str.isdigit():
            return a_str
        else:
            return -1

    def validate_email(self, email_str):
        #take the input and split by @ and by .
        #check if the first is all letters
        #check if the second is nanair.is
        #
        pass

    def validate_address(self, address_str):
        pass

    def validate_plane_type(self):
        pass

    def validate_plane_id(self, plane_id_str):
        """TF-XXX"""

        pass

    def validate_time(self, time):

        try:
            datetime.time(time)
            return True
        except ValueError:
            return False


    def validate_date(self, date):

        try:
            datetime.date.fromisoformat(date)
            return True
        except ValueError:
            return False


    def validate_departure(self, departure_date_and_time):
        voyage_list = self.llAPI.get_all_voyages()
        for voyage in voyage_list:
            temp_departure_datetime = voyage.get_departure_out()
            if temp_departure_datetime == departure_date_and_time:
                return False
        
        return True


    def validate_arrival(self, arrival_str):
        pass

    def validate_flight_num(self, flight_num_str):
        pass

