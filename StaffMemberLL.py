from IOAPI import IOAPI

class StaffMemberLL():
    IOAPI_temp = IOAPI()

    def get_staff_member_info(self):
        pass

    def get_all_staff(self):
        ''' Returns a list of tuples with names and ssn of all staff members '''
        staff_list = self.IOAPI_temp.load_all_staff_from_file()
        staff_info_list = []

        for staff_member in staff_list:
            ssn = staff_member.get_ssn()
            name = staff_member.get_name()
            staff_info_list.append((ssn, name))
        
        return staff_info_list

    def get_all_flight_attendants(self):
        staff_list = self.IOAPI_temp.load_all_staff_from_file()
        flight_attendants_info_list = []

        for flight_attendant in staff_list:
            if flight_attendant.role == "Flight attendant":
                ssn = flight_attendant.get_ssn()
                name = flight_attendant.get_name()
                flight_attendants_info_list.append((ssn, name))

        return flight_attendants_info_list

    def get_pilots(self):
        ''' Returns a list of all instances of pilots '''
        staff_list = self.IOAPI_temp.load_all_staff_from_file()
        pilots_list = []

        for staff_member in staff_list:
            if staff_member.role == "Pilot":
                pilots_list.append(staff_member)
            
        return pilots_list

    def get_all_pilots(self):
        ''' Returns a list of tuples for each pilot, the tuple contains their ssn and name '''
        pilots_list = self.get_pilots()
        pilots_info_list = []

        for pilot in pilots_list:
            ssn = pilot.get_ssn()
            name = pilot.get_name()
            pilots_info_list.append((ssn, name))

        return pilots_info_list

    def get_pilots_by_one_license(self,planeTypeId):
        pilots_list = self.get_pilots()
        airplane_types_list = load_airplane_types()
        airplane_types_id = []
        pilots_info_list = []

        for airplane_type in airplane_types_list:
            airplane_type_id = airplane_type.get_plane_type_id()
            airplane_types_id.append(airplane_type_id)

        for pilot in pilots_list:
            if pilot.licence == planeTypeId:
                pilots_info_list.append(pilot)

    def get_pilots_by_all_licenses(self):
        #pilots_list = self.get_pilots()
        #pilots_info_list = []
        pass

    def get_all_working(self):
        pass

    def get_all_not_working(self):
        pass

    def get_staff_member_schedule(self):
        pass

    def create_staff_members(self):
        pass

    def change_staff_member_info(self):
        pass

staff = StaffMemberLL()
a_list = staff.get_all_pilots()
print(a_list)
