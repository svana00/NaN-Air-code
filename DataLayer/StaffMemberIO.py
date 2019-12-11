import csv
import datetime
from MODELS.staff_member import StaffMember

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
        staff_member_file.close()

    def store_staff_member_info(self, staff_list):
        ''' Changes/adds info on a specific staff member '''

        big_csv = self.get_header()
        for staff in staff_list:
            big_csv += staff.instance_to_csv_string() + "\n"
        staff_file = open("csv_files/Staff_Members.csv", "w+")
        staff_file.write(big_csv)

    def get_header(self):
        ''' Returns the header from the file '''

        staff_file = open("csv_files/Staff_Members.csv", "r")
        for index, line in enumerate(staff_file):
            if index == 0:
                header = line
        staff_file.close()
        
        return header