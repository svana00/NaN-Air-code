import datetime

class StaffMemberLL():
    def __init__(self, ioAPI):
        self.ioAPI = ioAPI

    def get_staff_member_info(self, ssn):
        ''' Returns an instance of a staff member with given ssn '''
        staff_members_list = self.ioAPI.load_all_staff()
        for staff_member in staff_members_list:
            if staff_member.get_ssn() == ssn:
                return staff_member

    def get_all_staff(self):
        ''' Returns a list of instances of all staff members '''

        staff_list = self.ioAPI.load_all_staff()
        return staff_list

    def get_all_flight_attendants(self):
        ''' Returns a list of instances of all flight attendants '''

        staff_list = self.ioAPI.load_all_staff()
        flight_attendants_list = []

        for staff_member in staff_list:
            if staff_member.get_role() == "Flight Attendant":
                flight_attendants_list.append(staff_member)

        return flight_attendants_list

    def get_all_pilots(self):
        ''' Returns a list of all instances of pilots '''

        staff_list = self.ioAPI.load_all_staff()
        pilots_list = []

        for staff_member in staff_list:
            if staff_member.get_role() == "Pilot":
                pilots_list.append(staff_member)

        return pilots_list

    def get_pilots_by_one_licence(self, airplane_type_id):
        ''' Returns a list of tuples with names and ssn of all pilots
            with a specific licence '''

        pilots_list = self.get_all_pilots()
        pilots_list_with_licence = []

        for pilot in pilots_list:
            licence = pilot.get_licence()
            if licence == airplane_type_id:
                pilots_list_with_licence.append(pilot)

        return pilots_list_with_licence

    def get_pilots_by_all_licences(self):
        ''' Returns a dictionary where the keys are an airplane type
            and the value is a list of tuples for pilots that have the
            licence for that type '''

        pilots_list = self.get_all_pilots()
        pilots_by_licences_dict = {}

        for pilot in pilots_list:
            licence = pilot.get_licence()

            if licence in pilots_by_licences_dict:
                pilots_by_licences_dict[licence].append(pilot)
            else:
                pilots_by_licences_dict[licence] = [pilot]

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
        staff_member_list = self.ioAPI.load_all_staff()
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
        ''' Filters voyages to only voyages in the desired week where the target staff member is working '''

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

    def create_staff_member(self, new_staff_member):
        ''' Sends the new instance down to the database for storing '''

        return self.ioAPI.store_new_staff_member(new_staff_member)

    def store_new_staff_changes(self, staff_member_instance_list):
        ''' Sends an updated list of staff member isntances down to the database for storing ''' 
        
        return self.ioAPI.store_staff_changes(staff_member_instance_list)