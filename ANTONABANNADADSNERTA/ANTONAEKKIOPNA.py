class Changes:
    def __init__(self, ioAPI):
        self.ioAPI = ioAPI
    
    def change_dest(self):
        file_1 = open("new_file.csv", "w+")
        
