
from StaffMemberUI import StaffMemberUI
from DestinationUI import DestinationUI
from AirplanesUI import AirplanensUI
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
                All_Staff = StaffMemberUI()
                All_Staff.show_all_staff()
            elif var == "2":
                pass
            elif var == "3":
                pass
            elif var == "4":
                DestUI = DestinationUI()
                DestUI.show_destinations()
            elif var == "q":
                break
            else:
                print("invalid choice")
