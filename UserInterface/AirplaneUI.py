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
        return_val = 0
        while return_val == 0:

            print("*"*56 + "\n"+" "*int((56-len(" AIRPLANES "))/2)+" AIRPLANES "+" "*int((56-len(" AIRPLANES "))/2)+"\n"+"*"*56)
            print("1. AIRPLANES OVERVIEW\n2. SEE STATE OF AIRPLANES\n3. CREATE AIRPLANE\n")
            user_choice = input("Input a command: ")

            if user_choice == "1":
                self.overview_of_airplanes()
            elif user_choice == "2":
                self.state_of_airplanes()
            elif user_choice == "3":
                self.create_airplane()
            elif user_choice == "b":
                return 0
            elif user_choice == "h":
                return "*"
            else:
                print("invalid choice\nPlease try again")
                self.display_airplane_menu()

    def overview_of_airplanes(self):
        ''' Shows all airplanes and lets you choose an airplane to see more info about '''
        airplanes_list = self.llAPI.get_all_airplanes()

        return_val = 0
        while return_val == 0:

            self.header("-", " ALL AIRPLANES ")
            for number, airplane in enumerate(airplanes_list, 1):
                name = airplane.get_name()
                print("{}. {}".format(number, name))

            choice = input("\nDo you want to see more info about a specific airplane? (y/n): ")
            if choice == "y":
                choice = input("Please enter the number for the airplane you want to see more info about: ")
                return_val = self.display_airplane(choice)
            elif choice == "b" or choice == "n":
                return 0
            elif choice == "h":
                return "*"

    def display_airplane(self, number):
        airplanes_list = self.llAPI.get_all_airplanes()

        return_val = 0
        while return_val == 0:
            airplane = airplanes_list[int(number) - 1]
            self.header("-", " {} ".format(airplane.get_name().upper()))
            print(airplane)
            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"
        
    def state_of_airplanes(self):
        return_val = 0
        while return_val == 0:
            counter = 0
            airplanes_list = self.llAPI.get_all_airplanes()

            self.header("-", " ENTER DATE ")
            print("To see the state of our airplanes, please specify the date and time you want to see :)")
            chosen_date = input("\nPlease enter your desired date in the format (YYYY-MM-DD): ")
            chosen_time = input("Please enter your desired time in the format (HH:MM:00): ")

            self.header("-", " STATE OF ALL AIRPLANES AT {} ON {}".format(chosen_time, chosen_date))
            for airplane in airplanes_list:
                counter += 1
                airplane_name_str = airplane.get_name()
                airplane_id_str = airplane.get_plane_id()
                date_and_time = chosen_date + "T" + chosen_time
                airplane_state_str = self.llAPI.get_airplane_state(airplane.get_plane_id(), date_and_time)
                print("{:>3}. {:<23} ID: {:<10} State: {:<15}"\
                .format(counter, airplane_name_str, airplane_id_str, airplane_state_str))
            
            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"

    def create_airplane(self):
        ''' Returns a new instance of an airplane to the "create_new_airplane_ function '''
        return_val = 0
        while return_val == 0:
            new_airplane = Airplane()

            self.header("-", " ADD AIRPLANE ")
            name_str = ""
            plane_id_str = ""
            plane_type_str = ""

            new_info_str = "1. Name: {}\n2. ID: {}\n3. TYPE: {}".format(name_str, plane_id_str, plane_type_str)
            print(new_info_str)

            name_str = input("\Please enter new airplane name: ")

            while not self.validation.validate_name(name_str):
                name_str = input("The name you entered is invalid. Please  a new one using only letters: ")
            new_airplane.set_name(name_str)

            # ---- Set plane ID ----
            self.header("-", " ADD AIRPLANE ")
            new_info_str = "1. Name: {}\n2. ID: {}\n3. TYPE: {}".format(name_str, plane_id_str, plane_type_str)
            print(new_info_str)
            plane_id_str = input("\nPlease enter new airplane ID: ")
            while not self.validation.validate_plane_id(plane_id_str):
                plane_id_str = input("The airplane ID you entered is invalid: Please enter a new one: ")
            new_airplane.set_plane_id(plane_id_str)

            # ---- Set airplane type ----
            self.header("-", " ADD AIRPLANE ")
            new_info_str = "1. Name: {}\n2. ID: {}\n3. TYPE: {}".format(name_str, plane_id_str, plane_type_str)
            print(new_info_str)
            type_list = ["NABAE146", "NAFokkerF28", "NAFokkerF100"]
            print("\n1. {}\n2. {}\n3. {}".format(type_list[0], type_list[1], type_list[2]))
            type_choice = input("\Please enter the number for airplane type: ")

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