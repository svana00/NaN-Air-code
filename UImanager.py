
from StaffMemberUI import StaffMemberUI
from DestinationUI import DestinationUI
from AirplaneUI import AirplanensUI
from VoyageUI import VoyageUI


class UIManager():
    def start(self):
        self.mainLoop()
        
    def mainLoop(self):
        while True:
            print("*"*26 + "\n\t NaN AIR\n"+"*"*26)
            print("1. STAFF\n2. AIRPLANES\n3. VOYAGES\n4. DESTINATIONS")
            var = input("\nInput a command: ")
            if var == "1":
                Staff_member_UI = StaffMemberUI()
                Staff_member_UI.display_staff_menu()
            elif var == "2":
                pass
            elif var == "3":
                Voyage_UI = VoyageUI()
                Voyage_UI.display_voyages_menu()
            elif var == "4":
                Dest_UI = DestinationUI()
                Dest_UI.display_dest_menu()
            elif var == "q":
                break
            else:
                print("invalid choice")
