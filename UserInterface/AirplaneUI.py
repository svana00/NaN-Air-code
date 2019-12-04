
class AirplaneUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI

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
            self.create_airplane()
        else:
            print("invalid choice\nPlease try again")
            self.display_airplane_menu()

    def show_all_airplane_types(self):
        pass

    def show_airplane_state(self):
        pass

    def create_airplane(self):
        ###### initializing the values for the new object and the list that will contain them ###3
        name_ID_str = ""
        airplane_type_str = ""
        airplane_info_list = []
        
        #printing out the menu
        self.header("-", " ADD AIRPLANE ")
        print("1. ID: {}\n2. TYPE: {}".format(name_ID_str, airplane_type_str))

        choice = input("\n"+"Input what you want to add: ")
        
        VALID_LIST = ["1","2","confirm"] #all of the valid options within the menu

        while choice in VALID_LIST:
            if choice == "1":
                name_ID_str = input("\nEnter new ID: ")
                airplane_info_list[0] = name_ID_str
                
            elif choice == "2":
                airplane_type_str = input("Enter new airport: ")
                airplane_info_list[2] = airplane_type_str
           
            self.header("-", " ADD AIRPLANE ")
            print("1. ID: {}\n2. TYPE: {}".format(name_ID_str, airplane_type_str))
            choice = input("\nInput what you want to add: ")
        
        return airplane_info_list
