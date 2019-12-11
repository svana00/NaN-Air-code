import csv
import datetime
from MODELS.staff_member import StaffMember
from MODELS.voyage import Voyage

class StaffMemberIO:
    
    def load_all_staff(self):
        ''' Returns a list of instances of all staff members '''
        name_list = []
        staff_file = open("csv_files/Staff_Members.csv", "r")
        reader = csv.DictReader(staff_file)

        for row in reader:
            ssn = row["ssn"]
            name = row["name"]
            role = row["role"]
            rank = row["rank"]
            licence = row["licence"]
            address = row["address"]
            phone_number = row["phone_number"]
            email = row["email"]
            staff_member = StaffMember(ssn,name,role,rank,licence,address,phone_number,email)
            name_list.append(staff_member)

        return name_list

    def store_new_staff_member(self,staff_member_str):
        ''' Stores new staff member to existing file '''
        staff_member_file = open("csv_files/Staff_Members.csv", "a+")
        staff_member_file.write(staff_member_str)

    def store_staff_member_info(self, staff_list):
        ''' Changes/adds info on a specific staff member '''
        big_csv = ""
        for staff in staff_list:
            big_csv += staff.instance_to_csv_string() + "\n"
        staff_file = open("csv_files/Staff_Members.csv", "w+")
        staff_file.write(big_csv)

    def load_work_schedule(self):
        ''' Gets work schedule for a specific staff member. Returns a dict with staff ID as the key 
            and a list of voyages the staff member has for the week as the value '''

        staff_member_file = open("csv_files/Staff_Members.csv", "r")
        voyages_file = open("csv_files/Voyages.csv", "r")

        staff_reader = csv.DictReader(staff_member_file)
        voyages_reader = csv.DictReader(voyages_file)

        start_date = "2019-11-04T05:32:00"
        end_date = datetime.datetime.fromisoformat("2019-11-04T05:32:00") + datetime.timedelta(days = 6)
        for i in voyages_reader:
            #if i % 2 != 0:
                #flight_num_out = voyages_reader[i]["flightNumber"]
            pass

beggi = StaffMemberIO()
beggi.load_work_schedule()