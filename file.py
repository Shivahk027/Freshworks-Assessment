class Folder:
    def __init__(self, file):
        self.file = file
        
    #this function is call after all operations in the file to set initial index
    def closeTheFile(self, fptr):
        fptr.seek(0, 0)
        fptr.close()

    #function to read the file
    def readTheFile(self):
        try:
            fptr = open(self.file, "r")
            lines = fptr.read()
            return lines
        except FileNotFoundError:
            print("File does not exist!!")
        finally:
            self.closeTheFile(fptr)

    #function to write into file
    def writeTheFile(self, lines):
        try:
            fptr = open(self.file, "w")
            for line in lines:
                fptr.write(line)            
        except:
            print("Something went wrong...!!")
        finally:
            self.closeTheFile(fptr)
