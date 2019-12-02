class UImain:
    def start(self):
        self.mainLoop()
        
    def mainLoop(self):
        while True:
            var = input("Input a command: ")
            print("your cocmmand was: " + var)