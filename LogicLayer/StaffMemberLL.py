import datetime

class StaffMemberLL():
    def __init__(self, ioAPI):
        self.ioAPI = ioAPI

    def get_staff_member_info(self, ssn):
        ''' Returns an instance of a staff member with given ssn '''
        staff_members_list = self.ioAPI.load_all_staff_from_file()
        for staff_member in staff_members_list:
            if staff_member.get_ssn() == ssn:
                return staff_member

    def get_all_staff(self):
        ''' Returns a list of tuples with names and ssn of all staff members '''
        staff_list = self.ioAPI.load_all_staff_from_file()
        staff_info_list = []

        for staff_member in staff_list:
            ssn = staff_member.get_ssn()
            name = staff_member.get_name()
            staff_info_list.append((ssn, name))

        return staff_info_list

    def get_all_flight_attendants(self):
        ''' Returns a list of tuples with names and ssn of all flight attendants '''
        staff_list = self.ioAPI.load_all_staff_from_file()
        flight_attendants_info_list = []

        for flight_attendant in staff_list:
            if flight_attendant.role == "Flight attendant":
                ssn = flight_attendant.get_ssn()
                name = flight_attendant.get_name()
                flight_attendants_info_list.append((ssn, name))

        return flight_attendants_info_list

    def get_pilots(self):
        ''' Returns a list of all instances of pilots '''
        staff_list = self.ioAPI.load_all_staff_from_file()
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

    def get_pilots_by_one_licence(self,airplane_type_id):
        ''' Returns a list of tuples with names and ssn of all pilots
            with a specific licence '''
        pilots_list = self.get_pilots()
        pilots_info_list = []

        for pilot in pilots_list:
            ssn = pilot.get_ssn()
            name = pilot.get_name()
            licence = pilot.licence
            if licence == airplane_type_id:
                pilots_info_list.append((ssn, name))

        return pilots_info_list

    def get_all_airplane_types(self):
        ''' Returns a list of all instances of airplane types '''
        airplane_types_list = self.ioAPI.load_airplane_types()
        airplane_types_info_list = []

        for airplane_type in airplane_types_list:
            airplane_type_id = airplane_type.get_plane_type_id()
            airplane_types_info_list.append(airplane_type_id)

        return airplane_types_info_list

    def get_pilots_by_all_licences(self):
        ''' Returns a dictionary where the keys are an airplane type
            and the value is a list of tuples for pilots that have the
            licence for that type '''
        pilots_list = self.get_pilots()
        pilots_by_licences_dict = {}

        for pilot in pilots_list:
            ssn = pilot.get_ssn()
            name = pilot.get_name()
            licence = pilot.get_licence()

            if licence in pilots_by_licences_dict:
                pilots_by_licences_dict[licence].append((ssn, name))
            else:
                pilots_by_licences_dict[licence] = [(ssn, name)]

        return pilots_by_licences_dict

    def get_all_working(self, desired_date_str):
        ''' Returns a dictionary where they key is a destination and the value is a list of staff members
            that are working a specific day '''
        voyages_list = self.ioAPI.load_all_voyages()
        desired_date = datetime.datetime.fromisoformat(desired_date_str).date()
        working_staff_dict = {}

        for voyage in voyages_list:
            voyage_departure_out = voyage.get_departure_out()
            temp_date = datetime.datetime.fromisoformat(voyage_departure_out).date()

            if desired_date == temp_date:
                cabin_crew_list = voyage.get_cabin_crew()
                destination = voyage.get_dest_id()
                if cabin_crew_list != []:
                    working_staff_dict[destination] = cabin_crew_list
        
        return working_staff_dict

    def get_all_not_working(self, desired_date_str):
        ''' Returns a list of staff members that are not working a specific day '''
        voyages_list = self.ioAPI.load_all_voyages()
        staff_member_list = self.ioAPI.load_all_staff_from_file()
        desired_date = datetime.datetime.fromisoformat(desired_date_str).date()
        staff_working_list = []
        staff_not_working_list = []

        for voyage in voyages_list:
            voyage_departure_out = voyage.get_departure_out()
            temp_date = datetime.datetime.fromisoformat(voyage_departure_out).date()

            if desired_date == temp_date:
                cabin_crew = voyage.get_cabin_crew()
                if cabin_crew != []:
                    for staff_member in cabin_crew:
                        staff_working_list.append(staff_member)

        for staff_member in staff_member_list:
            ssn = staff_member.get_ssn()
            if ssn not in staff_working_list:
                staff_not_working_list.append(ssn)

        return staff_not_working_list

    def get_staff_member_schedule(self, ssn, start_of_desired_week_str):
        
        staff_member = self.get_staff_member_info(ssn)
        staff_member_id = staff_member.get_ssn()
        voyages_list = self.ioAPI.load_all_voyages()
        voyages_in_week_list = []
        voyages_for_staff_member_in_week_list = []

        start_of_desired_week = datetime.datetime.fromisoformat(start_of_desired_week_str).date()
        end_of_desired_week = datetime.datetime.fromisoformat(start_of_desired_week_str).date() + datetime.timedelta(days = 6)

        for voyage in voyages_list:
            temp_date = datetime.datetime.fromisoformat(voyage.get_departure_out()).date()
            if temp_date >= start_of_desired_week and temp_date <= end_of_desired_week:
                voyages_in_week_list.append(voyage)

        for voyage in voyages_in_week_list:
            cabin_crew_list = voyage.get_cabin_crew()
            if staff_member_id in cabin_crew_list:
                voyages_for_staff_member_in_week_list.append(voyage)

        return voyages_for_staff_member_in_week_list

    def create_staff_member(self,staff_member_info_list):
        staff_member_str = ",".join(staff_member_info_list)
        return self.ioAPI.store_new_staff_member(staff_member_str)

    def get_staff_member_instance_list(self):
        staff_member_instance_list = self.ioAPI.load_all_staff_from_file()
        return staff_member_instance_list

    def store_new_staff_changes(self, staff_member_instance_list):
        return self.ioAPI.store_staff_changes(staff_member_instance_list)