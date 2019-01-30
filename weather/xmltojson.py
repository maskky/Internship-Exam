import json
import xmltodict
import os
 
def xmltojson():

    xmlData = openXMLFile(input("Enter XML file (Ex. \"input.xml\") >> "))

    if(not xmlData == ""):
        jsonData = convert(xmlData)
        jsonData = editFormat(jsonData, "\n")
        createJSONFile(jsonData, "output")

def openXMLFile(filename):
    if (os.path.exists(filename)):
        with open(filename, "r") as fileOpen:
            return fileOpen.read()
    else:
        print("No such file or directory.")
        return ""

def convert(xmlData):
    CONST_INDENT = 4
    jsonData = json.dumps(xmltodict.parse(xmlData), indent = CONST_INDENT)
    return jsonData

def createJSONFile(jsonData, filename):
    CONST_FILE_TYPE = "json"
    with open(filename + "." + CONST_FILE_TYPE, "w") as fileOutput:
        fileOutput.write(jsonData)
        print("Convert XML to JSON Success.")

def editFormat(data, character):
    data = data[0 : data.find('\n')] + data[data.find('\n', data.find('\n') + 2):data.rfind('\n')]
    data = data.replace("\"@", "\"")
    data = data.replace("\n    ", "\n")
    return data

xmltojson()