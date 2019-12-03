import csv
from models import StaffMember

class StaffMemberIO:
    
    def load_all_staff_from_file(self):
        name_list = []
        with open("Staff_Members.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]

                name_list.append(name)
            return name_list

    def loadStaffMemberfromFile(self):
        pass

    def storeNewStaffMember(self):
        pass

    def storeStaffMemberInfo(self):
        pass
