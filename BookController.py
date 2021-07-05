import json

print("BookController loaded")

class Mix:
    def __init__(self, name="", ingredients={}):
        self.name = name
        self.ingredients = ingredients

def listMixNames():
    with open("Receptboek.json") as json_file:
        book = json.load(json_file)
    
    mixes = list(book.keys())

    return mixes

#def listMixes():
#    allMixen = {}
#
 #   with open("Receptboek.json") as f:
  #      mixen = json.load(f)
#    for mix in mixen:
#        mixName = mix["name"]
 #       composition = mix["composition"]
  #      allMixen.update(mixName, composition)
   # return allMixen

def listMixenForPrint():
    msg = "Mixen nu in het systeem zijn: \n"
    mixList = listMixNames()

    for mixName in mixList:
        msg += mixName + "\n"

    return msg

#def listAvailableMixes():
#    mixenNames = []
#    with open("Receptboek.json") as f:
#        mixen = json.load(f)
#    for mix in mixen:
#        possible = True
#        ingredienten = list(mix["composition"].keys())
#        for ingredient in ingredienten:
#            if not ingredient in listAvilibleFlessen():
#                possible = False
#                break
#        if possible:
#            mixenNames.append(mix["name"])
    
#    return(mixenNames)

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

#returns list of possible mixes
def listAvailableMixes():

    availableMixes = []

    with open('flessenInPosition.json') as json_file:
        drinksInSystem = json.load(json_file)
    with open("Receptboek.json") as json_file:
        book = json.load(json_file)
    
    mixes = list(book.keys())

    #print(mixes)

    for name in mixes:
        mix = book[name]
        bottles = list(mix.keys())
        #print(name, bottles)
        possible = True
        for bottle in bottles:
            if bottle not in drinksInSystem: possible = False
        
        if possible: availableMixes.append(name)
        #print(list(mix.keys()))
    
    return availableMixes

def addMix(newMix=Mix()):
    page = {
        "name": newMix.name,
        "composition": newMix.ingredients
    }

    with open('Receptboek.json') as json_file:
        data = json.load(json_file)
        data[newMix.name] = newMix.ingredients
        
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

def getFlesPosition(flesnaam):
    with open('flessenInPosition.json') as json_file:
        data = json.load(json_file)
    position  = data.index(flesnaam)
    return position+1

def getIngrdients(mixname):
    with open('Receptboek.json') as json_file:
        data = json.load(json_file)
        return data[mixname]
    
#print(getIngrdients('baco'))
#print(getFlesPosition("Cola"))

print(listAvailableMixes())
print(listMixNames())

#veg = {
#            "Bacardi": 1,
 #           "Cola": 3
  #      }

#baco = Mix(name = "baco", ingredients=veg)

#addMix(baco)