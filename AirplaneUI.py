from LLAPI import LLAPI

class AirplanesUI():

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(13 - int((len(string)/2))) + string + form*(13 - int((len(string)/2))))

    def display_airplane_menu(self):
        print("\n","*"*26 + "\n\t Airplanes \n"+"*"*26)
        print("1. OVERVIEW\n2. ADD AIRPLANES\n")
        user_choice = input("Input a command: ")

        if user_choice == "1":
            pass
        elif user_choice == "2":
            pass
        else:
            print("invalid choice\nPlease try again")
            self.display_airplane_menu()

    def show_all_airplane_types(self):
        pass

    def show_airplane_state(self):
        pass

    def create_airplane(self):
        pass