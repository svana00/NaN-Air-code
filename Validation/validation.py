import datetime

class Validate:
    def __init__(self):
        pass

    def validate_letter(self, letter_str):
        new_str = letter_str.replace(" ", "")
        if new_str.isalpha() == True:
            return True
        else:
            return False
        
    def validate_number(self, num_str):
        new_str = num_str.replace(" ", "")
        if new_str.isdigit() == True:
            return True
        else:
            return False

    def validate_ssn(self, ssn_num):
        if len(ssn_num) == 10 and ssn_num.isdigit():
            return True
        else:
            return False

    def validate_phone_num(self, phone_num_int):
        if len(phone_num_int) == 7 and phone_num_int.isdigit():
            return True
        else:
            return False

    def validate_email(self, email_str):
        if "@" in email_str:
            temp_email_list = email_str.split("@")
            if len(temp_email_list) == 2: 
                if temp_email_list[1] == "nanair.is":
                    return True
        return False

    def validate_address(self, address_str):
        temp_address_list = address_str.split(" ")
        if len(temp_address_list) == 2:
            if temp_address[0].isalpha() and temp_address[1].isdigit():
                return True
        return False

    def validate_plane_type(self):
        pass

    def validate_plane_id(self, plane_id_str):
        """TF-XXX"""

        pass

    def validate_time(self, time):

        try:
            datetime.time.fromisoformat(time)
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
    def validate_staff_working(self, staff_member_id, be):
        #voyage_list = self.llAPI.get_all_voyages()
        #for voyage in voyage_list:
        #    temp_staff_member_list = voyage.get_staff_members()
        #    if staff_member_id in temp_staff_member_list:
        #         return False
        pass

"""
hellu = Validate()
if hellu.validate_date("2000-03-18"):
    print("yaaaaaaaaas")
else:
    print("noooopeeeee")
"""