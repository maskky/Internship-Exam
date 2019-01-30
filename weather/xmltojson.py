import json
import xmltodict
 
def xmltojson():

    xmlData = openXMLFile("input")
    jsonData = convert(xmlData)
    jsonData = editFormat(jsonData, "\n")
 
    createXMLFile(jsonData, "output")

def openXMLFile(filename):
    CONST_FILE_TYPE = "xml"
    with open(filename + "." + CONST_FILE_TYPE, "r") as fileOpen:
        return fileOpen.read()

def convert(xmlData):
    CONST_INDENT = 4
    jsonData = json.dumps(xmltodict.parse(xmlData), indent = CONST_INDENT)
    return jsonData

def createXMLFile(jsonData, filename):
    CONST_FILE_TYPE = "json"
    with open(filename + "." + CONST_FILE_TYPE, "w") as fileOutput:
        fileOutput.write(jsonData)

def editFormat(data, character):
    data = data[0 : data.find('\n')] + data[data.find('\n', data.find('\n') + 2):data.rfind('\n')]
    data = data.replace("\"@", "\"")
    data = data.replace("\n    ", "\n")
    return data

xmltojson()