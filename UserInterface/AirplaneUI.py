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
        ''' Returns a new instance of an airplane to the "creat_new_airplane_ function '''
        new_airplane = Airplane()

        name_str = ""
        plane_id_str = ""
        plane_type_str = ""

        #printing out the menu
        self.header("-", " ADD AIRPLANE ")
        print("1. Name: {}\n2. ID: {}\n3. TYPE: {}".format(name_str, plane_id_str, plane_type_str))
        
        VALID_LIST = ["1","2", "3", "confirm"] #all of the valid options within the menu
        chosen_input_list = set()

        choice = input("\nPlease enter the number corresponding to the information you would like to add: ")
        if choice == "0":
            return 0
        elif choice == "*":
            return "*"

        while choice in VALID_LIST:

            if choice == "1":
                name_str = input("\nEnter airplane name: ")
                while not self.validation.validate_name(name_str):
                    if name_str == "0":
                        return 0
                    elif name_str == "*":
                        return "*"
                    name_str = input("The name you entered is invalid. Please enter a using letters only: ")
                new_airplane.set_name(name_str)
                chosen_input_list.add(choice)

            elif choice == "2":
                plane_id_str = input("Enter airplane ID: ")
                while not self.validation.validate_plane_id(plane_id_str):
                    if plane_id_str == "0":
                        return 0
                    elif plane_id_str == "*":
                        return "*"
                    plane_id_str = input("The ID you entered is invalid. Please try again: ")
                new_airplane.set_plane_id(plane_id_str)
                chosen_input_list.add(choice)
    
            elif choice == "3":
                type_list = ["NABAE146", "NAFokkerF28", "NAFokkerF100"]
                print("\n1. {}\n2. {}\n3. {}".format(type_list[0], type_list[1], type_list[2]))
                type_choice = input("\nEnter number of new airplane type: ")

                if type_choice == "1":
                    new_plane_type = "NABAE146"
                    new_airplane.set_type_id(plane_type_str)
                    chosen_input_list.add(choice)


                    chosen_input_list.add(choice)
                elif type_choice == "2":
                    new_plane_type = "NAFokkerF28"
                    new_airplane.set_type_id(plane_type_str)
                    chosen_input_list.add(choice)

                elif type_choice == "3":
                    new_plane_type = "NAFokkerF100"
                    new_airplane.set_type_id(plane_type_str)
                    chosen_input_list.add(choice)

            elif choice == "confirm":
                break
           
            self.header("-", " ADD AIRPLANE ")
            print("1. Name: {}\n2. ID: {}\n3. TYPE: {}".format(name_str, plane_id_str, plane_type_str))
            choice = input("\nInput what you want to add: ")

        return self.llAPI.create_new_airplane(new_airplane)
            
