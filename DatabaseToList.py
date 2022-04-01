from os import error

class DatabaseToList:
    def database_to_list():
        try:
            f = open("database.txt", "r")
        except OSError:
            print("File not found")
        
        fileOfLines = f.readlines()
        databaseList = []
        for i in fileOfLines:
            list = i.split(" @ ")
            list[1] = list[1].replace("\n", "")
            databaseList.append([list[0], list[1]]) #appends the string to a new list
        f.close()
        
        return databaseList