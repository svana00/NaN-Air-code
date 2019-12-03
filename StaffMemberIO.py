import csv
from models import StaffMember

class StaffMemberIO:
    
    def load_all_staff_from_file(self):
        ''' Returns a list of instances of all staff members '''
        name_list = []
        with open("Staff_Members.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]

                name_list.append(name)
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
