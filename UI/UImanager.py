
class UIManager:
    def start(self):
        self.mainLoop()
        
    def mainLoop(self):
        while True:
            print("*"*26 + "\n\t NaN AIR\n"+"*"*26)
            print("1. STAFF\n2. AIRPLANES\n3. VOYAGES\n4. DESTINATIONS")
            var = input("\nInput a command: ")
            if var == "1":
                print("amazing choice m8")
            if var != "1" or "2" or "3" or "4":
                print("invalid choice")


