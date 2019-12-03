from LLAPI import LLAPI

class VoyageUI():

    def header(self, form, string):
        """ creates a header with the form as decoration before the chosen string """
        print("\n\n"+form*(13 - (len(string)/2)) + string + form*(13 - (len(string)/2)))

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
        pass

    def create_voyage(self):
        self.header("*"," VOYAGES ")
        print("1. ADD VOYAGE\n2. ADD FROM EXISTING VOYAGES")

    def copy_voyage(self):

        pass

    def assign_voyage(self):
        pass

    def change_voyage(self):
        pass