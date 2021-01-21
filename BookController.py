import json

print("BookController loaded")

def listMixen():
        MixenNames = []

        with open("Receptboek.json") as f:
                mixen = json.load(f)
        for mix in mixen:
                mixName = mix["name"]
                MixenNames.append(mixName)
        return MixenNames

def listMixenForPrint():
        msg = "Mixen nu in het systeem zijn: \n"
        mixList = listMixen()

        for mixName in mixList:
                msg += mixName + "\n"
                
        return msg

#returnt een lijst van flessen
def listFlessen():
        with open('flessen.json') as json_file:
                data = json.load(json_file)
        return data

def listFlessenForPrint():
        msg = "Flessen nu in het systeem zijn: \n"
        flesList = listFlessen()

        for flesName in flesList:
                msg += flesName + "\n"
                
        return msg


def addMix(newDrinkName, ingredients):
        page = {
        "name" : newDrinkName,
        "composition": ingredients
        }

        with open('Receptboek.json') as json_file:
                data = json.load(json_file)
                data.append(page)
        outfile = open("Receptboek.json", "w+")
        json.dump(data, outfile, indent = 4)
        outfile.close()

def addFles(name):
        data = listFlessen()
        name = name.strip()
        name = name.title()
        data.append(name)
        data.sort()
        data = list(dict.fromkeys(data))

        outfile = open("flessen.json", "w+")
        json.dump(data, outfile, indent = 0)
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
        json.dump(data, outfile, indent = 0)
        outfile.close()
        print(name, "toegevoed")

def updatePositionFlessen(position, flesname):
        with open("flessenInPosition.json") as f:
                places = json.load(f)

        places[position]
