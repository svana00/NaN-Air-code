    def get_all_airplanes(self):
        airplane_info_list = self.ioAPI.load_all_airplanes()
        return airplane_info_list

    def get_all_airplane_types(self):
        pass

    def get_airplane(self, plane_id):
        airplanes_list = self.ioAPI.load_all_airplanes()
        
        for airplane in airplanes_list:
            if airplane.get_plane_id() == plane_id:
                return airplane

    def make_airplane(self, new_airplane_list):
        airplane_str = ",".join(new_airplane_list)
        return self.ioAPI.create_new_airplane(airplane_str)


    def gets_int_list_and_returns_datetime_format(self, int_list):
        year = int_list[0]
        month = int_list[1]
        day = int_list[2]
        hour = int_list[3]
        minute = int_list[4]
        return datetime.datetime(year, month, day, hour, minute)

    def gets_instance_attribute_and_returns_int_list(self, voyage_attribute):
        temp_attribute = voyage_attribute
        temp_attribute_str = temp_attribute.replace("T","-").replace(":", "-")
        temp_attribute_str_list = temp_attribute_str.split("-")
        attribute_int_list = [int(i) for i in temp_attribute_str_list]
        return attribute_int_list
    
    def get_airplane_state(self, airplane_instance, chosen_time_and_date):
        """ gets an airplane and chosen time and returns the state of the chosen airplane """

        chosen_airplane = airplane_instance
        voyages_list = self.ioAPI.load_all_voyages() # List of all voyages
        airplane_state = "IDLE" # initializes the airplane state at IDLE
        NOW = datetime.datetime.fromisoformat(chosen_time_and_date)

        for voyage in voyages_list:
            voyage_plane = voyage.get_plane_id()

            departure1_int_list = self.gets_instance_attribute_and_returns_int_list(voyage.get_departure_out())
            departure1_date = self.gets_int_list_and_returns_datetime_format(departure1_int_list)

            arrival1_int_list = self.gets_instance_attribute_and_returns_int_list(voyage.get_arrival_out())
            arrival1_date = self.gets_int_list_and_returns_datetime_format(arrival1_int_list)

            departure2_int_list = self.gets_instance_attribute_and_returns_int_list(voyage.get_departure_home())
            departure2_date = self.gets_int_list_and_returns_datetime_format(departure2_int_list)

            arrival2_int_list = self.gets_instance_attribute_and_returns_int_list(voyage.get_arrival_home())
            arrival2_date = self.gets_int_list_and_returns_datetime_format(arrival2_int_list)

            if voyage_plane == chosen_airplane:

                if departure1_date <= NOW <= arrival1_date:
                    airplane_state = "in flight 1"
                elif departure2_date <= NOW <= arrival2_date:
                    airplane_state = "in flight 2"
                elif arrival1_date < NOW < departure2_date:
                    airplane_state = "in intermission" 
                else:
                    airplane_state = "booked to fly at {}".format(voyage.get_departure_out())

        return airplane_state


def overview_of_airplanes(self):
        #smá flipp
        counter = 0
        self.header("-", " ALL AIRPLANES ")
        airplane_info_list = self.llAPI.get_all_airplanes()

        chosen_date = input("Enter date in the format (YYYY-MM-DD): ")
        chosen_time = input("Enter the time in the format (HH:MM:00): ")

        for airplane in airplane_info_list:
            counter += 1
            airplane_name_str = airplane.get_name()
            airplane_id_str = airplane.get_plane_id()
            airplane_type_str =  airplane.get_type_id()    #2019-11-12T06:20:00
            date_and_time = chosen_date + "T" + chosen_time
            #chosen_time = datetime.datetime(2019,11,20,6,40,00)
            airplane_state_str = self.llAPI.get_airplane_state(airplane.get_plane_id(),date_and_time)
            print("{}. Name: {:<30} ID: {:<10} Type: {:<20} State: {:<15}".format(counter, airplane_name_str, airplane_id_str, airplane_type_str, airplane_state_str))
