import datetime
from MODELS.airplane import Airplane
from Validation.validation import Validate

class AirplaneUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI
        self.validation = Validate()

    def header(self, form, string):
        ''' Creates a header with the form as decoration around the chosen string '''

        print("\n\n"+form*(28 - int((len(string)/2))) + string + form*(28 - int((len(string)/2))))

    def display_airplane_menu(self):
        ''' Displays the airplanes sub-menu '''

        return_val = 0
        while return_val == 0:

            print("\n" + "*"*56 + "\n"+" "*int((56-len(" AIRPLANES "))/2)+" AIRPLANES "+" "*int((56-len(" AIRPLANES "))/2)+"\n"+"*"*56)
            print("1. AIRPLANES OVERVIEW\n2. SEE STATE OF AIRPLANES\n3. CREATE AIRPLANE\n")
            user_choice = input("Input a command: ")

            # Displays a sub-sub-menu depending on the user input
            if user_choice == "1":
                return_val = self.overview_of_airplanes()
            elif user_choice == "2":
                return_val = self.state_of_airplanes()
            elif user_choice == "3":
                return_val = self.create_airplane()
            elif user_choice == "b":
                return 0
            elif user_choice == "h":
                return "*"
            else:
                user_choice = input("Invalid command. Please try again: ")

    def overview_of_airplanes(self):
        ''' Shows a listing of all airplanes and lets you choose an airplane to see more info about '''

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

    def display_airplane(self, choice):
        ''' Displays more information about a specific airplane '''

        airplanes_list = self.llAPI.get_all_airplanes()

        return_val = 0
        while return_val == 0:
            airplane = airplanes_list[int(choice) - 1] # Matches the user_choice to the index in airplanes list
            self.header("-", " {} ".format(airplane.get_name().upper()))
            print(airplane) # Calls the __str__ method for the chosen airplane instance

            back_option = input("\nTo go back enter b, to go home enter h: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"
        
    def state_of_airplanes(self):
        ''' Shows an overview of all states of airplanes for a specific date and time '''

        return_val = 0
        while return_val == 0:
            counter = 0
            airplanes_list = self.llAPI.get_all_airplanes()

            self.header("-", " ENTER DATE ")
            print("To see the state of our airplanes, please specify the date and time you want to see :)")

            # Choose a date
            chosen_date = input("\nPlease enter your desired date in the format (YYYY-MM-DD): ")
            while not self.validation.validate_date(chosen_date):
                chosen_date = input("Invalid date. Please enter a new date using the format (YYYY-MM-DD)")

            # Choose a time
            chosen_time = input("Please enter your desired time in the format (HH:MM:00): ")
            while not self.validation.validate_time(chosen_time):
                chosen_time = input("Invalid time. Please use the format (HH:MM:SS): ")

            # Creates the listing
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
        ''' Gets information inputs from user to create a new instance of an Airplane '''

        return_val = 0
        while return_val == 0:
            new_airplane = Airplane()

            # ---- Set name ----
            self.header("=", " ENTER NAME ")
            print(new_airplane)

            name_str = input("Please enter new airplane name: ")

            while not self.validation.validate_name(name_str):
                name_str = input("The name you entered is invalid. Please enter a new one using only letters: ")

            new_airplane.set_name(name_str)

            # ---- Set plane ID ----
            self.header("=", " ENTER PLANE ID ")
            print(new_airplane)

            plane_id_str = input("\nPlease enter new airplane ID: ")

            while not self.validation.validate_plane_id(plane_id_str):
                plane_id_str = input("The airplane ID you entered is invalid: Please enter a new one: ")

            new_airplane.set_plane_id(plane_id_str)

            # ---- Set airplane type ----
            self.header("=", " SET AIRPLANE TYPE ")
            print(new_airplane)

            plane_types_list = ["NABAE146", "NAFokkerF28", "NAFokkerF100"]

            for number, plane_type in enumerate(plane_types_list, 1):
                print("{}. {}".format(number, plane_type))

            valid_type_choices = ["1", "2", "3"]
            type_choice = input("\nPlease enter the number for airplane type: ")

            while type_choice not in valid_type_choices:
                type_choice = input("Invalid choice. Please enter again: ")

            # ---- Sets the plane capacity depending on the plane type ----
            else:
                if type_choice == "1":
                    plane_type_str = plane_types_list[0]
                    new_airplane.set_type_id(plane_type_str)
                    new_airplane.set_capacity("83")

                elif type_choice == "2":
                    plane_type_str = plane_types_list[1]
                    new_airplane.set_type_id(plane_type_str)
                    new_airplane.set_capacity("65")

                elif type_choice == "3":
                    plane_type_str = plane_types_list[2]
                    new_airplane.set_type_id(plane_type_str)
                    new_airplane.set_capacity("100")

            # ---- Get confirmation from user ----
            self.header("-", " CREATE AIRPLANE ")
            print(new_airplane)
            confirmation = input("Is all the information correct? (y/n): ")
            if confirmation == "y":
                print("\nYou did it! The new airplane has been stored in the database!")
                self.llAPI.create_new_airplane(new_airplane)

                back_option = input("To go home enter h, to go back enter b: ")
                if back_option == "b":
                    return 0
                elif back_option == "h":
                    return "*"

            # ------- Give the option of going back or home ------------
            back_option = input("To go home enter h, to go back enter b: ")
            if back_option == "b":
                return 0
            elif back_option == "h":
                return "*"