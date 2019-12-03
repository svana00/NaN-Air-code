from LLAPI import LLAPI

class VoyageUI():

    def header(self, form, string):
        print(form*(13 - len(string)) + string + form*(13 - len(string)))

    def display_voyages_menu(self, overview_options):
        print("*"*26 + "\n\t VOYAGES \n"+"*"*26)
        print("1. CHANGE\n2. OVERVIEW\n3. ADD")
        var = input("\nInput a command: ")
        if var == "1":
            print("")
        elif var == "2":
            overview_options()
        elif var == "3":
            print("")

    def overview_options(self):
        pass
    def choose_date(self):
        pass

    def show_voyages_by_date(self):
        pass

    def show_voyages_by_week(self):
        pass

    def show_one_voyage(self):
        pass

    def show_all_voyage(self):
        pass

    def create_voyage(self, header):
        header("*"," VOYAGES ")
        print("1. ADD VOYAGE\n2. ADD FROM EXISTING VOYAGES")

    def copy_voyage(self):

        pass

    def assign_voyage(self):
        pass