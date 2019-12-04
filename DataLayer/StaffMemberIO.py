import csv
from MODELS.staff_member import StaffMember

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

    def storeNewStaffMember(self):
        ''' Stores new staff member to existing file '''
        pass

    def storeStaffMemberInfo(self):
        ''' Changes/adds info on a specific staff member '''
        pass
