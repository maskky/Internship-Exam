import json
import xmltodict
 
def xmltojson():

    xmlData = openXMLFile("input.xml")
    jsonData = convert(xmlData)
    jsonData = editFormat(jsonData, "\n")
 
    createXMLFile(jsonData)

def openXMLFile(filename):
    with open(filename, "r") as fileOpen:
        return fileOpen.read()

def convert(xmlData):
    CONST_INDENT = 4
    jsonData = json.dumps(xmltodict.parse(xmlData), indent = CONST_INDENT)
    return jsonData

def createXMLFile(jsonData, filename):
    with open(filename, "w") as fileOutput:
        fileOutput.write(jsonData)

def editFormat(data, character):
    data = data[0 : data.find('\n')] + data[data.find('\n', data.find('\n') + 2):data.rfind('\n')]
    data = data.replace("\"@", "\"")
    data = data.replace("\n    ", "\n")
    return data

xmltojson()