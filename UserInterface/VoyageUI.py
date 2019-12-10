from Validation.validation import Validate
class VoyageUI():

    def __init__(self, llAPI):
        self.llAPI = llAPI
        self.validate = Validate()

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(28 - int((len(string)/2))) + string + form*(28 - int((len(string)/2))))

    def display_voyages_menu(self):
        """ displays the main menu for voyages giving the user 
        the options to change, add, or see overview of voyages """
        print("*"*56 + "\n"+" "*int((56-len(" VOYAGES "))/2)+"VOYAGES"+" "*int((56-len(" VOYAGES "))/2)+"\n"+"*"*56)
        print("1. ASSIGN\n2. OVERVIEW\n3. ADD")
        var = input("\nInput a command: ")
        if var == "1":
            self.assign_voyage()
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

    def show_all_voyages(self):
        counter = 0
        voyage_list = self.llAPI.get_all_voyages()

        self.header("-", " ALL VOYAGES ")

        for voyage in voyage_list:
            counter += 1
            voyage_id = voyage.get_voyage_id()
            dest_id = voyage.get_dest_id()
            destination =  self.llAPI.get_destination_info(dest_id)
            city = destination.get_city()
            departure_out = voyage.get_departure_out()
            print("{:<2}. Voyage_id: {:<5} City: {:<15} Departure at: {:<15}".format(counter, voyage_id, city, departure_out))

        choice = input("\nDo you want to see more info about a specific voyage? (y/n): ")
        if choice == "y":
            return self.display_voyage(voyage_list)

    def display_voyage(self, voyage_list):
        number = int(input("Enter number of voyage: "))
        voyage = voyage_list[(number) - 1]
        voyage_id = voyage.get_voyage_id()
        self.header("-", " Voyage {} ".format(voyage_id))
        print(voyage)

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
        time_str = input("Enter time of voyage (HH:MM:SS) : ")

        while not self.validate.validate_time(time_str):
            print("Invalid time.")
            time_str = input("Enter time of voyage (HH:MM:SS) : ")
        else:
            voyage_info_list.append(time_str)   

        self.header("-", " ADD VOYAGE ")
        print("\n1. DESTINATION: {}\n2. DATE: {}\n3. TIME OF FLIGHT FROM KEFLAVIK TO DESTINATION: {}".format(city, date_str, time_str))

        print("\nChanges have been confirmed")

        return self.llAPI.make_voyage(voyage_info_list)

    def assign_voyage(self):
        # 1. Voyages sem eru ekki fullmannaðar
        # 2. Vela valid airplane
        # 3. Vela valid staff (ekki busy eða ekki með leyfi)
        # 4. Done

        airplanes_list = self.llAPI.get_all_airplanes() # List of instances
        voyage_list = self.llAPI.get_all_voyages() # List of instances
        non_assigned_voyages = "x"
        valid_airplanes_list = []
        counter = 1

        self.header("-", " AIRPLANES ")

        for airplane in airplanes_list:
            airplane_id = airplane.get_plane_id()
            name = airplane.get_name()
            print("{}. {}".format(counter, name))
            counter += 1

        choice = input("Enter a number: ")