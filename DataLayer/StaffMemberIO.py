import csv
import datetime
from MODELS.staff_member import StaffMember
from MODELS.voyage import Voyage

class StaffMemberIO:
    
    def load_all_staff_from_file(self):
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

    def loadStaffMemberfromFile(self):
        ''' Returns an instance of a specific staff member '''
        pass

    def store_new_staff_member(self,staff_member_str):
        ''' Stores new staff member to existing file '''
        staff_member_file = open("csv_files/StaffMember.csv", "a+")
        staff_member_file.write(staff_member_str)
        return staff_member_file

    def storeStaffMemberInfo(self):
        ''' Changes/adds info on a specific staff member '''
        pass

    def load_work_schedule(self):
        ''' Gets work schedule for a specific staff member. Returns a dict with staff ID as the key 
            and a list of voyages the staff member has for the week as the value '''

        staff_member_file = open("csv_files/Staff_Members.csv", "r")
        voyages_file = open("csv_files/PastFlights.csv", "r")

        staff_reader = csv.DictReader(staff_member_file)
        voyages_reader = csv.DictReader(voyages_file)

        start_date = "2019-11-04T05:32:00"
        end_date = datetime.datetime.fromisoformat("2019-11-04T05:32:00") + datetime.timedelta(days = 6)
        for i in len(voyages_reader):
            if i % 2 != 0:
                #flight_num_out = voyages_reader[i]["flightNumber"]
                pass
                



beggi = StaffMemberIO()
beggi.load_work_schedule()