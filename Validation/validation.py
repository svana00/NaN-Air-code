import datetime

class Validate:

    def validate_name(self, letter_str):
        ''' Validates name inputs from user ''' 

        new_str = letter_str.replace(" ", "")
        if new_str.isalpha() == True:
            return True
        else:
            return False
        
    def validate_number(self, num_str):
        ''' Validate number inputs from user '''

        new_str = num_str.replace(" ", "")
        if new_str.isdigit() == True:
            return True
        else:
            return False

    def validate_ssn(self, ssn_num):
        ''' Validates ssn inputs from user '''

        if len(ssn_num) == 10 and ssn_num.isdigit():
            return True
        else:
            return False

    def validate_phone_num(self, phone_num_int):
        ''' Validate phone number inputs from user '''

        if len(phone_num_int) == 7 and phone_num_int.isdigit():
            return True
        else:
            return False

    def validate_email(self, email_str):
        ''' Validates email inputs from user ''' 

        if "@" in email_str:
            temp_email_list = email_str.split("@")
            if len(temp_email_list) == 2: 
                if temp_email_list[1] == "nanair.is":
                    return True
        return False

    def validate_address(self, address_str):
        ''' Validates address inputs from user '''

        temp_address_list = address_str.split(" ")
        if len(temp_address_list) == 2:
            if temp_address_list[0].isalpha() and temp_address_list[1].isdigit():
                return True
        return False

    def validate_plane_id(self, plane_id_str):
        ''' Validates plane ID inputs from user '''

        #"""TF-XXX"""
        if plane_id_str[:3] == "TF-":
            if len(plane_id_str[3:]) == 3 and plane_id_str[3:].isalpha() and plane_id_str[3:].isupper():
                return True
        
        return False

    def validate_time(self, time):
        ''' Validate time inputs from user '''

        try:
            datetime.time.fromisoformat(time)
            return True
        except ValueError:
            return False

    def validate_date(self, date):
        ''' Validates date inputs from user '''

        try:
            datetime.date.fromisoformat(date)
            return True
        except ValueError:
            return False

    def validate_departure(self, departure_date_and_time):
        ''' Validates departure date when creating a new voyage to ensure user is not creating a voyage in the past '''
        
        try:
            datetime.datetime.fromisoformat(departure_date_and_time)
        except ValueError:
            return False
        
        if departure_date_and_time <= datetime.datetime.now().isoformat():
            return False
        
        return True

    def validate_flight_time(self, flight_time):
        ''' Validates flight time inputs from user ''' 

        if int(flight_time) > 0:
            return True
        
        return False

    def validate_flight_distance(self, distance):
        ''' Validates flight distance inputs from user '''
        
        if int(distance) > 0:
            return True
        
        return False