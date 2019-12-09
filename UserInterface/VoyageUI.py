from Validation.validation import Validate
class VoyageUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI
        self.validate = Validate()

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
            self.change_voyage_menu()
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
        destination_list = []
        voyage_info_list = self.llAPI.get_all_voyages()

        self.header("-", " ALL VOYAGES ")

        for voyage_info in voyage_info_list:
            counter += 1
            voyage_id = voyage_info[0]
            dest_id = voyage_info[1]
            destination =  self.llAPI.get_destination_info(dest_id)
            city = destination.get_city()
            departure_out = voyage_info[2]

            print("{:<2}. Voyage_id: {:<5} City: {:<15} Departure at: {:<15}".format(counter, voyage_id, city, departure_out))

    def display_voyage(self, a_voy_info_list):
        a_voyage_info_list = list(a_voy_info_list)
        #voyage_info_print_list = ["destination","flight 1 date (YYYY/MM/DD)", "flight 1 time (XX:XX:XX)", \
        #                        "flight 2 date (YYYY/MM/DD)","flight 1 time (XX:XX:XX)", "airplane"] 
        voyage_info_list = ["flight number 1", "flight number 2", "destination", "flight 1 date", "flight 1 time", \
                            "flight 2 date", "flight 2 time", "airplane ID", "captain","copilot", "fsm", "fa1", "fa2"] 


        # header and main body
        self.header("*", " {} ".format(a_voyage_info_list[1]))
        counter = 0
        for i in range(len(a_voyage_info_list)):
            counter += 1
            print("{}. {} {}".format(counter,voyage_info_list[i].upper(), a_voyage_info_list[i]))

    def add_voyage_menu(self):
        self.header("*"," VOYAGES ")
        print("1. ADD VOYAGE\n2. ADD FROM EXISTING VOYAGES")
        menu_choice = input("Input command here: ")
        if menu_choice == "1":
            self.create_voyage()
        elif menu_choice == "2":
            self.copy_voyage()
        else:
            print("Invalid choice\nPlease try again")

    def create_voyage(self):
        ''' Returns a list of information about a new voyage '''
        voyage_info_list = []
 
        # User chooses destination
        destinations_info_list = self.llAPI.get_destinations()
        counter = 1

        self.header("-", " CHOOSE DESTINATION ")
        for destination_info in destinations_info_list:
            city = destination_info[2]
            print("{}. {}".format(counter,city))
            counter += 1

        valid_list = [str(num) for num in range(len(destinations_info_list))]
        invalid_input = True
        number = input("\nEnter number of desired destination for voyage: ")

        while invalid_input == True:
            if number in valid_list:
                dest_id = destinations_info_list[(int(number) - 1)][0]
                city = destinations_info_list[(int(number) - 1)][2]
                voyage_info_list.append(dest_id)
                invalid_input = False
            else:
                print("Invalid choice. Enter again.")
                number = input("\nEnter number of desired destination for voyage: ")

        invalid_input = True

        # User chooses date for voyage
        self.header("-", " CHOOSE DATE ")
        date_str = input("Enter date of voyage (YYYY-MM-DD) : ")

        while not self.validate.validate_date(date_str):
            print("Invalid date.")
            date_str = input("Enter date of voyage (YYYY-MM-DD) : ")
        else:
            voyage_info_list.append(date_str)        

        # User chooses time for voyage
        self.header("-", " CHOOSE TIME ")
        time_str = input("Enter time of voyage (XX-XX-XX) : ")

        while not self.validate.validate_time(time_str):
            print("Invalid time.")
            time_str = input("Enter time of voyage (XX:XX:XX) : ")
        else:
            voyage_info_list.append(time_str)   

        self.header("-", " ADD VOYAGE ")
        print("\n1. DESTINATION: {}\n2. DATE: {}\n3. TIME OF FLIGHT FROM KEFLAVIK TO DESTINATION: {}".format(city, date_str, time_str))

        print("Changes have been confirmed")
        return self.llAPI.make_voyage(voyage_info_list)

    def assign_voyage(self):
        pass

    def change_voyage_information(self):
        self.show_all_voyages()

        # show all voyages and then choose one of them,
        # then you are shown all of the information you are able to change,
        # you enter what you want to change

    def change_voyage_menu(self):
        #prints header and main body
        self.header("-", " CHANGE VOYAGE ")
        option_list = ["ASSIGN STAFF MEMBERS","CHANGE INFORMATION"]
        for i in range(2):
            print("{} {}".format(str(i+1),option_list[i]))

        #asking for input and redirecting to different frames based on that input
        change_choice = input("\nEnter what you want to change: ")

        if change_choice == "1":
            self.assign_voyage()
        elif change_choice == "2":
            self.change_voyage_information()