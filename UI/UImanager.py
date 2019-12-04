from UI.StaffMemberUI import StaffMemberUI
from UI.DestinationUI import DestinationUI
from UI.AirplaneUI import AirplaneUI
from UI.VoyageUI import VoyageUI
from LL.LLAPI import LLAPI

class UIManager():

    def __init__(self):
        self.llAPI = LLAPI()
        self.staffUI = StaffMemberUI(self.llAPI)
        self.destUI = DestinationUI(self.llAPI)
        self.airplaneUI = AirplaneUI(self.llAPI)
        self.voyageUI = VoyageUI(self.llAPI)
        
    def start(self):
        self.mainLoop()
        
    def mainLoop(self):
        while True:
            print("\n\n" + "*"*26 + "\n\t NaN AIR\n"+"*"*26)
            print("1. STAFF\n2. AIRPLANES\n3. VOYAGES\n4. DESTINATIONS")
            var = input("\nInput a command: ")
            if var == "1":
                self.staffUI.display_staff_menu()
            elif var == "2":
                self.airplaneUI.display_airplane_menu()
            elif var == "3":
                self.voyageUI.display_voyages_menu()
            elif var == "4":
                self.destUI.display_dest_menu()
            elif var == "q":
                break
            else:
                print("invalid choice")
