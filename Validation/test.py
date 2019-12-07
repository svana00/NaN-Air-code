import datetime

a_str = "1 2 3 4 5 6"
b_str = a_str.replace(" ", "")
print(b_str.isdigit())

nde_str = "sigurdur@nanair.is"
siggf  = nde_str.split("@")
print(siggf)
nd = int(1)

year = int(input("Enter a year: "))
month = int(input("Enter a month "))
day = int(input("Enter a day: "))
hour = int(input("Enter a hour: "))
minute = int(input("Enter a minute: "))
second = int(input("Enter a second: "))
date_list = []

start_date = datetime.datetime(year, month, day, hour, minute, second)
for index in range(7):
    end_date = start_date + datetime.timedelta(days=index)
    end_date = end_date.isoformat()
    date = datetime.datetime.fromisoformat(end_date)
    date_list.append(date.isoformat())
print(date_list)
    #print(start_date)
    #print(end_date)

emailstr = "amotm@nanair.is"
e_list = emailstr.split("@")
counter = 0
if e_list[1] == "nanair.is":
        counter += 1
if counter >= len(e_list):
        print("lests ")


class Validate:
    def __init__(self):
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
        email_list = email_str.split("@")

    def validate_address(self, address_str):
        pass

    def validate_plane_type(self):
        pass

    def validate_plane_id(self, plane_id_str):
        """TF-XXX"""
        pass

    def validate_time(self, year, month, day, hour, minute, second):
        try:
            new_date = datetime.datetime(year, month, day, hour, minute, second)
            return new_date
        except ValueError:
            return -1


    def check_if_working(self): # we don't need this
        pass

    def validate_destination(self, dest_str):
        pass

    def validate_arrival(self, arrival_str):
        pass

    def validate_flight_num(self, flight_num_str):
        pass

