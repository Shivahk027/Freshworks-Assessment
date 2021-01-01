import json
import threading
import time
from file import Folder

#class to maintain thread life session
class KeySession:
    def insert(self, key_value, key, value, secs):
        if key in key_value:
            print(f"\nKey: {key} already exists!\n")
        else:
            key_value[key] = value
            print(f"{key}: {value} iserted!\n")
            time.sleep(secs)
            del key_value[key]
#this is the main class
class answer(Folder):
    key_value = dict()

    #function to initialize file
    def initilize(self, file = "json.txt"):
        self.fObj = Folder(file)
        self.key_value = json.loads(self.fObj.readTheFile())
        print("\nInitilized successfully!\n")

    #function to instert key-value pair
    def insert(self, key, value):
        if key in self.key_value:
            print(f"\nKey: {key} already exists..!\n")
        else:
            self.key_value[key] = value
            print(f"{key}: {value} iserted..!\n")

    #function to delete key-value pair
    def delete(self, key):
        if key in self.key_value:
            del self.key_value[key]
            print(f"\nKey: {key} is deleted successfully!\n")
        else:            
            print(f"\nKey: {key} does not exists!\n")

    #function to retrieve the key-value pair
    def getValue(self, key):
        if key in self.key_value:
            return self.key_value[key]
        else:
            print(f"\nKey: {key} does not exists!\n")
    #function to write into the file
    def writeToFile(self, file):
        try:
            fileStr = json.dumps(self.key_value)
            with open(file, "w") as fptr:
                fptr.write(fileStr)
            print(f"\nFile is saved!\n")
        except:
            print("\nSomething went worng..!!\n")            

    #this is the menu driven
    def menu(self):
        while True:
            try:
                print("*---MENU---*")
                print("\n1. Initilize file.")
                print("2. Insert a Key-Value pair.")
                print("3. Insert a Key-Value pair with time-to-live in seconds.")
                print("4. Get value of a Key.")
                print("5. Delete a Key-Value pair.")
                print("6. Save the file.")
                print("7. Exit.\n")
                print("(Enter your option)-->")
                choice = int(input())
                if choice == 1:
                    file = input("\n Enter file-name: ")
                    self.initilize(file)
                elif choice == 2:
                    key = input("\n Enter Key: ")
                    value = input("Enter Value: ")
                    self.insert(key, value)
                elif choice == 3:
                    key = input("\n Enter Key: ")
                    value = input("Enter Value: ")
                    secs = int(input("Enter time in seconds: "))
                    threadObject = threading.Thread(target = KeySession.insert, args=(5, self.key_value, key, value, secs))
                    threadObject.start()
                elif choice == 4:
                    key = input("\nEnter Key: ")
                    value = self.getValue(key)
                    if value != None:
                        print(f"\n{key}: {value}\n")
                elif choice == 5:
                    key = input("\nEnter Key: ")
                    self.delete(key)
                elif choice == 6:
                    file = input("\nEnter file name with extension to save key-value pair: ")
                    self.writeToFile(file)
                    break
                else:
                    if choice == 7:
                        break
                    else:
                        raise Exception(ValueError)
            except ValueError:
                print("Invalid option..!!")
                print("Re-enter your option...!!")
            finally:
                print("\n\n")

#MAIN
mainFunctionObject = answer(Folder)
mainFunctionObject.menu()
