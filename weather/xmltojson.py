import json
import xmltodict
import os
 
def xmltojson():
    filename = input("Enter XML file (Ex. \"weather.xml\") >> ")
    xmlData = openXMLFile(filename)

    if(not xmlData == ""):
        jsonData = convert(xmlData)
        jsonData = editFormat(jsonData, "\n")
        createJSONFile(jsonData, filename.replace(".xml", ".json"))

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
    with open(filename, "w") as fileOutput:
        fileOutput.write(jsonData)
        print("Convert XML to JSON Success.")
        print("Output file :", filename)

def editFormat(data, character):
    data = data[0 : data.find('\n')] + data[data.find('\n', data.find('\n') + 2):data.rfind('\n')]
    data = data.replace("\"@", "\"")
    data = data.replace("\n    ", "\n")
    return data

xmltojson()