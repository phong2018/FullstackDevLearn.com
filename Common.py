import os 
import json
dataPath = os.getcwd() + "/database.txt"

# saveData
def saveData(newData, filePath = dataPath):  
    with open(filePath, "w") as outfile:
        json.dump(newData, outfile) 

# getData
def getData(filePath = dataPath):
    data = {}
    with open(filePath) as json_file:
        data = json.load(json_file)

    return data 