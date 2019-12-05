
class VoyageUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(13 - int((len(string)/2))) + string + form*(13 - int((len(string)/2))))

    def display_voyages_menu(self):
        """ displays the main menu for voyages giving the user 
        the options to change, add, or see overview of voyages """

        print("*"*26 + "\n\t VOYAGES \n"+"*"*26)
        print("1. CHANGE\n2. OVERVIEW\n3. ADD")
        var = input("\nInput a command: ")
        if var == "1":
            self.change_voyage()
        elif var == "2":
            self.overview_options() # menu for overview choices
        elif var == "3":
            self.create_voyage()


    def overview_options(self):
        """ menu for overview choices """
        self.header("-", " GET OVERVIEW ")
        print("1. ALL VOYAGES \n2. VOYAGES BY DATE")
        option = input("\nInput a command: ")
        if option == "1":
            self.show_all_voyages()
        elif option == "2":
            self.choose_date()

    def choose_date(self):
        self.header("-"," CHOOSE DATE ")
        print("With the format dd/mm/yyyy")
        date = input("Please enter the desired date: ")
        if date == "01/01/1000":
            print("whoop whoop!!")

    def show_voyages_by_date(self):
        pass

    def show_voyages_by_week(self):
        pass

    def show_one_voyage(self):
        pass

    def show_all_voyages(self):
        counter = 0
        voyages_dict = {}
        self.header("-", " ALL VOYAGES ")
        voyage_list = self.llAPI.get_all_voyages()
        for voyage in voyage_list:
            voyage_name = voyage_list[0]
            counter += 1
            voyages_dict[str(counter)] = voyage
            print("{}. {}".format(counter,voyage_name))

        ###### option to choose a specific destination
        input_choice = input("To choose a specific voyage enter it's number: ")
        if input_choice in voyages_dict:
            self.display_voyage(voyages_dict[input_choice])

    def display_voyage(self, a_voyage_info_list):
        self.header("*", " {} ".format(a_voyage_info_list[0]))
        counter = 0
        for info in a_voyage_info_list:
            counter += 1
            print("{}. {}".format(counter, info))

    def add_voyage_menu(self):
        self.header("*"," VOYAGES ")
        print("1. ADD VOYAGE\n2. ADD FROM EXISTING VOYAGES")
        menu_choice = input("Input command here: ")
        if menu_choice == "1":
            self.create_voyage
        elif menu_choice == "2":
            self.copy_voyage
        else:
            print("Invalid choice\nPlease try again")

    def create_voyage(self):
    ######initializing the values for the new object and the list that will contain them ##
        
        flight_number_str = ""
        departing_from_str = ""
        arriving_at_str = ""
        departure_str = ""
        arrival_at_str = ""
        aircraft_ID_str = ""
        captain_str = ""
        copilot_str = ""
        fsm_str = ""
        fa1_str = ""
        fa2_str = ""

        a_dict_list = [flight_number_str,departing_from_str,arriving_at_str,departure_str,arrival_at_str,aircraft_ID_str,captain_str,copilot_str,fsm_str,fa1_str,fa2_str] # lists all the functionality and things needed to add a voyage
        test_list = ["flight number","departing from","arriving at", "departure", "arrival", "aircraft", "captain", "copilot", "fsm", "fa1", "fa2"] 
        insert_list = ["\nplease enter new {}: ".format(test_list[i]) for i in range(len(test_list))]

        voyages_dict = { str(i+1) : a_dict_list[i] for i in range(0, len(a_dict_list) ) }

        #### the header and main body
        self.header("-", " ADD VOYAGE ")
        for i in range(len(a_dict_list)):
            print("{}. {}: {}".format((i+1), test_list[i],a_dict_list[i]))
        input_number_str = input("\nInput what you want to add: ")
        #######

        ###### a while loop that asks for and replaces values for a new voyage
        while input_number_str in voyages_dict.keys() :
            choice = input(insert_list[int(input_number_str) - 1]) # prints out the corresponding text to what the user wants to change and takes in the input
            voyages_dict[input_number_str] = choice # changes the value in the dict to the entered value

            #### printing the header and modified main body ##
            self.header("-", " ADD VOYAGE ")
            for i in range(len(a_dict_list)):
                print("{}. {}: {}".format((i+1), test_list[i], voyages_dict[str(i+1)]))
            print("To confirm changes enter confirm")
            #######3

            input_number_str = input("\nInput what you want to add: ")
        if input_number_str == "confirm":
            return 0 ### need to find a way to return the list of values from the dict

    def copy_voyage(self):

        pass

    def assign_voyage(self):
        pass

    def change_voyage(self):
        pass
