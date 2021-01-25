import json

print("BookController loaded")

class Mix:
    def __init__(self, name="", ingredients={}):
        self.name = name
        self.ingredients = ingredients

def listMixNames():
    mixenNames = []

    with open("Receptboek.json") as f:
        mixen = json.load(f)
    for mix in mixen:
        mixName = mix["name"]
        mixenNames.append(mixName)
    return mixenNames

def listMixes():
    allMixen = {}

    with open("Receptboek.json") as f:
        mixen = json.load(f)
    for mix in mixen:
        mixName = mix["name"]
        composition = mix["composition"]
        allMixen.update(mixName, composition)
    return allMixen

def listMixenForPrint():
    msg = "Mixen nu in het systeem zijn: \n"
    mixList = listMixNames()

    for mixName in mixList:
        msg += mixName + "\n"

    return msg

def listAvailableMixes():
    mixenNames = []
    with open("Receptboek.json") as f:
        mixen = json.load(f)
    for mix in mixen:
        possible = True
        ingredienten = list(mix["composition"].keys())
        for ingredient in ingredienten:
            if not ingredient in listAvilibleFlessen():
                possible = False
                break
        if possible:
            mixenNames.append(mix["name"])
    
    return(mixenNames)

def listFlessen():
    with open('flessen.json') as json_file:
        data = json.load(json_file)
    return data

def listAvilibleFlessen():
    with open('flessenInPosition.json') as json_file:
        data = json.load(json_file)
    return data

def listFlessenForPrint():
    msg = "Flessen nu in het systeem zijn: \n"
    flesList = listFlessen()

    for flesName in flesList:
        msg += flesName + "\n"

    return msg

def addMix(newMix=Mix()):
    page = {
        "name": newMix.name,
        "composition": newMix.ingredients
    }

    with open('Receptboek.json') as json_file:
        data = json.load(json_file)
        data.append(page)
    outfile = open("Receptboek.json", "w+")
    json.dump(data, outfile, indent=4)
    outfile.close()

def getMix(name):
    return Mix(name, listMixes()[name])

def addFles(name):
    data = listFlessen()
    name = name.strip()
    name = name.title()
    data.append(name)
    data.sort()
    data = list(dict.fromkeys(data))

    outfile = open("flessen.json", "w+")
    json.dump(data, outfile, indent=0)
    outfile.close()
    print(name, "toegevoed")

def removeFles(name):
    data = listFlessen()
    name = name.strip()
    name = name.title()
    data.remove(name)
    data.sort()
    data = list(dict.fromkeys(data))

    outfile = open("flessen.json", "w+")
    json.dump(data, outfile, indent=0)
    outfile.close()
    print(name, "toegevoegd")

def updatePositionFlessen(position, flesname):
    with open("flessenInPosition.json") as f:
        places = json.load(f)
    places[position] = flesname
    outfile = open("flessenInPosition.json", "w+")

    json.dump(places, outfile, indent=0)
    outfile.close()


