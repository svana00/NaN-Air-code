
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
        airplane_type_list = self.llAPI.get_all_airplane_types()
        for airplane_type in airplane_type_list:
            city = airplane_type_list[0]
            country = airplane_type_list[1]
            counter += 1
            a_dict[str(counter)] = airplane_type
            print("{}. {}: {}".format(counter,country, city))

    def show_airplane_state(self):
        pass

    def create_airplane(self):
        ###### initializing the values for the new object and the list that will contain them ###3
        name_ID_str = ""
        airplane_type_str = ""
        airplane_info_list = ["" for i in range(3)]
        
        #printing out the menu
        self.header("-", " ADD AIRPLANE ")
        print("1. ID: {}\n2. TYPE: {}".format(name_ID_str, airplane_type_str))

        choice = input("\n"+"Input what you want to add: ")
        
        VALID_LIST = ["1","2","confirm"] #all of the valid options within the menu

        while choice in VALID_LIST:
            if choice == "1":
                name_ID_str = input("\nEnter airplane name: ")
                airplane_info_list[0] = name_ID_str
                
            elif choice == "2":
                airplane_type_str = input("Enter airplane type: ")
                airplane_info_list[2] = airplane_type_str
            
            elif choice == "confirm":
                break
           
            self.header("-", " ADD AIRPLANE ")
            print("1. ID: {}\n2. TYPE: {}".format(name_ID_str, airplane_type_str))
            choice = input("\nInput what you want to add: ")

        return self.llAPI.create_new_airplane(airplane_info_list)
            
