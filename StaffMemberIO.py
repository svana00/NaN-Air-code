import csv
from models import StaffMember

class StaffMemberIO:
    
    def load_all_staff_from_file(self):
        ''' Returns a list of instances of all staff members '''
        name_list = []
        with open("Staff_Members.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                ssn = row["ssn"]
                name = row["name"]
                role = row["role"]
                rank = ["rank"]
                licence = ["license"]
                address = ["address"]
                phone_number = ["phone_number"]
                staff_member = StaffMember(ssn,name,role,rank,licence,address,phone_number)
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
