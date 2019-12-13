from UserInterface.StaffMemberUI import StaffMemberUI
from UserInterface.DestinationUI import DestinationUI
from UserInterface.AirplaneUI import AirplaneUI
from UserInterface.VoyageUI import VoyageUI
from LogicLayer.LLAPI import LLAPI

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
        # constants make the rest of the program easier to write and change 
        white = "\033[1;37;40m"
        cyan = "\033[1;36;40m"
        magenta = "\033[1;35;40m"
        blue ="\033[1;34;40m"
        yellow = "\033[1;33;40m"
        green =  "\033[1;32;40m"
        red = "\033[1;31;40m"
        dark_gray = "\033[1;30;40m"
        #black  = "\033[0;30;47m"   
        #red yellow green cyan blue magenta
        return_val = 0
        while return_val == 0 or return_val == "*":
            
            # ----- super extra logo ------
            '''
            print(red + "\n\n             /**   /**           /**   /**        /******  /****** /******* "+ white + "TM"+ red +"                                               ")
            print("            | *** | **          | *** | **       /**__  **|_  **_/| **__  **"+ white + "   *  *                                          " + red)               
            print(yellow + "            | ****| **  /****** | ****| **      | **  \ **  | **  | **  \ **"+ dark_gray + "           *         "+ white + "Where every number"+ red + "          ")
            print(yellow + "            | ** ** ** |____  **| ** ** **      | ********  | **  | *******/"+ white + "                 *       is divisible by zero    " + green)
            print("            | **  ****  /*******| **  ****      | **__  **  | **  | **__  **"+ dark_gray + "                       *                         " + cyan)
            print("            | **\  *** /**__  **| **\  ***      | **  | **  | **  | **  \ **"+ dark_gray + "               *                                 " + blue)
            print(magenta + "            | ** \  **|  *******| ** \  **      | **  | ** /******| **  | **"+ white + "                     *                           "+ magenta)
            print("            |__/  \__/ \_______/|__/  \__/      |__/  |__/|______/|__/  |__/                                                 \n\n" + "\033[0m")
            '''
            # ---- very basic logo -------
            
            print("\n\n             /**   /**           /**   /**        /******  /****** /******* TM")
            print("            | *** | **          | *** | **       /**__  **|_  **_/| **__  **")
            print("            | ****| **  /****** | ****| **      | **  \ **  | **  | **  \ **         where every number")
            print("            | ** ** ** |____  **| ** ** **      | ********  | **  | *******/             is divisable by zero")
            print("            | **  ****  /*******| **  ****      | **__  **  | **  | **__  **")
            print("            | **\  *** /**__  **| **\  ***      | **  | **  | **  | **  \ **")
            print("            | ** \  **|  *******| ** \  **      | **  | ** /******| **  | **")
            print("            |__/  \__/ \_______/|__/  \__/      |__/  |__/|______/|__/  |__/\n\n")
            

            #kinda extra logo -----
            """
            print(red + "\n\n             /**   /**           /**   /**        /******  /****** /******* "+ white + "TM"+red)
            print("            | *** | **          | *** | **       /**__  **|_  **_/| **__  **" + red)               
            print(yellow + "            | ****| **  /****** | ****| **      | **  \ **  | **  | **  \ **"+ red)
            print(yellow + "            | ** ** ** |____  **| ** ** **      | ********  | **  | *******/"+ green)
            print("            | **  ****  /*******| **  ****      | **__  **  | **  | **__  **"+ cyan)
            print("            | **\  *** /**__  **| **\  ***      | **  | **  | **  | **  \ **"+ blue)
            print(magenta + "            | ** \  **|  *******| ** \  **      | **  | ** /******| **  | **"+  magenta)
            print("            |__/  \__/ \_______/|__/  \__/      |__/  |__/|______/|__/  |__/\n\n" + white)
            """





            # font = bigmoney-ne : by nathan bloomfield (xzovik@gmail.com)
            print("\n\n"+"*"*56 + "\n"+" "*int((56-len(" MAIN MENU "))/2)+" MAIN MENU "+" "*int((56-len(" MAIN MENU "))/2)+"\n"+"*"*56)
            print("1. STAFF\n2. AIRPLANES\n3. VOYAGES\n4. DESTINATIONS")
            var = input("\nInput a command: ")
            print("")
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
