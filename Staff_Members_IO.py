import csv
from models import StaffMember

class StaffMemberIO:
    def load_all_staff_from_file(self):
        staff_list = []
        with open("Staff_Members.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                staff_id = row["staff_id"]
                name = row["name"]
                role = row["role"]
                rank = row["rank"]
                licence = row["licence"]
                address = row["address"]
                phone_number = row["phone_number"]

                staff = StaffMember(staff_id, name, role, rank, licence, address, phone_number)
                staff_list.append(staff)
            
            return staff_list


