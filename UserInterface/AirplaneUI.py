import datetime
from MODELS.airplane import Airplane
from Validation.validation import Validate

class AirplaneUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI
        self.validation = Validate()

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(28 - int((len(string)/2))) + string + form*(28 - int((len(string)/2))))

    def display_airplane_menu(self):
        print("*"*56 + "\n"+" "*int((56-len(" AIRPLANES "))/2)+" AIRPLANES "+" "*int((56-len(" AIRPLANES "))/2)+"\n"+"*"*56)
        print("1. OVERVIEW\n2. ADD AIRPLANES\n")
        user_choice = input("Input a command: ")

        if user_choice == "1":
            self.overview_of_airplanes()
        elif user_choice == "2":
            self.create_airplane()
        else:
            print("invalid choice\nPlease try again")
            self.display_airplane_menu()

    #def display_airplane_overview_menu(self):
    #    self.header("*", " PICK AIRPLANE OVERVIEW SUBGROUP ")
    #    print("1. GET OVERVIEW OF ALL AIRPLANE TYPES\n2. GET OVERVIEW OF AIRPLANE STATES\n")

    """
    def show_destinations(self):
        counter = 0
        a_dict = dict()
        self.header("-", " ALL DESTINATIONS ")
        dest_list = self.llAPI.get_all_dest()
        for destination in dest_list:
            city = destination[0]
            country = destination[1]
            counter += 1
            a_dict[str(counter)] = destination
            print("{}. {}: {}".format(counter,country, city))
        
        ########  option to choose a specific destination
        input_choice = input("\nTo choose a destination enter it's number: ")
        if input_choice in a_dict:
            self.display_destination(a_dict[input_choice])

    def display_destination(self, a_dest_info_list):
        self.header("*", " {} ".format(a_dest_info_list[1]))
        counter = 0
        display_string = ["DESTINATION ID: ","CITY: ","COUNTRY: ", "AIRPORT: ", "FLIGHT TIME: ", "DISTANCE: ","NAME OF CONTACT PERSONEL: ", "EMERGENCY PHONE NUMBER: "]
        for i in range(len(a_dest_info_list)):
            counter += 1
            print("{}. {} {}".format(counter, display_string[i] ,a_dest_info_list[i]))
    """

    def show_all_airplane_types(self):
        counter = 0
        a_dict = dict()
        self.header("-", " ALL AIRPLANE TYPES ")
        airplane_type_list = self.llAPI.get_all_airplanes()
        for airplane_type in airplane_type_list:
            city = airplane_type_list[0]
            country = airplane_type_list[1]
            counter += 1
            a_dict[str(counter)] = airplane_type
            print("{}. {}: {}".format(counter,country, city))

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
            airplane_state_str = self.llAPI.get_airplane_state(airplane.get_plane_id(), date_and_time)
            print("{}. Name: {:<30} ID: {:<10} Type: {:<20} State: {:<15}".format(counter, airplane_name_str, airplane_id_str, airplane_type_str, airplane_state_str))


    def create_airplane(self):
        ''' Returns a new instance of an airplane to the "create_new_airplane_ function '''
        new_airplane = Airplane()

        self.header("-", " ADD AIRPLANE ")
        name_str = ""
        plane_id_str = ""
        plane_type_str = ""

        new_info_str = "1. Name: {}\n2. ID: {}\n3. TYPE: {}".format(name_str, plane_id_str, plane_type_str)
        print(new_info_str)
        
        name_str = input("\nEnter new airplane name: ")
        # --- Option to go back -----
        if name_str == "b":
            return 0
        elif name_str == "h":
            return "*"
        # ---- if user wants to keep going ------
        while not self.validation.validate_name(name_str):
            name_str = input("The name you entered is invalid. Please enter a new one using only letters: ")
        new_airplane.set_name(name_str)

        # ---- Set plane ID ----
        self.header("-", " ADD AIRPLANE ")
        new_info_str = "1. Name: {}\n2. ID: {}\n3. TYPE: {}".format(name_str, plane_id_str, plane_type_str)
        print(new_info_str)
        plane_id_str = input("\nEnter new airplane ID: ")
        while not self.validation.validate_plane_id(plane_id_str):
            plane_id_str = input("The airplane ID you entered is invalid: Please enter a new one: ")
        new_airplane.set_plane_id(plane_id_str)

        # ---- Set airplane type ----
        self.header("-", " ADD AIRPLANE ")
        new_info_str = "1. Name: {}\n2. ID: {}\n3. TYPE: {}".format(name_str, plane_id_str, plane_type_str)
        print(new_info_str)
        type_list = ["NABAE146", "NAFokkerF28", "NAFokkerF100"]
        print("\n1. {}\n2. {}\n3. {}".format(type_list[0], type_list[1], type_list[2]))
        type_choice = input("\nEnter number of new airplane type: ")

        if type_choice == "1":
            plane_type_str = "NABAE146"
            new_airplane.set_type_id(plane_type_str)

        elif type_choice == "2":
            plane_type_str = "NAFokkerF28"
            new_airplane.set_type_id(plane_type_str)

        elif type_choice == "3":
            plane_type_str = "NAFokkerF100"
            new_airplane.set_type_id(plane_type_str)

            # ---- Get confirmation from user ----
        self.header("-", " ADD AIRPLANE ")
        new_info_str = "1. Name: {}\n2. ID: {}\n3. TYPE: {}".format(name_str, plane_id_str, plane_type_str)
        print(new_info_str)
        yes_or_no = input("\nIs all the information correct? (y/n): ")
        if yes_or_no == "y":
            print("You did it! The new airplane has been stored in the database!")
            return self.llAPI.create_new_airplane(new_airplane)

        # ------- Give the option of going back or home ------------
        back_option = input("To go home enter h, to go back enter b: ")
        if back_option == "b":
            return 0
        elif back_option == "h":
            return "*"
